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
        const res = await fetch(`http://localhost:8000/artistas/${name}`);
        const text = await res.json();
        if (res.ok) {
            return text;
        } else {
            throw new Error(text);
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
        <h1>Lista de Artistas</h1>
        {#each artistas as artista}
        <div class="artist boxBorder flexCenter">
            <p>{artista.id}</p>
            <p>{artista.name}</p>
            <img
                src="https://image.tmdb.org/t/p/w185/{artista.profile_path}"
                alt=""
            />
            <p>{artista.biography}</p>
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
