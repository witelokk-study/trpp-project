<script>
	import axios from 'axios';
	import { onMount } from 'svelte';
	import deleteSvg from '$lib/images/delete.svg';

	export let categoryId;
	let tasks = [];

	async function fetchTasks() {
		const token = localStorage.getItem('token');
		let url;
		if (typeof categoryId !== 'undefined')
			url = `http://localhost:8000/tasks/category/${categoryId}`;
		else url = `http://localhost:8000/tasks/`;
		const response = await axios.get(url, {
			headers: {
				Authorization: `Bearer ${token}`
			}
		});
		tasks = response.data;
	}

	onMount(fetchTasks);

	async function editTaskDone(id, done) {
		const token = localStorage.getItem('token');
		await axios.patch(
			`http://localhost:8000/tasks/${id}`,
			{ done },
			{
				headers: {
					Authorization: `Bearer ${token}`
				}
			}
		);
		fetchTasks();
	}

	async function editTaskText(id, text) {
		const token = localStorage.getItem('token');
		await axios.patch(
			`http://localhost:8000/tasks/${id}`,
			{ text },
			{
				headers: {
					Authorization: `Bearer ${token}`
				}
			}
		);
		fetchTasks();
	}

	async function createTask(text) {
		const token = localStorage.getItem('token');
		await axios.post(
			`http://localhost:8000/tasks`,
			{ text, done: false, category_id: categoryId },
			{
				headers: {
					Authorization: `Bearer ${token}`
				}
			}
		);
		fetchTasks();
	}

	async function deleteTask(id) {
		const token = localStorage.getItem('token');
		await axios.delete(`http://localhost:8000/tasks/${id}`, {
			headers: {
				Authorization: `Bearer ${token}`
			}
		});
		fetchTasks();
	}

	function handleTaskNameInputKeydown(event, taskId) {
		if (event.key === 'Enter') {
			editTaskText(taskId, event.target.value);
			event.target.value = '';
      event.target.blur();
		}
	}

	function handleAddTaskInputKeydown(event) {
		if (event.key === 'Enter') {
			createTask(event.target.value);
			event.target.value = '';
		}
	}
</script>

<div class="container">
	<ul class="task-list">
		{#each tasks as task}
			<li>
				<input
					type="checkbox"
					checked={task.done}
					on:change={(e) => editTaskDone(task.id, e.target.checked)}
				/>
				<input
					type="text"
					value={task.text}
					on:keydown={(e) => handleTaskNameInputKeydown(e, task.id)}
				/>
				<button class="delete" on:click={() => deleteTask(task.id)}
					><img src={deleteSvg} alt="Delete" /></button
				>
			</li>
		{/each}
		<li id="add_task">
			<input type="text" placeholder="Add task" on:keydown={handleAddTaskInputKeydown} />
		</li>
	</ul>
</div>

<style>
	input[type='checkbox'] {
		transform: scale(1.5);
		accent-color: #855264;
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
		/* margin-top: 5px; */
		background-color: transparent;
		color: #d7c7e4;
    border: 0;
	}

  .task-list li button:hover {
    /* filter: invert(42%) sepia(93%) saturate(1352%) hue-rotate(8deg) brightness(119%) contrast(119%); */
    filter: brightness(200%);
    cursor: pointer;
  }

	li#add_task {
		padding-left: 35px;
		color: #77717b;
	}

  input {
    background: transparent;
    color: white;
    border: 0;
  }

	/* button {
		border: 0;
		background: transparent;
	} */
</style>
