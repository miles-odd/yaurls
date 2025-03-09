# Core application logic
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from .database import *
from .utils import *

# Start FastAPI and make sure the database exists
app = FastAPI()
init_db()

# Test stuff with root route
@app.get("/")
async def root():
    slug = generate_random_slug(6)
    insert_url(slug, "https://www.google.com")
    
    return redirect_url(slug)

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
@app.get("/{slug}/redirect")
def redirect_url(short_url: str):
    
    # Obtain just the slug if short_url contains the whole thing
    if short_url.startswith("yaurls.it/"):
        slug = short_url.removeprefix("yaurls.it/")
    else:
        slug = short_url
        
    url = get_url(slug)
    
    if url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    else:
        return RedirectResponse(url)