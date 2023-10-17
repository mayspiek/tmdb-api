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
                <p>{filme.title}</p>
                <img src={filme.image} alt="cover" />
                <button>Favoritar</button>
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
