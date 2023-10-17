<script>
    export let menu
</script>
<div class="components-nav">
    <ul>
        <li><a href="/" on:click|preventDefault={() => (menu = 1)}>Movie</a></li>
        <li><a href="/" on:click|preventDefault={() => (menu = 2)}>Artist</a></li>
        <li><a href="/" on:click|preventDefault={() => (menu = 3)}>User</a></li>
        <li><a href="/" on:click|preventDefault={() => (menu = 4)}>User List</a></li>
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