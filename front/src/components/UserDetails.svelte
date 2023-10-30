<script>
    import "../globals.css";
    const user = {
        name,
        email,
        password,
    };
</script>

<div class="container">
    <form class="crud" action="sumbmit">
        <input
            value={user.name}
            type="text"
            name="name"
            placeholder="User name"
            required
            autocomplete="off"
        />
        <input
            value={user.email}
            type="text"
            name="email"
            placeholder="Email"
            required
            autocomplete="off"
        />
        <input
            value={user.password}
            type="password"
            name="password"
            placeholder="password"
            required
            autocomplete="off"
        />
    </form>
</div>
<button type="submit">Atualizar Usuário </button>
