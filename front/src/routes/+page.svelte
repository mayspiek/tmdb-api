<!-- <script>
    import Artista from "./Artist/+page.svelte";
	import Movie from "./Movie/+page.svelte";
	import Nav from "./+layout.svelte";
	import User from "./User/User.svelte";
    import UserList from "./User/+page.svelte";
	
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
 -->
