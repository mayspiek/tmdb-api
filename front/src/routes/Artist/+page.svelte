<script>
    import { onMount } from "svelte";

    let promise = "";
    let nameArtist = "";
    
    async function getArtists(){
        const res = await fetch(`http://localhost:8000/artists`);
        const text = await res.json();
        if (res.ok) {
            return text;
        } else {
            throw new Error(text);
        }
    }

    async function searchArtist(name) {
        // faz um request GET para endpoint /filmes
        const res = await fetch(`http://localhost:8000/artists/${name}`);
        const text = await res.json();
        if (res.ok) {
            return text;
        } else {
            throw new Error(text);
        }
    }

    async function favoriteArtist(art_id){
        const verificaFavorito = await fetch(`http://localhost:8000/favorites/artists/1/${art_id}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        });
        if(verificaFavorito.ok){
            alert("Este artista já foi favoritado anteriormente.");
        } else {
            const res = await fetch(`http://localhost:8000/favorites/artists/1/${art_id}`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
            });
            if (res.ok) {
                alert("Artista favoritado com sucesso!");
            } else {
                alert("Falha ao favoritar o artista");
            }
        }
    }

    function search() {
        return (promise = searchArtist(nameArtist));
    }

    function handleClick() {
        return promise = getArtists();
    }

    onMount(() => {
        promise = getArtists();
    });
</script>


<div class="content flexCenter">
    <form action="">
        <input bind:value={nameArtist} type="text" />
        <button on:click={search}> Procurar </button>
        <button on:click={handleClick}>Todos Artistas</button>
    </form>

    {#await promise}
        <p>...waiting</p>
        {:then artistas}
    {#if promise = getArtists()}
        <h1>Artistas populares da Semana</h1>
    {:else}
        <h1>Artistas</h1>
    {/if}
        {#each artistas as artista}
        <div class="artist boxBorder flexCenter">
            <p>Nome: {artista.name}</p> <span>Rank: {artista.rank}</span>
            <p>Data de Nascimento: {artista.birthday}</p>
            <img
                src="https://image.tmdb.org/t/p/w185/{artista.profile_path}"
                alt=""
            />
            <p>{artista.biography}</p>
            <button on:click={favoriteArtist(artista.id)}>Favoritar</button>
        </div>
        {/each}
    {:catch error}
        <p style="color: red">{error.message}</p>
    {/await}
</div>

<style>
    .content, .artist {
        flex-direction: column;
    }
    .artist{
        width: 60%;
    }
</style>
