from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static/css", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "message": "Hello From Victor Spicter"}
    )

@app.get("/about", response_class=HTMLResponse)
async def get_about(request: Request):
    return templates.TemplateResponse(
        "about.html",
        {"request": request, "focus_area": "Backend architecture and automation",
        "tech_stack": ["Python", "FastAPI", "SQLModel", "HTMX", "Tailwind"]}
    )
