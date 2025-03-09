# Core application logic
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from .database import *
from .utils import *

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
    return {"message": "Hello World"}

# Create new slug to map to the given URL
@app.post("/shorten")
def shorten_url(url: str):
    slug = generate_random_slug(6)
    insert_url(slug, url)
    
    short_url = "yaurls.it/" + slug
    return {"shortened_url": short_url}

# Return the URL mapped to by the given slug
@app.get("/{slug}")
def expand_url(short_url: str):
    
    # Obtain just the slug if short_url contains the whole thing
    if short_url.startswith("yaurls.it/"):
        slug = short_url.removeprefix("yaurls.it/")
    else:
        slug = short_url
        
    url = get_url(slug)
    
    if url is None:
        return {"error": "URL not found"}
    else:
        return {"retrieved": url}
    
# Redirect to the URL mapped to by the given slug
@app.get("/redirect")
def redirect_url(short_url: str):
        
    # Obtain just the slug if short_url contains the whole thing
    if short_url.startswith("yaurls.it/"):
        slug = short_url.removeprefix("yaurls.it/")
    else:
        slug = short_url
        
    url = get_url(slug)
    print(f"Retrieved URL: {url}")
    
    return RedirectResponse(url=url, status_code=307)