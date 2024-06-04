import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig, loadEnv } from 'vite';


// Load environment variables based on the current mode
export default ({ mode }) => {
	const env = loadEnv(mode, process.cwd());

	return defineConfig({
		plugins: [sveltekit()],
		define: {
			'process.env.API_URL': JSON.stringify(env.API_URL)
		},
	});
};
