<script>
    import "../../globals.css";

    let promise = getFavoriteMovies();
    let promise2 = getFavoriteArtists();
    async function getFavoriteMovies() {
        const res = await fetch(`http://18.212.220.116:8000/favorites/movies/1`);
        const text = await res.json();
        if (res.ok) {
            return text;
        } else {
            throw new Error(text);
        }
    }

    async function getFavoriteArtists() {
        const res = await fetch(`http://18.212.220.116:8000/favorites/artists/1`);
        const text = await res.json();
        if (res.ok) {
            return text;
        } else {
            throw new Error(text);
        }
    }

    function handleClick() {
        promise = getFavoriteMovies();
        promise2 = getFavoriteArtists();
    }
</script>

<button on:click={handleClick}> Get Favorites </button>
<h1>Lista de Favoritos</h1>
<div class="content flexCenter">
    {#await promise}
        <p>...waiting</p>
    {:then movies}
        <div class="">
            {#each movies as movie}
                <div class="movies boxBorder">
                    <p>
                        <span>ID: </span>
                        {movie.tmdb_id}
                    </p>

                    <p>
                        <span>Title: </span>
                        {movie.title}
                    </p>
                    <p>
                        <span>Sinopse: </span>
                        {movie.sinopse}
                    </p>
                    <p>
                        <img
                        src="https://image.tmdb.org/t/p/w185{movie.image}"
                        alt=""
                        />
                    </p>
                    <button
                        on:click={() => {
                            {
                                fetch(
                                    `http://18.212.220.116:8000/favorites/movies/1/${movie.tmdb_id}`,
                                    {
                                        method: "DELETE",
                                    }
                                )
                                    .then((response) => response.json())
                                    .then((data) => {
                                        console.log(data);
                                        alert(
                                            `"${data.tmdb_id}" Deletado com sucesso`
                                        );
                                        handleClick();
                                    })
                                    .catch((error) => {
                                        alert(error.message);
                                    });
                            }
                        }}>Delete</button
                    >
                </div>
            {/each}
        </div>
    {:catch error}
        <p style="color: red">{error.message}</p>
    {/await}

    {#await promise2}
        <p>waiting...</p>
    {:then artists} 
        <div class="">
            {#each artists as artist}
                <div class="artists boxBorder">
                    <p> <span>Nome: </span>
                        {artist.name}
                    </p>
                    <p> <span>Rank: </span>
                        {artist.rank}
                    </p>
                    <p> <span>Data de Nascimento: </span>
                        {artist.birthday}
                    </p>
                    <img src="https://image.tmdb.org/t/p/w185{artist.image}" alt="" srcset="">
                    <p> <span>Biografia: </span>
                        {artist.biography}
                    </p>

                    <button on:click={()=>{
                        {
                            fetch(`http://18.212.220.116:8000/favorites/artists/1/${artist.artist_id}`, {
                                method: "DELETE",
                            })
                                .then((response) => response.json())
                                .then((data) => {
                                    console.log(data);
                                    alert(`"${data.tmdb_artist_id}" Deletado com sucesso`);
                                    handleClick();
                                })
                                .catch((error) => {
                                    alert(error.message);
                                });
                        }
                    }}>Deletar</button>
                </div>
            {/each}
        </div>
    {:catch error}
        <p style="color: red">{error.message}</p>
    {/await}

</div>

<style>
    .movies {
        text-align: center;
    }
    .content {
        flex-wrap: wrap;
        align-items: center;
        display: inherit;
        flex-direction: row;
        width: 80%;
    }
    span{
        font-weight: bold;
    }


</style>
