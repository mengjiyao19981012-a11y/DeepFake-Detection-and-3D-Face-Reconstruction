"""
Global configuration for the biometric vulnerability detection system.
All paths, device settings, and runtime parameters are centralized here.
"""
from pathlib import Path

# ──────────────────────────────────────────────
#  Project Root
# ──────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).parent.parent  # biometric-3d-vuln-research/
BACKEND_DIR = Path(__file__).parent

# ──────────────────────────────────────────────
#  Device  (M2 Max Apple Silicon)
# ──────────────────────────────────────────────
import torch
DEVICE = "mps" if torch.backends.mps.is_available() else "cpu"

# ──────────────────────────────────────────────
#  Model Weights
# ──────────────────────────────────────────────
WEIGHTS_DIR = PROJECT_ROOT / "weights"
YOLO_WEIGHTS = WEIGHTS_DIR / "yolov8" / "yolov8n.pt"
RESNET_WEIGHTS = WEIGHTS_DIR / "resnet50" / "best_model.pth"
RECON_WEIGHTS_DIR = WEIGHTS_DIR / "recon"

# ──────────────────────────────────────────────
#  Static / Output Directories
# ──────────────────────────────────────────────
STATIC_DIR = BACKEND_DIR / "static"
UPLOAD_DIR = STATIC_DIR / "uploads"
OUTPUT_IMG_DIR = STATIC_DIR / "output_img"
MODEL_3D_DIR = STATIC_DIR / "3d_model"

# ──────────────────────────────────────────────
#  Data Directories
# ──────────────────────────────────────────────
DATA_DIR = PROJECT_ROOT / "data"
SAMPLES_DIR = DATA_DIR / "samples"
REPORTS_DIR = DATA_DIR / "reports"

# ──────────────────────────────────────────────
#  Database
# ──────────────────────────────────────────────
DATABASE_URL = f"sqlite:///{DATA_DIR / 'app.db'}"

# ──────────────────────────────────────────────
#  Upload Constraints
# ──────────────────────────────────────────────
MAX_UPLOAD_SIZE_MB = 500          # 500 MB per file
ALLOWED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp"}
ALLOWED_VIDEO_EXTENSIONS = {".mp4", ".avi", ".mov", ".mkv"}

# ──────────────────────────────────────────────
#  Detection Parameters
# ──────────────────────────────────────────────
YOLO_CONF_THRESHOLD = 0.35        # YOLO face detection confidence
YOLO_IOU_THRESHOLD = 0.45
RESNET_INPUT_SIZE = (224, 224)     # ResNet50 input crop size
FAKE_RISK_THRESHOLD = 0.5          # > 0.5 → classified as fake

# ──────────────────────────────────────────────
#  Video Processing
# ──────────────────────────────────────────────
VIDEO_SAMPLE_INTERVAL = 10         # process every Nth frame (reduce load)
VIDEO_MAX_PARALLEL_TASKS = 2       # prevent memory blow-up on M2

# ──────────────────────────────────────────────
#  Ensure directories exist
# ──────────────────────────────────────────────
for _d in [UPLOAD_DIR, OUTPUT_IMG_DIR, MODEL_3D_DIR, SAMPLES_DIR, REPORTS_DIR]:
    _d.mkdir(parents=True, exist_ok=True)
