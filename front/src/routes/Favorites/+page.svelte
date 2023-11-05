<script>
    import "../../globals.css";
    let promise = getFavorites();
    async function getFavorites() {
        const res = await fetch(`http://localhost:8000/favorites/1`);
        const text = await res.json();
        if (res.ok) {
            return text;
        } else {
            throw new Error(text);
        }
    }

    function handleClick() {
        promise = getFavorites();
    }
</script>

<div class="content flexCenter">
    <button on:click={handleClick}> Get Favorites </button>
    <h1>Lista de Favoritos</h1>
    {#await promise}
        <p>...waiting</p>
    {:then favorites}
        {#each favorites as favorite}
            <div class="movies boxBorder flexCenter">
                <div class="moviesWrapper">
                    <button
                        on:click={() => {
                            {
                                fetch(
                                    `http://localhost:8000/favorites/1/${favorite.movie_id}`,
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
                                        handleClick();                                    })
                                    .catch((error) => {
                                        alert(error.message);
                                    });
                            }
                        }}>Delete</button
                    >
                    <p>
                        <span>ID: </span>
                        {favorite.movie_id}
                    </p>

                    <p>
                        <span>Title: </span>
                        {favorite.title}
                    </p>
                    <p>
                        <span>Sinopse: </span>
                        {favorite.sinopse}
                    </p>
                    <p>
                        <img
                            src="https://image.tmdb.org/t/p/w185{favorite.image}"
                            alt=""
                        />
                    </p>
                </div>
            </div>
        {/each}
    {:catch error}
        <p style="color: red">{error.message}</p>
    {/await}
</div>

<style>
    .movies {
        width: 50%;
    }

    .moviesWrapper {
        text-align: center;
    }
</style>
