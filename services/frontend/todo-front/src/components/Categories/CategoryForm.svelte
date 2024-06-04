<script>
	import axios from 'axios';
	import { navigate } from 'svelte-routing';

	let name = '';
	let description = '';

	async function createCategory() {
		const token = localStorage.getItem('token');
		await axios.post(`http://localhost:8000/categories/`, {
			name,
			description
		}, {
			headers: {
				Authorization: `Bearer ${token}`
			}
		});
		navigate('/categories');
	}
</script>

<div class="container">
	<h1>New Category</h1>
	<form on:submit|preventDefault={createCategory}>
		<input type="text" bind:value={name} placeholder="Name" />
		<textarea bind:value={description} placeholder="Description"></textarea>
		<button type="submit">Create</button>
	</form>
</div>

<style>
    .container {
        max-width: 800px;
        margin: 40px auto;
        padding: 20px;
        background-color: #241a36;
        border: 1px solid #542c47;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    input[type='text'], textarea {
        width: 100%;
        padding: 10px;
        margin-bottom: 20px;
        border: 1px solid #855264;
        background-color: #241a36;
        color: #d7c7e4;
    }

    button[type='submit'] {
        background-color: #a48fa9;
        color: #0b0b1d;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }

    button[type='submit']:hover {
        background-color: #855264;
    }
</style>
