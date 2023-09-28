<script>
    import { get } from "svelte/store";

    let promise = getArtista();
        async function getArtista() {

            // faz um request GET para endpoint /filmes
            const res = await fetch("http://localhost:8000/artistas/leonardo");
            const text = await res.json();
            if (res.ok) {
                return text;
            } else {
                throw new Error(text);
            }
        }
        function handleClick() {
            promise = getArtista();
            alert("clicou no get artitst")
        }
        </script>

<div class="content">
    <input type="text" id="artista_nome"><button onClick=handleClick()> Get Artistas </button>

    {#await promise}
        <p>...waiting</p>
    {:then artista}
        <h1>Lista de Artistas</h1>
            <p>{artista.name}</p>
            <img src="
            https://image.tmdb.org/t/p/w185{artista.profile_path}" alt="">
            <p>{artista.biography}</p>
            
    {:catch error}
        <p style="color: red">{error.message}</p>
    {/await}
</div>

<style>
    .content{
        display: flex;
        align-items: center;
        flex-direction: column;
    }
</style>
