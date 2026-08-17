"""
FastAPI dependency injection.
Provides singleton model instances and service objects.
"""
from __future__ import annotations

import logging
from functools import lru_cache

from backend.model_wrapper.yolo_wrapper import YOLOFaceDetector
from backend.model_wrapper.resnet_wrapper import ResNet50Wrapper
from backend.services.detect_service import DetectService

logger = logging.getLogger(__name__)

# ── Singleton model instances (loaded once at startup) ──
_yolo: YOLOFaceDetector | None = None
_resnet: ResNet50Wrapper | None = None


def get_yolo() -> YOLOFaceDetector:
    global _yolo
    if _yolo is None:
        _yolo = YOLOFaceDetector()
        _yolo.load()
    return _yolo


def get_resnet() -> ResNet50Wrapper:
    global _resnet
    if _resnet is None:
        _resnet = ResNet50Wrapper()
        _resnet.load()
    return _resnet


def get_detect_service() -> DetectService:
    return DetectService(yolo=get_yolo(), resnet=get_resnet())
