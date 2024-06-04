<script>
	import axios from 'axios';
	import { navigate } from 'svelte-routing';

	let email = '';
	let password = '';

	async function register() {
		try {
			await axios.post("http://0.0.0.0:8000/auth/", { email, password });
			navigate('/login');
		} catch (error) {
			console.error('Registration failed', error);
		}
	}
</script>

<div class="container">
	<h1>Register</h1>
	<form on:submit|preventDefault={register}>
		<input type="email" bind:value={email} placeholder="Email" />
		<input type="password" bind:value={password} placeholder="Password" />
		<button type="submit">Register</button>
	</form>
	<div>
		<p>Already have an account? <a href="/login">Login</a></p>
	</div>
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
        width: 97%;
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
