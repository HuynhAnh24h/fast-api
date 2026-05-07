from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password, compare_password


# REGISTER
def create_user(
    db: Session,
    email: str,
    password: str
):

    # check empty
    if not email or not password:
        raise HTTPException(
            status_code=400,
            detail="Email or password cannot be empty"
        )

    # check email exists
    user_email = db.query(User).filter(
        User.email == email
    ).first()

    if user_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    # hash password
    hashed_password = hash_password(password)

    # create user
    user = User(
        email=email,
        password=hashed_password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


# LOGIN
def login_user(
    db: Session,
    email: str,
    password: str
):

    # find user
    user = db.query(User).filter(
        User.email == email
    ).first()

    # check user exists
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User does not exist"
        )

    # verify password
    is_valid = compare_password(
        password,
        user.password
    )

    if not is_valid:
        raise HTTPException(
            status_code=400,
            detail="Password incorrect"
        )

    return user