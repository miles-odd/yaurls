# Core application logic
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from .database import *
from .utils import *

class URLRequest(BaseModel):
    original_url: str
    
class Entry(BaseModel):
    slug: str
    url: str
    visits: int
    
# Start FastAPI and make sure the database exists
app = FastAPI()
init_db()

# Allow requests from frontend (localhost or file://)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Test stuff with root route
@app.get("/")
async def root():
    return FileResponse("frontend/index.html")

# Create new slug to map to the given URL
@app.post("/shorten")
def shorten_url(request: URLRequest) -> dict:
    slug = generate_random_slug(6)
    # Strip quotes from URL wrapped in JSON
    url = request.original_url[1:-1]
    insert_url(slug, request.original_url)
    
    # Expected return of the form {"shortened_url": "yaurls.it/abc123"}
    short_url = "yaurls.it/" + slug
    return {"shortened_url": short_url}

# Return the URL mapped to by the given slug
@app.get("/{slug}")
def expand_url(slug: str) -> str:
    url = get_url(slug)
    
    if url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    else:
        return url
    
# Redirect to the URL mapped to by the given slug
@app.get("/redirect/{slug}")
def redirect_url(slug: str) -> RedirectResponse:
    url = get_url(slug)
    
    if not url.startswith("http"):
        url = "https://" + url

    if url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return RedirectResponse(url=url, status_code=307)