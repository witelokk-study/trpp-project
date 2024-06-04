<script>
	import axios from 'axios';
	import { onMount } from 'svelte';

	let categories = [];

	async function fetchCategories() {
		const token = localStorage.getItem('token');
		const response = await axios.get(`${import.meta.env.VITE_API_URL}/categories/`, {
			headers: {
				Authorization: `Bearer ${token}`
			}
		});
		categories = response.data;
	}

	onMount(fetchCategories);
</script>

<div class="container">
	<h1>Categories</h1>
	<ul class="category-list">
		{#each categories as category}
			<li>
				{category.name}
			</li>
		{/each}
	</ul>
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

    .category-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .category-list li {
        padding: 10px;
        border-bottom: 1px solid #855264;
    }

    .category-list li:last-child {
        border-bottom: none;
    }
</style>
