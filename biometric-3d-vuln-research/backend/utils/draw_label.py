"""
Annotation drawing utilities.
Draws bounding boxes and risk-score labels on images.
"""
from __future__ import annotations

from typing import Dict, List, Tuple

import cv2
import numpy as np

# Color constants (BGR)
GREEN = (0, 220, 100)
RED = (40, 60, 240)
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)

FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.55
THICKNESS = 2


def draw_detection(
    image: np.ndarray,
    faces: List[Dict],
) -> np.ndarray:
    """
    Draw bounding boxes and labels on a copy of the image.

    Each face dict should contain:
        bbox:   (x1, y1, x2, y2)
        label:  "real" | "2d_deepfake" | "3d_synthetic"
        fake_score: float 0..1

    Green box → real face
    Red box   → fake face
    """
    canvas = image.copy()

    for face in faces:
        x1, y1, x2, y2 = face["bbox"]
        label = face["label"]
        score = face["fake_score"]
        is_real = face.get("is_real", label == "real")

        color = GREEN if is_real else RED
        status = "Real" if is_real else "Fake"

        # Draw bounding box
        cv2.rectangle(canvas, (x1, y1), (x2, y2), color, THICKNESS)

        # Label text
        text = f"{status} | risk: {score:.2f}"

        # Background rectangle for text readability
        (tw, th), baseline = cv2.getTextSize(text, FONT, FONT_SCALE, 1)
        cv2.rectangle(
            canvas,
            (x1, y1 - th - 8),
            (x1 + tw + 6, y1),
            color,
            cv2.FILLED,
        )
        cv2.putText(
            canvas,
            text,
            (x1 + 3, y1 - 5),
            FONT,
            FONT_SCALE,
            WHITE,
            1,
            cv2.LINE_AA,
        )

    return canvas


def draw_single_face_highlight(
    image: np.ndarray,
    bbox: Tuple[int, int, int, int],
    color: Tuple[int, int, int] = GREEN,
) -> np.ndarray:
    """Draw a single highlighted face box (used for 3D-recon preview)."""
    canvas = image.copy()
    x1, y1, x2, y2 = bbox
    cv2.rectangle(canvas, (x1, y1), (x2, y2), color, 2)
    return canvas
