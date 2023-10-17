<script>
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
            type="text"
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
    form.crud input {
        padding: 0.5rem;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    .crud button {
        padding: 0.5rem;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: #ccc;
        cursor: pointer;
    }
    .container{
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>
