"""
Detection REST endpoints.
POST /api/detect/image  — single image detection
POST /api/detect/video  — upload video, create async task
"""
from __future__ import annotations

import logging
import uuid
from pathlib import Path

from fastapi import APIRouter, UploadFile, File, HTTPException, Depends

from backend.config import UPLOAD_DIR, STATIC_DIR, ALLOWED_IMAGE_EXTENSIONS, ALLOWED_VIDEO_EXTENSIONS, MAX_UPLOAD_SIZE_MB
from backend.services.detect_service import DetectService
from backend.dependencies import get_detect_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/detect", tags=["detection"])


def _validate_extension(filename: str, allowed: set) -> str:
    ext = Path(filename).suffix.lower()
    if ext not in allowed:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type '{ext}'. Allowed: {allowed}",
        )
    return ext


# ──────────────────────────────────────────────
#  POST /api/detect/image
# ──────────────────────────────────────────────
@router.post("/image")
async def detect_image(
    file: UploadFile = File(...),
    service: DetectService = Depends(get_detect_service),
):
    """
    Upload a single image and return face detection + classification results.
    """
    _validate_extension(file.filename or "unknown.jpg", ALLOWED_IMAGE_EXTENSIONS)

    # Save uploaded file
    file_id = uuid.uuid4().hex[:12]
    ext = Path(file.filename).suffix  # type: ignore[arg-type]
    save_path = UPLOAD_DIR / f"{file_id}{ext}"
    content = await file.read()
    if len(content) > MAX_UPLOAD_SIZE_MB * 1024 * 1024:
        raise HTTPException(status_code=413, detail=f"File exceeds {MAX_UPLOAD_SIZE_MB} MB limit")
    save_path.write_bytes(content)

    try:
        result = service.detect_image(save_path, annotate=True)
    except Exception as e:
        logger.exception("Image detection failed")
        raise HTTPException(status_code=500, detail=str(e))

    # Convert local path to relative URL path
    if result.get("annotated_path"):
        ap = Path(result["annotated_path"])
        # make it relative to static dir so frontend can fetch via /static/...
        try:
            result["annotated_path"] = "/static/" + str(ap.relative_to(STATIC_DIR)).replace("\\", "/")
        except ValueError:
            pass

    return {
        "file_id": file_id,
        "original_name": file.filename,
        **result,
    }


# ──────────────────────────────────────────────
#  POST /api/detect/video
# ──────────────────────────────────────────────
@router.post("/video")
async def detect_video(
    file: UploadFile = File(...),
):
    """
    Upload a video file and create an asynchronous detection task.
    Returns a task_id that can be polled via GET /api/video/task/{task_id}.
    """
    _validate_extension(file.filename or "unknown.mp4", ALLOWED_VIDEO_EXTENSIONS)

    task_id = uuid.uuid4().hex[:16]
    ext = Path(file.filename).suffix  # type: ignore[arg-type]
    save_path = UPLOAD_DIR / f"{task_id}{ext}"
    content = await file.read()
    if len(content) > MAX_UPLOAD_SIZE_MB * 1024 * 1024:
        raise HTTPException(status_code=413, detail=f"File exceeds {MAX_UPLOAD_SIZE_MB} MB limit")
    save_path.write_bytes(content)

    # TODO: enqueue background task via video_service
    # For now, return the task_id placeholder
    return {
        "task_id": task_id,
        "original_name": file.filename,
        "status": "pending",
        "message": "Video uploaded. Background processing will begin shortly.",
    }
