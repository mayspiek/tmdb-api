<script> 
    import '../globals.css'
    let resposta = "";
    async function sendForm(e) {
        // envia o formulario no formato json
        let formData = new FormData(e.target);
        let data = Object.fromEntries(formData.entries());
        const res = await fetch("http://localhost:8000/users", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });
        const json = await res.json();
        resposta = JSON.stringify(json);
        e.target.reset();
    }
</script>

<div class="container">
    <h2>New user</h2>

    <p>{resposta}</p>

    <form class="crud" on:submit|preventDefault={sendForm}>
        <input
            type="text"
            name="name"
            placeholder="User name"
            required
            autocomplete="off"
        />
        <input
            type="text"
            name="email"
            placeholder="Email"
            required
            autocomplete="off"
        />
        <input
            type="password"
            name="password"
            placeholder="password"
            required
            autocomplete="off"
        />
        <button type="submit">Adicionar Usuário </button>
    </form>
</div>

<style>
    form.crud {
        display: grid;
        grid-template-columns: 1fr;
        gap: 5px;
        row-gap: 10px;
        width: 60%;
    }
    .container{
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>
