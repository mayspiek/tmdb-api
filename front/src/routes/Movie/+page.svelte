<script>
    let promise = getFilmes();
    let nomeFilme = "";
    async function getFilmes() {
        // faz um request GET para endpoint /filmes
        const res = await fetch(`http://localhost:8000/movies`);
        const text = await res.json();
        if (res.ok) {
            return text;
        } else {
            throw new Error(text);
        }
    }
    async function favoritarFilme(tmdb_id) {
        try {
            // verifica se o filme já está favoritado
            const verificarFavoritoRes = await fetch(`http://localhost:8000/favorites/movies/1/${tmdb_id}`, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                },
            });
            if (verificarFavoritoRes.ok) {
                // Se a verificação for bem-sucedida, o filme já está favoritado
                alert("Este filme já foi favoritado anteriormente.");
            } else{
                // se nao, ele faz o post para favoritar
                const res = await fetch(`http://localhost:8000/favorites/movies/1/${tmdb_id}`, {
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
            }
        } catch (error) {
            alert("Ocorreu um erro ao favoritar o filme.");
            console.error(error);
            
        }
    }

    async function searchFilme(nomeFilme) {
        const res = await fetch(`http://localhost:8000/movies/${nomeFilme}`);
        const text = await res.json();
        if (res.ok) {
            return text;
        } else {
            throw new Error(text);
        }
    }

    function search() {
        return (promise = searchFilme(nomeFilme));
    }

</script>
<div class="title flexCenter">
    <form action="">
        <input bind:value={nomeFilme} type="text" />
        <button on:click={search}> Procurar </button>
        <button on:click={getFilmes}> Get filmes </button>
    </form>
</div>
<h1>Lista de Filmes</h1>
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
    button{ 
        margin: .3rem auto;
        display: block;
    }

</style>
