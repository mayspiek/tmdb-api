<script>
    export let menu
    export let appName
</script>
<div class="components-nav">
    <ul>
        <li><a href="/" on:click|preventDefault={() => (menu = 1)}>Movie</a></li>
        <li><a href="/" on:click|preventDefault={() => (menu = 2)}>Artist</a></li>
        <li><a href="/" on:click|preventDefault={() => (menu = 3)}>Movie</a></li>
    </ul>
</div>
<style>
    .components-nav li{
        margin: 1rem;
    }
    ul{
        color: navy;
        list-style-type: none;
    }
    li{
            display: inline;
    }
</style>