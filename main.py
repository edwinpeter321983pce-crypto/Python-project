import httpx
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import requests

app = FastAPI(title="PraiseAI Web Backend")

# Setup HTML template directory
templates = Jinja2Templates(directory="templates")

# Configure your AI Model API details here 
# (You can swap this with OpenAI, Anthropic, or a free open-source provider API later)
AI_API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = os.getenv("AI_API_KEY")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serves the main PraiseAI website landing and chat page."""
    return templates.TemplateResponse(request, "index.html")

@app.post("/api/chat")
async def chat_with_ai(payload: dict):
    user_message = payload.get("message") or payload.get("prompt", "")
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": user_message}]
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(AI_API_URL, json=data, headers=headers)
        result = response.json()
        
        if "choices" in result:
            ai_reply = result["choices"][0]["message"]["content"]
        else:
            ai_reply = f"API Error: {result}"
            
    return {"reply": ai_reply}
import os

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port)