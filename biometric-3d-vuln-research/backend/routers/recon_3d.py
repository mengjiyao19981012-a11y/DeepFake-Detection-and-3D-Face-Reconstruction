"""
3D face reconstruction endpoints.
POST /api/recon/3dface  — generate 3D model from a real-face image
"""
from fastapi import APIRouter

router = APIRouter(prefix="/api/recon", tags=["reconstruction"])


@router.post("/3dface")
async def reconstruct_3d_face():
    """Generate OBJ 3D face model from a real-face image."""
    # TODO: implement with recon_service
    return {
        "status": "not_implemented",
        "message": "3D reconstruction endpoint not yet implemented.",
    }
