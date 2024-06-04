<script>
	import axios from 'axios';
	import { navigate } from 'svelte-routing';

	let email = '';
	let password = '';

	async function login() {
		try {
			const response = await axios.post(`${import.meta.env.VITE_API_URL}/auth/token`, {
				email,
				password
			});
			localStorage.setItem('token', response.data.access_token);
			navigate('/tasks');
		} catch (error) {
			console.error('Login failed', error);
		}
	}
</script>

<div class="container">
	<h1>Login</h1>
	<form on:submit|preventDefault={login}>
		<input type="email" bind:value={email} placeholder="Email" />
		<input type="password" bind:value={password} placeholder="Password" />
		<button type="submit">Login</button>
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

    input[type='email'], input[type='password'] {
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
