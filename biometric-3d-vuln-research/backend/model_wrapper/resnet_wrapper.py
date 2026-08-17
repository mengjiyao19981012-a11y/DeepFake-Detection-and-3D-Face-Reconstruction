"""
ResNet50 face authenticity classifier wrapper.
Loads the custom-trained ResNet50 weights and performs inference
to distinguish Real / 2D-Deepfake / 3D-Synthetic faces.
"""
from __future__ import annotations

import logging
from typing import Dict, Optional, Tuple

import numpy as np
import torch
import torch.nn as nn
import torchvision.transforms as T
from PIL import Image

from backend.config import DEVICE, RESNET_INPUT_SIZE, RESNET_WEIGHTS

logger = logging.getLogger(__name__)

# Class labels corresponding to the model output indices
CLASS_LABELS = ["real", "2d_deepfake", "3d_synthetic"]

# Image preprocessing pipeline (matches training)
_transform = T.Compose(
    [
        T.Resize(RESNET_INPUT_SIZE),
        T.ToTensor(),
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)


class ResNet50Classifier(nn.Module):
    """
    Wraps a ResNet50 backbone with a custom classification head.
    The architecture assumes 3 output classes:
        0 → real
        1 → 2d_deepfake
        2 → 3d_synthetic
    """

    def __init__(self, num_classes: int = 3) -> None:
        super().__init__()
        import torchvision.models as models

        backbone = models.resnet50(weights=None)
        in_features = backbone.fc.in_features
        backbone.fc = nn.Identity()  # remove original fc
        self.backbone = backbone
        self.classifier = nn.Linear(in_features, num_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        features = self.backbone(x)
        return self.classifier(features)


class ResNet50Wrapper:
    """Singleton-style wrapper for the ResNet50 authenticity classifier."""

    def __init__(self, weights_path: Optional[str] = None) -> None:
        self.weights_path = str(weights_path or RESNET_WEIGHTS)
        self.device = DEVICE
        self._model: Optional[ResNet50Classifier] = None

    def load(self) -> None:
        """Load weights into the model (call once at startup)."""
        if self._model is not None:
            return
        logger.info("Loading ResNet50 classifier from %s", self.weights_path)
        self._model = ResNet50Classifier(num_classes=3)
        state_dict = torch.load(self.weights_path, map_location="cpu", weights_only=True)
        # Handle possible "module." prefix from DataParallel training
        if any(k.startswith("module.") for k in state_dict):
            state_dict = {k.replace("module.", ""): v for k, v in state_dict.items()}
        self._model.load_state_dict(state_dict, strict=False)
        self._model.to(self.device)
        self._model.eval()
        logger.info("ResNet50 classifier loaded on %s.", self.device)

    @property
    def model(self) -> ResNet50Classifier:
        if self._model is None:
            self.load()
        return self._model  # type: ignore[return-value]

    @torch.no_grad()
    def classify(self, face_image: np.ndarray) -> Dict:
        """
        Classify a single face crop (BGR numpy array).

        Returns
        -------
        {
            "label": str,             # "real" | "2d_deepfake" | "3d_synthetic"
            "fake_score": float,      # 0..1, higher = more likely fake
            "probs": {                # per-class probabilities
                "real": float,
                "2d_deepfake": float,
                "3d_synthetic": float,
            },
            "is_real": bool,
        }
        """
        # BGR → RGB PIL
        pil_img = Image.fromarray(face_image[:, :, ::-1])
        tensor = _transform(pil_img).unsqueeze(0).to(self.device)

        logits = self.model(tensor)
        probs = torch.softmax(logits, dim=1).squeeze(0).cpu().numpy()

        real_prob = float(probs[0])
        fake2d_prob = float(probs[1])
        fake3d_prob = float(probs[2])

        fake_score = round(fake2d_prob + fake3d_prob, 4)
        predicted_idx = int(np.argmax(probs))
        label = CLASS_LABELS[predicted_idx]

        return {
            "label": label,
            "fake_score": fake_score,
            "probs": {
                "real": round(real_prob, 4),
                "2d_deepfake": round(fake2d_prob, 4),
                "3d_synthetic": round(fake3d_prob, 4),
            },
            "is_real": label == "real",
        }
