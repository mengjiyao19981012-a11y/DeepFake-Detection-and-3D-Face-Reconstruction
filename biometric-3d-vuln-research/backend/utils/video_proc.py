"""
Video processing utilities.
Frame extraction, annotated video composition, and video-level statistics.
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Generator, List, Optional, Tuple

import cv2
import numpy as np

from backend.config import VIDEO_SAMPLE_INTERVAL

logger = logging.getLogger(__name__)


def get_video_info(video_path: Path) -> dict:
    """Return basic video metadata."""
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise ValueError(f"Cannot open video: {video_path}")
    info = {
        "fps": cap.get(cv2.CAP_PROP_FPS),
        "total_frames": int(cap.get(cv2.CAP_PROP_FRAME_COUNT)),
        "width": int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        "height": int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        "duration_sec": 0.0,
    }
    if info["fps"] > 0:
        info["duration_sec"] = round(info["total_frames"] / info["fps"], 2)
    cap.release()
    return info


def iter_frames(
    video_path: Path,
    sample_interval: int = VIDEO_SAMPLE_INTERVAL,
) -> Generator[Tuple[int, np.ndarray], None, None]:
    """
    Yield (frame_index, frame_image) for every Nth frame.

    Parameters
    ----------
    video_path : Path
    sample_interval : int
        Process every Nth frame (1 = every frame).
    """
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise ValueError(f"Cannot open video: {video_path}")

    idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if idx % sample_interval == 0:
            yield idx, frame
        idx += 1
    cap.release()


def compose_annotated_video(
    input_path: Path,
    output_path: Path,
    annotated_frames: dict,  # {frame_index: np.ndarray}
    fps: float,
    width: int,
    height: int,
) -> Path:
    """
    Write an annotated video from pre-rendered frames.

    Parameters
    ----------
    annotated_frames : dict[int, np.ndarray]
        Mapping frame_index → annotated image (BGR).
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fourcc = cv2.VideoWriter_fourcc(*"avc1")  # H.264
    writer = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height))

    if not writer.isOpened():
        # fallback to mp4v
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height))

    for idx in sorted(annotated_frames.keys()):
        writer.write(annotated_frames[idx])

    writer.release()
    return output_path


def compute_video_statistics(frame_results: List[dict]) -> dict:
    """
    Aggregate per-frame detection results into video-level stats.

    Parameters
    ----------
    frame_results : list of dict
        Each dict: {"frame_idx": int, "faces": [...], "has_faces": bool}

    Returns
    -------
    dict with keys:
        total_frames, frames_with_faces, fake_frames,
        fake_ratio, avg_fake_score, max_fake_score
    """
    total = len(frame_results)
    if total == 0:
        return {
            "total_frames": 0,
            "frames_with_faces": 0,
            "fake_frames": 0,
            "fake_ratio": 0.0,
            "avg_fake_score": 0.0,
            "max_fake_score": 0.0,
        }

    frames_with_faces = sum(1 for r in frame_results if r.get("has_faces"))
    all_scores: List[float] = []
    fake_frame_count = 0

    for r in frame_results:
        for face in r.get("faces", []):
            score = face.get("fake_score", 0)
            all_scores.append(score)
            if not face.get("is_real", True):
                fake_frame_count += 1
                break  # count frame once if any fake face present

    return {
        "total_frames": total,
        "frames_with_faces": frames_with_faces,
        "fake_frames": fake_frame_count,
        "fake_ratio": round(fake_frame_count / total, 4) if total else 0.0,
        "avg_fake_score": round(np.mean(all_scores), 4) if all_scores else 0.0,
        "max_fake_score": round(np.max(all_scores), 4) if all_scores else 0.0,
    }
