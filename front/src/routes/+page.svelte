<script>
	let menu;
    import Artista from "./Artista.svelte";
	import Movie from "./Movie.svelte";
	import Nav from "./Nav.svelte";
	import User from "./User.svelte";
</script>

<Nav bind:menu/>
{#if menu === 1}
		<Movie/>
{:else if menu === 2}
		<Artista/>
{:else if menu === 3}
		<User/>
{/if}
