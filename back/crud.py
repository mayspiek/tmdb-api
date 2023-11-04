from sqlalchemy.orm import Session
import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db_user.name = user.name
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()
    return user_id

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, name=user.name, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def favorite_movie(db: Session, tmdb_id: int, user_id: int):
    db_movie = db.query(models.Movie).filter(models.Movie.tmdb_id).first()
    print(tmdb_id)
    if db_movie is None:
        db_movie = models.Movie(tmdb_id=tmdb_id, user_id=user_id)
        db.add(db_movie)
        db.commit()
        db.refresh(db_movie)
    return db_movie

def get_favorites(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Movie).offset(skip).limit(limit).all()
