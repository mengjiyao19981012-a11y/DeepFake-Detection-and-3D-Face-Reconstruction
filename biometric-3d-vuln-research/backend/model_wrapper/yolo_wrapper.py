"""
YOLOv8 face detection wrapper.
Loads the official YOLOv8 model, runs inference on a single image,
and returns bounding boxes of detected faces.
"""
from __future__ import annotations

import logging
from typing import List, Optional, Tuple

import numpy as np
import torch
from ultralytics import YOLO

from backend.config import DEVICE, YOLO_CONF_THRESHOLD, YOLO_IOU_THRESHOLD, YOLO_WEIGHTS

logger = logging.getLogger(__name__)

# Bounding box type: (x1, y1, x2, y2, confidence)
BBox = Tuple[int, int, int, int, float]


class YOLOFaceDetector:
    """Singleton-style wrapper for YOLOv8 face detection on Apple Silicon MPS."""

    def __init__(self, weights_path: Optional[str] = None) -> None:
        self.weights_path = str(weights_path or YOLO_WEIGHTS)
        self.device = DEVICE
        self._model: Optional[YOLO] = None

    def load(self) -> None:
        """Load the YOLO model into memory (call once at startup)."""
        if self._model is not None:
            return
        logger.info("Loading YOLOv8 face detector from %s on device=%s", self.weights_path, self.device)
        self._model = YOLO(self.weights_path)
        # Ultralytics will auto-detect MPS; we explicitly set the device for clarity
        self._model.to(self.device)
        logger.info("YOLOv8 loaded successfully.")

    @property
    def model(self) -> YOLO:
        if self._model is None:
            self.load()
        return self._model  # type: ignore[return-value]

    def detect(self, image: np.ndarray) -> List[BBox]:
        """
        Run face detection on a single BGR image (numpy array H×W×3).

        Returns
        -------
        List of (x1, y1, x2, y2, confidence) for every detected face.
        Returns an empty list if no face is found.
        """
        results = self.model(
            image,
            conf=YOLO_CONF_THRESHOLD,
            iou=YOLO_IOU_THRESHOLD,
            verbose=False,
        )
        faces: List[BBox] = []
        for result in results:
            if result.boxes is None:
                continue
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                conf = float(box.conf[0])
                faces.append((int(x1), int(y1), int(x2), int(y2), conf))
        return faces

    def crop_face(self, image: np.ndarray, bbox: BBox) -> np.ndarray:
        """Crop the face region from the image given a bounding box."""
        x1, y1, x2, y2, _ = bbox
        h, w = image.shape[:2]
        # guard against out-of-bounds
        x1 = max(0, x1)
        y1 = max(0, y1)
        x2 = min(w, x2)
        y2 = min(h, y2)
        return image[y1:y2, x1:x2]
