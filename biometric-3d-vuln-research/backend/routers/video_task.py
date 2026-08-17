"""
Video async task endpoints.
GET /api/video/task/{task_id}  — query video processing status & results
"""
from fastapi import APIRouter

router = APIRouter(prefix="/api/video", tags=["video"])


@router.get("/task/{task_id}")
async def get_video_task(task_id: str):
    """
    Query video processing status, per-frame results, and statistics.

    Returns status: pending | processing | done | failed
    When done, includes stats dict with total_frames, fake_ratio, avg_fake_score, etc.
    """
    # TODO: implement with video_service + database lookup
    return {
        "task_id": task_id,
        "status": "pending",
        "progress": 0,
        "stats": None,
        "message": "Video task endpoint not yet implemented.",
    }
