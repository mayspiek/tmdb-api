from fastapi import FastAPI
from tmdb import get_json

app = FastAPI()

from fastapi.middleware.cors import (
     CORSMiddleware
)
# habilita CORS (permite que o Svelte acesse o fastapi)
origins = [
    "http://localhost",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========================================================

# ATIVIDADE 1

@app.get("/filme/{title}")
async def find_movie(title: str):
    """ 
    procura filmes pelo titulo e ordena pelos mais populares 
    Exemplo: /filme/avatar
    """
    return {"title": title}

# ========================================================

# ATIVIDADE 2

@app.get("/artista/filmes")
async def find_filmes_artista(personId: int):
    """ 
    busca os filmes mais populares de um artista 
    Exemplo: /artista/filmes?personId=1100
    """
    return {"id": personId}

# ========================================================

@app.get("/filmes")
async def filmes_populares(limit=3):
    """ Obtem os filmes mais populares usando endpoint discover """
    data = get_json(
        "/discover/movie", "?sort_by=vote_count.desc"
    )
    results = data['results']
    filtro = []
    for movie in results:
        filtro.append({"title": movie['original_title'],
                       "image": f"https://image.tmdb.org/t/p/w185{movie['poster_path']}"})
    return filtro

@app.get("/artista/{id}")
async def get_artista(id: int):
    data = get_json("/person", f"/{id}?language=en-US")
    print(data)
    return data

@app.get("/artistas/{name}")
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
            "name": artist_id['name'],
            'rank': artist_id['popularity'],
            'biography': artist_id['biography'],
            "image": f"https://image.tmdb.org/t/p/w185{artist_id['profile_path']}"
        })
        print
        print(filtro)
        filtro.sort(reverse=True, key=lambda artist:artist['rank'])
        return filtro