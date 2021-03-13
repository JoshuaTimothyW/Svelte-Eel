# svelte-eel

svelte + python eel = web gui dekstop

Note :
For past few days I tried another web gui dekstop module for called flaskwebgui. I combined it with svelte then compiled it to exe file and it worked at first sight, but later I noticed the exe still run in my task manager after I closed the gui program because flaskwebgui used flask as localhost, the local server can only be shutdown from CLI or end process in task manager. So I tried eel as an alternative, compile it with pyinstaller, it work as charm. The only cons here is there's no hot reload in python side, hopefully there's update in the future.

I removed svelte localhost command in rollup.config.js to avoid same port with python eel, this library used bottle as localhost.


## Development Instruction

Use virtual enviroment and install library
```
pip install -r requirement.txt

npm i
```

Run auto bundle in svelte
```
npm run dev
```

run python eel
```
python main.py
```

## Build Executable File
Generate standalone exe in dist folder
```
npm run deploy
```