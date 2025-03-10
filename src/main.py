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

# Root route -> serve index.html
@app.get("/")
async def root():
    return FileResponse("frontend/index.html")

# Shorten -> take given URL and map to new slug
@app.post("/shorten")
def shorten_url(request: URLRequest) -> dict:
    slug = generate_random_slug(6)
    
    url = request.original_url # Note: might have quotes around it from being wrapped in json
    url = strip_quotes(url)
        
    insert_url(slug, url)
    
    short_url = "yaurls.it/" + slug
    return {"shortened_url": short_url}

# Return the URL mapped to by the given slug
@app.get("/expand/{slug}")
def expand_url(slug: str) -> str:
    url = get_url(slug)
    
    if url is None:
        # not a real slug; doesn't exist in database
        raise HTTPException(status_code=404, detail="URL not found")

    return url
    
# Redirect to the URL mapped to by the given slug
@app.get("/redirect/{slug}")
def redirect_url(slug: str) -> RedirectResponse:
    url = get_url(slug)
    url = add_http(url)

    if url is None:
        # not a real slug; doesn't exist in database
        raise HTTPException(status_code=404, detail="URL not found")

    return RedirectResponse(url=url, status_code=307)