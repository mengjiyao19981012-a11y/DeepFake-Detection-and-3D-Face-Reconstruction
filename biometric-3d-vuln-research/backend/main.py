"""
FastAPI application entry point.
Pre-loads YOLOv8 + ResNet50 models at startup and registers all routers.
"""
from __future__ import annotations

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.config import DEVICE, YOLO_WEIGHTS, RESNET_WEIGHTS, STATIC_DIR
from backend.database.db import init_db
from backend.dependencies import get_yolo, get_resnet
from backend.routers import detect, video_task, recon_3d, report

# ── Logging ──
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

# ── FastAPI app ──
app = FastAPI(
    title="Biometric 3D Vulnerability Detection",
    version="1.0.0",
    description="YOLOv8 + ResNet50 dual-backbone deepfake detection with 3D face reconstruction",
)

# ── CORS ──
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Serve static files (annotated images, 3D models, etc.) ──
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# ── Register routers ──
app.include_router(detect.router)
app.include_router(video_task.router)
app.include_router(recon_3d.router)
app.include_router(report.router)


# ── Startup event: preload models ──
@app.on_event("startup")
async def startup_event():
    logger.info("Starting server on device=%s", DEVICE)
    logger.info("YOLO weights: %s", YOLO_WEIGHTS)
    logger.info("ResNet weights: %s", RESNET_WEIGHTS)

    # Initialize database
    init_db()

    # Preload models into MPS memory
    logger.info("Preloading YOLOv8...")
    get_yolo()
    logger.info("Preloading ResNet50...")
    get_resnet()

    logger.info("All models loaded. Server is ready.")


@app.get("/")
async def root():
    return {"service": "Biometric 3D Vuln Detection API", "status": "running"}
