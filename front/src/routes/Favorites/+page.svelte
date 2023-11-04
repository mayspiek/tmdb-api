<script>
    let promise = getFavorites();
    async function getFavorites(){
        const res = await fetch(`http://localhost:8000/favorites/1`);
        const text = await res.json();
        if(res.ok){
            return text;
        }else{
            throw new Error(text);
        }
    }

    function handleClick(){
        promise = getFavorites();
    }
</script>
<div class="content FlexCenter">
    <button on:click={handleClick}> Get Favorites </button>
    {#await promise}
        <p>...waiting</p>
    {:then favorites}
        <h1>Lista de Favoritos</h1>
    {#each favorites as favorite}
        <div>
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
                <img src="https://image.tmdb.org/t/p/w185{favorite.image}" alt="">
            </p>
        </div>
    {/each}
    {:catch error}
    <p style="color: red">{error.message}</p>
    {/await}
</div>
