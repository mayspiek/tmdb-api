<script>
    import Artista from "./Artista.svelte";
	import Movie from "./Movie.svelte";
	import Nav from "./Nav.svelte";
	import User from "./User.svelte";
    import UserList from "./UserList.svelte";
	
    let menu = 1; // Defina o valor inicial do menu

    function switchPage(page) {
        menu = page;
    }
</script>

<Nav bind:menu={menu} />

{#if menu === 1}
    <Movie />
{:else if menu === 2}
    <Artista />
{:else if menu === 3}
    <User />
{:else if menu === 4}
    <UserList />
{/if}

