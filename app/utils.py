# Provides helper functions for main.py
import random
import string

# Generate a random string of the specified for the slug of the shortened URL
def generate_random_slug(length: int) -> str:
    valid_chars = string.ascii_letters + string.digits
    
    random_slug = ''
    random_slug = random_slug.join(random.choices(valid_chars, k=length))
    
    return random_slug