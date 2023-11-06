<script>
    let resposta = "";
    let mostrarFormulario = false;
    let mostrarUserList = true;
    let promise = getUsers();
    let usuarioParaAtualizar = null;

    async function sendForm(e) {
        // envia o formulario no formato json
        let formData = new FormData(e.target);
        let data = Object.fromEntries(formData.entries());
        if (usuarioParaAtualizar) {
            const userId = usuarioParaAtualizar.id;
            const res = await fetch(`http://localhost:8000/users/${userId}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
            });
            const json = await res.json();
            resposta = JSON.stringify(json);
            usuarioParaAtualizar = null;
        } else {
            const res = await fetch("http://localhost:8000/users", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
            });
            const json = await res.json();
            resposta = JSON.stringify(json);
            console.log(json);
            e.target.reset();
        }
    }

    async function getUsers() {
        // envia o formulario no formato json
        const res = await fetch("http://localhost:8000/users");
        const text = await res.json();
        if (res.ok) {
            return text;
        } else {
            throw new Error(text);
        }
    }

    function handleClick() {
        promise = getUsers();
        mostrarUserList = true;
        mostrarFormulario = false;
        usuarioParaAtualizar = null;
    }

    function toggleForm() {
        mostrarFormulario = true;
        mostrarUserList = false;
        usuarioParaAtualizar = null;
    }
    function updateUsuario(user) {
        usuarioParaAtualizar = user;
        mostrarFormulario = true;
        mostrarUserList = false;
    }
</script>

<div class="flexCenter">
    <button on:click={handleClick}> Mostrar Usuários </button>
    <button on:click={toggleForm}>Cadastrar Usuário</button>
</div>

{#if mostrarUserList}
    <div class="content flexCenter">
        {#await promise}
            <p>...waiting</p>
        {:then users}
            <h2>Lista de Users</h2>
            {#each users as user}
                <div class="information flexCenter boxBorder">
                    <div>
                        <p>
                            <span> ID: </span>
                            {user.id}
                        </p>

                        <p>
                            <span> Nome: </span>
                            {user.name}
                        </p>
                        <p>
                            <span>E-Mail: </span>
                            {user.email}
                        </p>
                    </div>

                    <div class="buttons">
                        <button
                            on:click={() => {
                                {
                                    fetch(
                                        `http://localhost:8000/users/${user.id}`,
                                        {
                                            method: "DELETE",
                                        }
                                    )
                                        .then((response) => response.json())
                                        .then((data) => {
                                            alert(
                                                `"${data.name}" Deletado com sucesso`,
                                                "success"
                                            );
                                            handleClick();
                                        })
                                        .catch((error) => {
                                            console.error("Error:", error);
                                        });
                                }
                            }}
                        >
                            Deletar
                        </button>

                        <!-- TO DO -->
                        <button
                            on:click={() => {
                                updateUsuario(user);
                            }}
                        >
                            Atualizar
                        </button>
                    </div>
                </div>
            {/each}
        {:catch error}
            <p style="color: red">{error.message}</p>
        {/await}
    </div>
{/if}
{#if mostrarFormulario}
    {#if usuarioParaAtualizar}
            <h2>Atualizar Usuário</h2>
            <p class="res">{resposta}</p>
        <div class="container">
            <form class="crud" on:submit|preventDefault={sendForm}>
                <input
                    type="text"
                    name="name"
                    placeholder="User name"
                    required
                    autocomplete="off"
                    bind:value={usuarioParaAtualizar.name}
                />
                <input
                    type="text"
                    name="email"
                    placeholder="Email"
                    required
                    autocomplete="off"
                    bind:value={usuarioParaAtualizar.email}
                />
                <input
                    type="text"
                    name="password"
                    placeholder="password"
                    required
                    autocomplete="off"
                    bind:value={usuarioParaAtualizar.password}
                />
                <button type="submit">Atualizar Usuário</button>
            </form>
        </div>
    {:else}
        <h2>Novo Usuário</h2>
        <p>{resposta}</p>
        <div class="content flexCenter">
            <form class="crud" on:submit|preventDefault={sendForm}>
                <input
                    type="text"
                    name="name"
                    placeholder="Nome do Usuário"
                    required
                    autocomplete="off"
                />
                <input
                    type="text"
                    name="email"
                    placeholder="exemplo@exemplo.com"
                    required
                    autocomplete="off"
                />
                <input
                    type="password"
                    name="password"
                    placeholder="Insira sua senha"
                    required
                    autocomplete="off"
                />
                <button type="submit">Adicionar Usuário</button>
            </form>
        </div>
    {/if}
{/if}

<style>
    form.crud {
        display: grid;
        grid-template-columns: 1fr;
        gap: 5px;
        row-gap: 10px;
        width: 60%;
    }
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .flexCenter {
        gap: 0.5rem;
        flex-direction: row;
        justify-content: center;
    }
    .content {
        flex-direction: column;
    }
    .information {
        justify-content: space-between;
        width: 30%;
    }
    span {
        font-weight: bold;
        text-decoration: underline;
    }

    .buttons {
        display: inherit;
        flex-direction: column;
        gap: 5px;
    }
    h2,.res{
        text-align: center;
    }
</style>
