# uvicorn pycine:app --reload

from pprint import pprint
from fastapi import FastAPI
from tmdb import get_json
from typing import List


app = FastAPI()

from fastapi.middleware.cors import (
     CORSMiddleware
)
# habilita CORS (permite que o Svelte acesse o fastapi)
origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:5173/UserList",
    "http://localhost:5173/favorites",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# USERS
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(bind=engine)


## MOVIES

# get movies from API and return a list of movies
@app.get("/movies")
async def filmes_populares():
    data = get_json(
        "/discover/movie", "?sort_by=vote_count.desc"
    )
    results = data['results']
    filtro = []
    for movie in results:
        filtro.append({"title": movie['original_title'],
                       "image": f"https://image.tmdb.org/t/p/w185{movie['poster_path']}",
                       "tmdb_id": movie['id']})
    return filtro

# get list of movies from API passing title as a parameter and return a list of movies
@app.get("/movies/{title}")
async def get_movies(title: str):
    movie_title = get_json(
        "/search/movie", f"?query={title}&include_adult=true&language=en-US"
    )

    results = movie_title['results']
    filtro = []

    for movie in results:
        movie_id = get_json("/movie", f"/{movie['id']}?language=en-US")
        filtro.append({
            'id': movie_id['id'],
            'title': movie_id['title'],
            'image': movie_id['poster_path'],
        })
    # filtro.sort(reverse=True, key=lambda artist:artist['rank'])
    return filtro

## favorita o filme
@app.post("/favorites/movies/{user_id}/{tmdb_id}", response_model=schemas.Movie)
def favorite_movie(user_id:int, tmdb_id:int, db: Session = Depends(get_db)):
    return crud.favorite_movie(db=db, user_id = user_id, tmdb_id=tmdb_id)

# PEGA TODOS OS FILMES FAVORITADOS DO USUÁRIO
@app.get("/favorites/movies/{user_id}")
async def get_favorites(user_id: int, db: Session = Depends(get_db)):
    db_movies = crud.get_favorites(db, user_id=user_id)
    # pegando os ids dos filmes favoritados do banco de dados
    tmdb_ids = [movie.tmdb_id for movie in db_movies]
    filtro = []
    if db_movies is None:
        raise HTTPException(status_code=404, detail="User not found")
    for movie_id in tmdb_ids:
        movie_api = get_json(
            f"/movie/{movie_id}?language=en-US"
        )
        filtro.append({
            'movie_id' : movie_api.get('id'),
            'title' : movie_api.get('original_title'),
            'sinopse' : movie_api.get('overview'),
            'image' : movie_api.get('poster_path')
        })        
    return filtro

@app.get("/favorites/movies/{user_id}/{tmdb_id}", response_model=schemas.Movie)
def get_favorite_by_id(user_id: int, tmdb_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_favorite_by_id(db, user_id=user_id, tmdb_id=tmdb_id)
    if db_movie is not None:
        return db_movie
    else:
        raise HTTPException(status_code=404, detail="Movie not found")

##DELETAR FILMES DO FAVORITOS
@app.delete("/favorites/movies/{user_id}/{tmdb_id}", response_model=schemas.Movie)
def delete_favorite(user_id: int, tmdb_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_favorite_by_id(db, user_id=user_id, tmdb_id=tmdb_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    crud.delete_favorite(db, user_id=user_id, tmdb_id=tmdb_id)
    return db_movie

# ARTISTS

# get movies from API and return a list of movies
@app.get("/artists")
async def artists_populares():
    data = get_json(
        "/trending/person/week", "?language=en-US"
    )
    results = data['results']
    # print(results)
    filtro = []
    for artist in results:
        artist_id = get_json("/person", f"/{artist['id']}?language=en-US")
        pprint(artist_id)
        filtro.append({
            'id': artist_id['id'],
            'name': artist_id['name'],
            'rank': artist_id['popularity'],
            'biography': artist_id['biography'],
            'birthday': artist_id['birthday'],
            "profile_path": artist_id['profile_path']
        })
    filtro.sort(reverse=True, key=lambda artist:artist['rank'])
    return filtro

# get list of artists from API passing name as a parameter and return a list of artists
@app.get("/artists/{name}")
async def get_artista(name: str):
    artist_name = get_json(
        "/search/person", f"?query={name}&language=en-US"
    )

    results = artist_name['results']
    filtro = []

    for artist in results:
        artist_id = get_json("/person", f"/{artist['id']}?language=en-US")
        filtro.append({
            'id': artist_id['id'],
            'name': artist_id['name'],
            'rank': artist_id['popularity'],
            'biography': artist_id['biography'],
            'birthday': artist_id['birthday'],
            "profile_path": artist_id['profile_path']
        })
    filtro.sort(reverse=True, key=lambda artist:artist['rank'])
    return filtro

# favorita o artista
@app.post("/favorites/artists/{user_id}/{tmdb_artist_id}", response_model=schemas.Artist)
def favorite_artist(user_id:int, tmdb_artist_id:int, db: Session = Depends(get_db)):
    return crud.favorite_artist(db=db, user_id = user_id, tmdb_artist_id = tmdb_artist_id)

# get artists favorited by user
@app.get("/favorites/artists/{user_id}")
async def get_favorites_artists(user_id: int, db: Session = Depends(get_db)):
    db_artists = crud.get_favorites_artists(db, user_id=user_id)
    # pegando os ids dos artistas favoritados do banco de dados
    tmdb_ids = [artist.tmdb_artist_id for artist in db_artists]
    filtro = []
    if db_artists is None:
        raise HTTPException(status_code=404, detail="User not found")
    for artist_id in tmdb_ids:
        tmdb_api = get_json(
            f"/person/{artist_id}?language=en-US"
        )
        filtro.append({
            'artist_id' : tmdb_api.get('id'),
            'name' : tmdb_api.get('name'),
            'rank' : tmdb_api.get('popularity'),
            'biography' : tmdb_api.get('biography'),
            'image' : tmdb_api.get('profile_path')
        })        
    return filtro

# get artist favorited by user
@app.get("/favorites/artists/{user_id}/{tmdb_artist_id}", response_model=schemas.Artist)
def get_favorite_artist_by_id(user_id: int, tmdb_artist_id: int, db: Session = Depends(get_db)):
    db_artist = crud.get_favorite_artist_by_id(db, user_id = user_id, tmdb_artist_id = tmdb_artist_id)
    if db_artist is not None:
        return db_artist
    else:
        raise HTTPException(status_code=404, detail="Artist not found")
    
# delete artist favorited by user
@app.delete("/favorites/artists/{user_id}/{tmdb_artist_id}", response_model=schemas.Artist)
def delete_favorite(user_id: int, tmdb_artist_id: int, db: Session = Depends(get_db)):
    db_artist = crud.get_favorite_artist_by_id(db, user_id=user_id, tmdb_artist_id = tmdb_artist_id)
    if db_artist is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    crud.delete_favorite_artist(db, user_id=user_id, tmdb_artist_id = tmdb_artist_id)
    return db_artist

## USERS ##

# get all users
@app.get("/users", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

## ATUALIZAZÇAO DE USUARIO
@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user = crud.update_user(db, user_id=user_id, user=user)
    return db_user

## DELETAR USUARIO
@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    crud.delete_user(db, user_id=user_id)
    return db_user



# uvicorn pycine:app --reload