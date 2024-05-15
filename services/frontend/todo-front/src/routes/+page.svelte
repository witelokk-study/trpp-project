<script>
	let token = '';
	let tasks = [];
	let categories = [];
	let newTask = '';
	let newCategory = '';
	let selectedCategory = '';

	async function getToken() {
		const response = await fetch('/auth/token', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ username: 'user', password: 'pass' })
		});
		token = await response.json();
	}

	async function getTasks() {
		const response = await fetch('/tasks/', {
			method: 'GET',
			headers: { Authorization: `Bearer ${token}` }
		});
		tasks = await response.json();
	}

	async function addTask() {
		const response = await fetch('/tasks/', {
			method: 'POST',
			headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
			body: JSON.stringify({ title: newTask, category: selectedCategory })
		});
		newTask = '';
		await getTasks();
	}

	async function deleteTask(taskId) {
		const response = await fetch(`/tasks/${taskId}`, {
			method: 'DELETE',
			headers: { Authorization: `Bearer ${token}` }
		});
		await getTasks();
	}

	async function getCategories() {
		const response = await fetch('/categories', {
			method: 'GET',
			headers: { Authorization: `Bearer ${token}` }
		});
		categories = await response.json();
	}

	async function addCategory() {
		const response = await fetch('/categories', {
			method: 'POST',
			headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
			body: JSON.stringify({ title: newCategory })
		});
		newCategory = '';
		await getCategories();
	}

	async function selectCategory(categoryId) {
		selectedCategory = categoryId;
		await getTasks();
	}

	getToken();
	getCategories();
</script>

<div class="container">
	<h1>To-Do List</h1>
	<form on:submit|preventDefault={addTask}>
		<input type="text" bind:value={newTask} placeholder="New Task" />
		<button type="submit">Add Task</button>
	</form>

	<h2>Categories</h2>
	<ul class="category-list">
		{#each categories as category}
			<li>
				<span>{category.title}</span>
				<button on:click={() => selectCategory(category.id)}>Select</button>
			</li>
		{/each}
	</ul>

	<form on:submit|preventDefault={addCategory}>
		<input type="text" bind:value={newCategory} placeholder="New Category" />
		<button type="submit">Add Category</button>
	</form>

	<h2>Tasks</h2>
	<ul class="task-list">
		{#each tasks as task}
			<li>
				<span>{task.title}</span>
				<button on:click={() => deleteTask(task.id)}>Delete</button>
			</li>
		{/each}
	</ul>
</div>

<style>
	body {
		font-family: Arial, sans-serif;
		margin: 20px;
		background-color: #0b0b1d; /* Dark blue background for the body */
		color: #d7c7e4; /* Light purple for text */
	}

	.container {
		max-width: 800px;
		margin: 40px auto;
		padding: 20px;
		background-color: #241a36; /* Dark purple for the container background */
		border: 1px solid #542c47; /* Darker purple border */
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
	}

	.task-list {
		list-style: none;
		padding: 0;
		margin: 0;
	}

	.task-list li {
		padding: 10px;
		border-bottom: 1px solid #855264; /* Soft brown for list item borders */
	}

	.task-list li:last-child {
		border-bottom: none;
	}

	.task-list li button {
		float: right;
		margin-top: 5px;
		background-color: #855264; /* Match button color to list border */
		color: #d7c7e4; /* Light purple text on button */
	}

	.category-list {
		list-style: none;
		padding: 0;
		margin: 0;
	}

	.category-list li {
		padding: 10px;
		border-bottom: 1px solid #855264; /* Consistent with task-list styling */
	}

	.category-list li:last-child {
		border-bottom: none;
	}

	.category-list li button {
		float: right;
		margin-top: 5px;
		background-color: #855264; /* Soft brown for buttons */
		color: #d7c7e4; /* Light purple text */
	}

	input[type='text'] {
		width: 100%;
		padding: 10px;
		margin-bottom: 20px;
		border: 1px solid #855264; /* Input border using the soft brown */
		background-color: #241a36; /* Dark purple background */
		color: #d7c7e4; /* Light purple text color for contrast */
	}

	button[type='submit'] {
		background-color: #a48fa9; /* Muted purple for submit button */
		color: #0b0b1d; /* Dark blue text */
		padding: 10px 20px;
		border: none;
		border-radius: 5px;
		cursor: pointer;
	}

	button[type='submit']:hover {
		background-color: #855264; /* Darker purple on hover */
	}
</style>
