from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from agent.agent_loop import process_message
from agent.config import config
import os

app = FastAPI(title="AI Admin Agent")

@app.get("/", response_class=HTMLResponse)
async def chat_ui():
    return """
    <!DOCTYPE html>
    <html>
    <head><title>AI Admin Agent</title></head>
    <body>
        <h1>AI Admin Agent</h1>
        <div id="chat"></div>
        <input id="input" type="text" placeholder="Type command..." style="width:80%">
        <button onclick="send()">Send</button>
        <script>
            async function send() {
                const input = document.getElementById('input');
                const chat = document.getElementById('chat');
                const msg = input.value;
                chat.innerHTML += `<p><b>You:</b> ${msg}</p>`;
                const res = await fetch('/chat', {method:'POST', body: JSON.stringify({message: msg}), headers:{'Content-Type':'application/json'}});
                const data = await res.json();
                chat.innerHTML += `<p><b>Agent:</b> ${data.response}</p>`;
                input.value = '';
            }
        </script>
    </body>
    </html>
    """

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    response = await process_message(data["message"])
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=config.port)
