from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.dependencies import get_db, get_current_user
from app.models.swap import Swap
from app.schemas.swap import SwapCreate, SwapResponse
from app.api.v1.models import UserResponse

router = APIRouter()

@router.post("/", response_model=SwapResponse)
async def create_swap(swap: SwapCreate, db: Session = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):
    db_swap = Swap(**swap.dict(), initiator_id=current_user.id, status="pending")
    db.add(db_swap)
    db.commit()
    db.refresh(db_swap)
    return SwapResponse.from_orm(db_swap)

@router.get("/me", response_model=List[SwapResponse])
async def list_swaps(db: Session = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):
    swaps = db.query(Swap).filter(
        (Swap.initiator_id == current_user.id) | (Swap.receiver_id == current_user.id)
    ).all()
    return [SwapResponse.from_orm(swap) for swap in swaps]

@router.post("/{swap_id}/accept")
async def accept_swap(swap_id: int, db: Session = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):
    swap = db.query(Swap).filter(Swap.id == swap_id, Swap.receiver_id == current_user.id).first()
    if not swap:
        raise HTTPException(status_code=404, detail="Swap not found or not authorized")
    swap.status = "accepted"
    db.commit()
    return {"detail": "Swap accepted"}

@router.post("/{swap_id}/reject")
async def reject_swap(swap_id: int, db: Session = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):
    swap = db.query(Swap).filter(Swap.id == swap_id, Swap.receiver_id == current_user.id).first()
    if not swap:
        raise HTTPException(status_code=404, detail="Swap not found or not authorized")
    swap.status = "rejected"
    db.commit()
    return {"detail": "Swap rejected"}

@router.delete("/{swap_id}")
async def delete_swap(swap_id: int, db: Session = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):
    swap = db.query(Swap).filter(Swap.id == swap_id, Swap.initiator_id == current_user.id).first()
    if not swap:
        raise HTTPException(status_code=404, detail="Swap not found or not authorized")
    swap.status = "deleted"
    db.commit()
    return {"detail": "Swap deleted"}