<script>
import "../../globals.css";
    let promise = getUsers();

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
    }


</script>

<div class="content flexCenter">
    <button on:click={handleClick}> Get Users </button>

    {#await promise}
        <p>...waiting</p>
    {:then users}
        <h1>Lista de Users</h1>
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

                <div>
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
                        Delete
                    </button>
                    
                    <!-- TO DO -->
                    <button> Update </button>
                </div>
            </div>
        {/each}
    {:catch error}
        <p style="color: red">{error.message}</p>
    {/await}
</div>

<style>
    .content {
        flex-wrap: wrap;
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
</style>
