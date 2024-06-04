<script>
	import axios from 'axios';
	import { onMount } from 'svelte';
	import TaskList from './Tasks/TaskList.svelte';
	import { goto } from '$app/navigation';

	export let activeCategoryId = 'all';

	const handleClick = (tabValue) => () => (activeCategoryId = tabValue);

	let categories = [];

	async function fetchCategories() {
		const token = localStorage.getItem('token');
		const response = await axios.get(`http://localhost:8000/categories/`, {
			headers: {
				Authorization: `Bearer ${token}`
			}
		});
		categories = response.data;
	}

	async function createCategory(name) {
		const token = localStorage.getItem('token');
		const response = await axios.post(
			`http://localhost:8000/categories/`,
			{ name },
			{
				headers: {
					Authorization: `Bearer ${token}`
				}
			}
		);
		categories = response.data;
	}

	async function onCreateDialogClicked() {
		let categoryName = prompt('Category name');
		if (!(categoryName == null || categoryName == '')) {
			await createCategory(categoryName);
            fetchCategories();
		}
	}

	onMount(() => {
		if (typeof localStorage.token === 'undefined') {
			goto('/tasks');
		} else {
			fetchCategories();
		}
	});
</script>

<div class="container">
	<h1>Tasks</h1>

	<ul>
		<li class={activeCategoryId === 'all' ? 'active' : ''}>
			<span on:click={handleClick('all')}>All</span>
		</li>
		{#each categories as category}
			<li class={activeCategoryId === category.id ? 'active' : ''}>
				<span on:click={handleClick(category.id)}>{category.name}</span>
			</li>
		{/each}
		<li><span id="add_category" on:click={onCreateDialogClicked}>+</span></li>
	</ul>
	{#if activeCategoryId === 'all'}
		<div class="box">
			<TaskList />
		</div>
	{/if}
	{#each categories as category}
		{#if activeCategoryId == category.id}
			<div class="box">
				<TaskList categoryId={category.id} />
			</div>
		{/if}
	{/each}
</div>

<style>
	h1 {
		margin: 0;
		padding: 0;
	}
	.container {
		max-width: 800px;
		margin: 40px auto;
		padding: 40px;
		background-color: #241a36;
		border: 1px solid #542c47;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
	}

	.box {
		margin-bottom: 10px;
		/* padding: 40px; */
		/* border: 1px solid #dee2e6; */
		border-radius: 0 0 0.5rem 0.5rem;
		border-top: 0;
	}
	ul {
		display: flex;
		flex-wrap: wrap;
		padding-left: 0;
		margin-bottom: 0;
		list-style: none;
		border-bottom: 1px solid #855264;
	}
	li {
		margin-bottom: -1px;
	}

	span {
		border: 1px solid transparent;
		border-top-left-radius: 0.25rem;
		border-top-right-radius: 0.25rem;
		display: block;
		padding: 0.5rem 1rem;
		cursor: pointer;
	}

	span#add_category:hover {
		border-color: none !important;
	}

	span:hover {
		border-color: #e9ecef #e9ecef #dee2e6;
	}

	li.active > span {
		color: #495057;
		background-color: #855264;
		color: white;
		border-color: #855264 #855264 #855264;
	}
</style>
