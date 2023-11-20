from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    
    movies = relationship("Movie", back_populates="user")
    artists = relationship("Artist", back_populates="user")

# filmes favoritos 
class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    tmdb_id = Column(Integer)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="movies")

# filmes favoritos 
class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, index=True)
    tmdb_artist_id = Column(Integer)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="artists")

    
