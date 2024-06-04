<script>
	import { Router, Link, Route } from 'svelte-routing';
	import Login from './components/Auth/Login.svelte';
	import Register from './components/Auth/Register.svelte';
	import TaskList from './components/Tasks/TaskList.svelte';
	import TaskDetail from './components/Tasks/TaskDetail.svelte';
	import TaskForm from './components/Tasks/TaskForm.svelte';
	import CategoryList from './components/Categories/CategoryList.svelte';
	import CategoryDetail from './components/Categories/CategoryDetail.svelte';
	import CategoryForm from './components/Categories/CategoryForm.svelte';
</script>

<Router>
	<nav>
		<Link to="/login">Login</Link>
		<Link to="/register">Register</Link>
		<Link to="/tasks">Tasks</Link>
		<Link to="/categories">Categories</Link>
	</nav>
	<Route path="/login" component={Login} />
	<Route path="/register" component={Register} />
	<Route path="/tasks" component={TaskList} />
	<Route path="/tasks/:id" component={TaskDetail} />
	<Route path="/tasks/new" component={TaskForm} />
	<Route path="/categories" component={CategoryList} />
	<Route path="/categories/:id" component={CategoryDetail} />
	<Route path="/categories/new" component={CategoryForm} />
</Router>

<style>
    :root {
        font-family: Arial, sans-serif;
        margin: 20px;
        background-color: #0b0b1d;
        color: #d7c7e4;
    }

    nav {
        display: flex;
        justify-content: space-around;
        background-color: #241a36;
        padding: 10px;
        margin-bottom: 20px;
    }

    nav a {
        color: #d7c7e4;
        text-decoration: none;
        padding: 10px;
    }

    nav a:hover {
        background-color: #855264;
        border-radius: 5px;
    }
</style>
