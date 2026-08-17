"""
Dual-backbone detection service.
Orchestrates YOLOv8 face detection → ResNet50 classification → annotation.
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np

from backend.config import (
    OUTPUT_IMG_DIR,
    FAKE_RISK_THRESHOLD,
)
from backend.model_wrapper.yolo_wrapper import YOLOFaceDetector
from backend.model_wrapper.resnet_wrapper import ResNet50Wrapper
from backend.utils.draw_label import draw_detection
from backend.utils.image_proc import load_image, resize_to_max_dim, save_image

logger = logging.getLogger(__name__)


class DetectService:
    """Orchestrates the full YOLO + ResNet pipeline for a single image."""

    def __init__(
        self,
        yolo: YOLOFaceDetector,
        resnet: ResNet50Wrapper,
    ) -> None:
        self.yolo = yolo
        self.resnet = resnet

    def detect_image(self, image_path: Path, annotate: bool = True) -> dict:
        """
        Run full detection pipeline on a single image file.

        Returns
        -------
        {
            "faces": [
                {
                    "bbox": [x1, y1, x2, y2],
                    "label": str,
                    "fake_score": float,
                    "probs": {...},
                    "is_real": bool,
                },
                ...
            ],
            "face_count": int,
            "has_fake": bool,
            "annotated_path": str | None,
            "summary": {
                "real_count": int,
                "fake_count": int,
                "avg_fake_score": float,
                "max_fake_score": float,
            },
        }
        """
        image = load_image(image_path)
        image = resize_to_max_dim(image)

        # ── Stage 1: YOLO face detection ──
        bboxes = self.yolo.detect(image)
        if not bboxes:
            return {
                "faces": [],
                "face_count": 0,
                "has_fake": False,
                "annotated_path": None,
                "summary": {
                    "real_count": 0,
                    "fake_count": 0,
                    "avg_fake_score": 0.0,
                    "max_fake_score": 0.0,
                },
            }

        # ── Stage 2: ResNet classification per face ──
        faces: List[Dict] = []
        for bbox in bboxes:
            x1, y1, x2, y2, yolo_conf = bbox
            crop = self.yolo.crop_face(image, (x1, y1, x2, y2))
            if crop.size == 0:
                continue
            result = self.resnet.classify(crop)
            result["bbox"] = [x1, y1, x2, y2]
            result["yolo_conf"] = round(yolo_conf, 4)
            faces.append(result)

        # ── Summaries ──
        real_count = sum(1 for f in faces if f["is_real"])
        fake_count = len(faces) - real_count
        scores = [f["fake_score"] for f in faces]
        avg_score = round(np.mean(scores), 4) if scores else 0.0
        max_score = round(max(scores), 4) if scores else 0.0

        # ── Annotated image ──
        annotated_path: Optional[str] = None
        if annotate and faces:
            annotated = draw_detection(image, faces)
            out_name = f"annotated_{image_path.stem}.jpg"
            out_path = OUTPUT_IMG_DIR / out_name
            save_image(annotated, out_path)
            annotated_path = str(out_path)

        return {
            "faces": faces,
            "face_count": len(faces),
            "has_fake": fake_count > 0,
            "annotated_path": annotated_path,
            "summary": {
                "real_count": real_count,
                "fake_count": fake_count,
                "avg_fake_score": avg_score,
                "max_fake_score": max_score,
            },
        }
