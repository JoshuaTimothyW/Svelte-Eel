<script>
	export let name;
	// eel.set_host("ws://localhost:8000");

	async function call_python() {
		let msg = await eel.hello_world()();
		alert(msg);
	}

	async function send_to_python() {
		let msg = "call from js";
		let res = await eel.print_string(msg)();
		alert(res);
	}

</script>

<main>
	<h1>Hello {name}!</h1>
	<button on:click={call_python}>send hello to python</button>
	<button on:click={send_to_python}>send message to python</button>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>