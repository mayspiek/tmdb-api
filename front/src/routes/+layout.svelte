<div class="components-nav">
    <ul>
        <li><a href="/Movie">Movie</a></li>
        <li><a href="/Artist">Artist</a></li>
        <li><a href="/User">User</a></li>
        <li><a href="/UserList">User List</a></li>
    </ul>
</div>
<slot></slot>
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