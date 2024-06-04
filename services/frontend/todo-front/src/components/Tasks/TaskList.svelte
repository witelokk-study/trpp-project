<script>
	import axios from 'axios';
	import { onMount } from 'svelte';

	let tasks = [];

	async function fetchTasks() {
		const token = localStorage.getItem('token');
		const response = await axios.get(`${import.meta.env.VITE_API_URL}/tasks/`, {
			headers: {
				Authorization: `Bearer ${token}`
			}
		});
		tasks = response.data;
	}

  onMount(fetchTasks);

  async function deleteTask(id) {
    const token = localStorage.getItem('token');
    await axios.delete(`${import.meta.env.VITE_API_URL}/tasks/${id}`, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });
    fetchTasks();
  }
</script>

<div class="container">
	<h1>Tasks</h1>
	<ul class="task-list">
		{#each tasks as task}
			<li>
				{task.title}
				<button on:click={() => deleteTask(task.id)}>Delete</button>
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

    .task-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .task-list li {
        padding: 10px;
        border-bottom: 1px solid #855264;
    }

    .task-list li:last-child {
        border-bottom: none;
    }

    .task-list li button {
        float: right;
        margin-top: 5px;
        background-color: #855264;
        color: #d7c7e4;
    }
</style>
