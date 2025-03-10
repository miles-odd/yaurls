# Provides helper functions for main.py (mainly string functions)
import random
import string

# Generate a random string of the specified for the slug of the shortened URL
def generate_random_slug(length: int) -> str:
    valid_chars = string.ascii_letters + string.digits
    
    random_slug = ''
    random_slug = random_slug.join(random.choices(valid_chars, k=length))
    
    return random_slug

# Strip surrounding quotes from a string (if the string has them).
def strip_quotes(str: str) -> str:
    if str.startswith("\""):
        str = str[1:-1]
        
    return url

# Add https:// to the beginning of a stiring if it doesn't already have it.
def add_http(str: str) -> str:
    if not str.startswith("http"):
        str = "http://" + str
        
    return str