<script>
	let menu = 2
	let appName = "Front"
	import Artista from "./Artista.svelte";
	import Movie from "./Movie.svelte";
	import Nav from "./Nav.svelte";
</script>

<Nav bind:menu/>
{#if menu === 1}
		<Movie/>
{:else if menu === 2}
		<Artista/>
{:else if menu === 3}
		<Artista/>
{/if}
