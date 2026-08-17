"""
Image preprocessing utilities.
Handles image loading, resizing, and format conversions.
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional, Tuple

import cv2
import numpy as np

logger = logging.getLogger(__name__)

# Default maximum dimension for downscaling large images
MAX_IMAGE_DIM = 2048


def load_image(path: Path) -> np.ndarray:
    """
    Load an image from disk as a BGR numpy array.

    Raises FileNotFoundError if the file does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"Image not found: {path}")
    img = cv2.imread(str(path))
    if img is None:
        raise ValueError(f"Failed to decode image: {path}")
    return img


def resize_to_max_dim(image: np.ndarray, max_dim: int = MAX_IMAGE_DIM) -> np.ndarray:
    """
    Downscale image so that its largest side ≤ max_dim, preserving aspect ratio.
    Returns the original image if it is already small enough.
    """
    h, w = image.shape[:2]
    if max(h, w) <= max_dim:
        return image
    scale = max_dim / max(h, w)
    new_w, new_h = int(w * scale), int(h * scale)
    return cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)


def bgr_to_rgb(image: np.ndarray) -> np.ndarray:
    """Convert BGR OpenCV image to RGB."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def rgb_to_bgr(image: np.ndarray) -> np.ndarray:
    """Convert RGB image to BGR OpenCV format."""
    return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


def save_image(image: np.ndarray, path: Path) -> None:
    """Save a BGR image to disk. Creates parent directories if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(path), image)


def get_image_dims(image: np.ndarray) -> Tuple[int, int]:
    """Return (width, height) of an image."""
    h, w = image.shape[:2]
    return w, h
