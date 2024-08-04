from fastapi import APIRouter, Depends, HTTPException, status
from datetime import timedelta, timezone
from .. import schemas, models, token
from fastapi.security import OAuth2PasswordRequestForm

from ..database import get_db

from ..hashing import Hash

from sqlalchemy.orm import Session


router = APIRouter(
    tags=["Authentication"],
)


@router.post("/login", response_model=schemas.Token)
def login(
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials"
        )

    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect Password"
        )
    # generate JWT token
    access_token = token.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
