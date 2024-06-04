<script>
	import axios from 'axios';
	import { onMount } from 'svelte';
	import { navigate } from 'svelte-routing';

	export let id;
	let task = {};

	async function fetchTask() {
		const token = localStorage.getItem('token');
		const response = await axios.get(`${import.meta.env.VITE_API_URL}/tasks/${id}`, {
			headers: {
				Authorization: `Bearer ${token}`
			}
		});
		task = response.data;
	}

	onMount(fetchTask);

	async function deleteTask() {
		const token = localStorage.getItem('token');
		await axios.delete(`${import.meta.env.VITE_API_URL}/tasks/${id}`, {
			headers: {
				Authorization: `Bearer ${token}`
			}
		});
		navigate('/tasks');
	}
</script>

<div class="container">
	<h1>{task.title}</h1>
	<p>{task.description}</p>
	<button on:click={deleteTask}>Delete</button>
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

    button {
        background-color: #a48fa9;
        color: #0b0b1d;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }

    button:hover {
        background-color: #855264;
    }
</style>
