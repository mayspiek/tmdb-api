<script>
    let promise = getFilmes();
    async function getFilmes() {
        // faz um request GET para endpoint /filmes
        const res = await fetch(`http://localhost:8000/filmes`);
        const text = await res.json();
        if (res.ok) {
            return text;
        } else {
            throw new Error(text);
        }
    }
    export function handleClick() {
        promise = getFilmes();
    }

    async function favoritarFilme(tmdb_id) {
        try {
            const res = await fetch(`http://localhost:8000/favorites/${tmdb_id}`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
            });
            if (res.ok) {
                alert("Filme favoritado com sucesso!");
            } else {
                alert("Falha ao favoritar o filme");
            }
        } catch (error) {
            console.error(error);
            alert("Ocorreu um erro ao favoritar o filme.");
        }
    }

</script>
<div class="title flexCenter">
    <button on:click={handleClick}> Get filmes </button>
    <h1>Lista de Filmes</h1>
</div>
{#await promise}
    <p>...waiting</p>
{:then filmes}
    <div class="content flexCenter">
        {#each filmes as filme}
            <div class="movies boxBorder">
                <p>{filme.tmdb_id}</p>
                <p>{filme.title}</p>
                <img src={filme.image} alt="cover" />
                <!-- FAVORITAR FILME -->
                <button on:click={() => favoritarFilme(filme.tmdb_id)}>Favoritar</button>

            </div>
        {/each}
    </div>
{:catch error}
    <p style="color: red">{error.message}</p>
{/await}

<style>
    .content {
        flex-wrap: wrap;
    }

    .movies{
        text-align: center;
    }
    .title{
        flex-direction: column;
    }
    button{ 
        margin: .3rem auto;
        display: block;
    }

</style>
