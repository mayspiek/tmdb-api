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
    async function favoritarFilme(tmdb_id) {
        try {
            // verifica se o filme já está favoritado
            const verificarFavoritoRes = await fetch(`http://localhost:8000/favorites/1/${tmdb_id}`, {
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
                const res = await fetch(`http://localhost:8000/favorites/1/${tmdb_id}`, {
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

</script>
<div class="title flexCenter">
    <button on:click={getFilmes}> Get filmes </button>
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
    button{ 
        margin: .3rem auto;
        display: block;
    }

</style>
