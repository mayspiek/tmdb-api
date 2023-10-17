<script>
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
    <button on:click={handleClick}> Get filmes </button>

    {#await promise}
        <p>...waiting</p>
    {:then users}
        <h1>Lista de Users</h1>
        {#each users as user}
            <div class="information flexCenter">
                <div>
                    <p>{user.id}</p>
                    <p>{user.name}</p>
                    <p>{user.email}</p>
                </div>

                <div>
                    <button on:click={()=>{{
                        fetch(`http://localhost:8000/users/${user.id}`, {
                            method: 'DELETE',
                        })
                        .then(response => response.json())
                        .then(data => {
                            console.log('Success:', data);
                            handleClick();
                        })
                        .catch((error) => {
                            console.error('Error:', error);
                        });
                    }}}> Delete </button>
                    
                    <button on:click={()=>{
                        fetch(`http://localhost:8000/users/${user.id}`, {
                            method: 'PUT',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({
                                name: "mayara  ",
                                email: "mayazinha",
                                password: "teste"
                            })
                        })
                        .then(response => response.json())
                        .then(data => {
                            console.log('Success:', data);
                            handleClick();
                        })
                        .catch((error) => {
                            console.error('Error:', error);
                        });
                    }}> Update </button>
                </div>
            </div>
        {/each}
    {:catch error}
        <p style="color: red">{error.message}</p>
    {/await}
</div>

<style>
    .flexCenter{
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .content {
        flex-direction: column;
    }

    .information{
        gap:.5rem;
        padding: 1rem;
        margin: .5rem;
        border: 1px solid black;
        border-radius: 10px;
        box-shadow: 5px 5px 3px 0px rgba(0,0,0,1);
    }
</style>
