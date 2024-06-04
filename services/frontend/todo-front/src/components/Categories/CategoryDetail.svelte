<script>
	import axios from 'axios';
	import { onMount } from 'svelte';

	export let id;
	let category = {};

	async function fetchCategory() {
		const token = localStorage.getItem('token');
		const response = await axios.get(`${import.meta.env.VITE_API_URL}/categories/${id}`, {
			headers: {
				Authorization: `Bearer ${token}`
			}
		});
		category = response.data;
	}

	onMount(fetchCategory);
</script>

<div class="container">
	<h1>{category.name}</h1>
	<p>{category.description}</p>
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
</style>
