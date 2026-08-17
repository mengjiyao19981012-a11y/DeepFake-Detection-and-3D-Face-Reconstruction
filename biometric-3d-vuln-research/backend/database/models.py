"""
SQLAlchemy ORM models for the detection system.
"""
from __future__ import annotations

import datetime
from pathlib import Path

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
    Text,
    ForeignKey,
    create_engine,
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


# ──────────────────────────────────────────────
#  Detection Record  (per frame, per face)
# ──────────────────────────────────────────────
class DetectionRecord(Base):
    __tablename__ = "detection_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(String(64), index=True, nullable=False)
    frame_index = Column(Integer, nullable=False)

    # bounding box
    bbox_x1 = Column(Integer, nullable=False)
    bbox_y1 = Column(Integer, nullable=False)
    bbox_x2 = Column(Integer, nullable=False)
    bbox_y2 = Column(Integer, nullable=False)

    # classification result
    label = Column(String(32), nullable=False)  # real / 2d_deepfake / 3d_synthetic
    fake_score = Column(Float, nullable=False)
    prob_real = Column(Float, nullable=False)
    prob_2d = Column(Float, nullable=False)
    prob_3d = Column(Float, nullable=False)

    is_real = Column(Boolean, nullable=False)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)


# ──────────────────────────────────────────────
#  Video Task
# ──────────────────────────────────────────────
class VideoTask(Base):
    __tablename__ = "video_tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(String(64), unique=True, index=True, nullable=False)

    original_filename = Column(String(256), nullable=False)
    status = Column(String(32), default="pending")  # pending / processing / done / failed

    # video metadata
    total_frames = Column(Integer, default=0)
    processed_frames = Column(Integer, default=0)
    fps = Column(Float, default=0.0)
    duration_sec = Column(Float, default=0.0)

    # statistics (filled after completion)
    frames_with_faces = Column(Integer, default=0)
    fake_frames = Column(Integer, default=0)
    fake_ratio = Column(Float, default=0.0)
    avg_fake_score = Column(Float, default=0.0)
    max_fake_score = Column(Float, default=0.0)

    annotated_video_path = Column(String(512), nullable=True)

    error_message = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


# ──────────────────────────────────────────────
#  3D Reconstruction Task
# ──────────────────────────────────────────────
class ReconTask(Base):
    __tablename__ = "recon_tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(String(64), unique=True, index=True, nullable=False)

    source_image = Column(String(512), nullable=False)
    status = Column(String(32), default="pending")  # pending / processing / done / failed

    obj_path = Column(String(512), nullable=True)
    texture_path = Column(String(512), nullable=True)
    preview_path = Column(String(512), nullable=True)
    landmarks_path = Column(String(512), nullable=True)

    error_message = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
