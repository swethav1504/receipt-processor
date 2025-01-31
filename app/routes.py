from fastapi import APIRouter, HTTPException
from app.models import Receipt
from app.store import save_receipt, get_receipt
from app.points import calculate_points

router = APIRouter()

@router.post("/receipts/process")
def process_receipt(receipt: Receipt):
    receipt_id = save_receipt(receipt)
    return {"id": receipt_id}

@router.get("/receipts/{id}/points")
def get_points(id: str):
    receipt = get_receipt(id)
    if receipt is None:
        raise HTTPException(status_code=404, detail="Receipt not found")

    points = calculate_points(receipt)
    return {"points": points}
