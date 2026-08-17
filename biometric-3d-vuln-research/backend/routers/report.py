"""
Report & CSV export endpoints.
GET /api/report/export/{task_id}  — export CSV for a video task
"""
from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter(prefix="/api/report", tags=["report"])


@router.get("/export/{task_id}")
async def export_csv(task_id: str):
    """
    Export all per-frame detection data as CSV.
    Returns a CSV file download.
    """
    # TODO: implement CSV generation from database
    csv_content = (
        "frame_index,label,fake_score,prob_real,prob_2d,prob_3d,bbox_x1,bbox_y1,bbox_x2,bbox_y2\n"
    )
    return PlainTextResponse(
        content=csv_content,
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=detection_report_{task_id}.csv"},
    )
