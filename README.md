# yaurls

<h3 align=center>
  yet another URL shortener
</h3>

<p align=center>
  ...because the world really needed another one of these.
</p>

## What is it?

**y**et **a**nother **URL s**hortener (**yaURLs**... get it?) is exactly what it says on the tin. Give it a long, (preferably) unwieldy URL, and it'll spit out a much shorter and cleaner-looking URL that you can share elsewhere to your heart's content. 

There may be additional features added in the future, but yeah, it's a URL shortener. It shortens URLs. That's the whole deal.

## What can it do?

Currently, yaurls supports such novel and unique features as:

- shortening a URL
- Redirecting you to the original URL using the shortened URL.

At least some additional features _are_ planned, such as:

- creating custom slugs (i.e. `yaurls.it/customslug`)
- creating click-limited/self-destructing links
- tracking statistics, such as number of (unique) clicks, location and device information, etc.

and possibly even more things, if I come up with more things and feel like adding them.

## How do I use it?

It's still early in development, so for now, the only option is locally hosting it. In order to run it:

0. Open up the terminal.
1. Clone this repository (`https://github.com/miles-odd/yaurls.git`).
2. Install the required packages (`pip install -r requirements.txt`).
3. Start a local instance of the app (`fastapi dev app/main.py`).
4. You should see FastAPI spit out a bunch of stuff in the terminal. Look for something like `Server started at http://<ip address>:<port>` and navigate to that URL in your browser.
5. Now you can play around with yaurls! Try entering a long URL in the top textbox, and then enter the resulting shortened URL in the bottom textbox. yaurls is sure to provide seconds of entertainment!*
   
<sup><sub>*note: no refunds if you didn't experience at least seconds of entertainment. I don't know how to refund your wasted time.</sub></sup>

In the future, I'll keep it up and running somewhere, and you'll be able to simply visit [whatever the website will be](https://www.youtube.com/watch?v=dQw4w9WgXcQ) to try it out!

## Why am I making this?

As you may have figured out by now, this README hasn't been taking itself too seriously. And that's because this isn't supposed to be too serious of a project. It's not novel, impressively complex, or even better than other similar projects (`yaurls.it/blah` is actually pretty long for a "short" URL)... but that's okay, because I'm not trying to replace anything or invent something new!

This is actually my first time doing any sort of webdev-related project, so I needed something simple enough to actually finish that would maybe allow for a few additional features. A URL shortener just seemed like the right choice for that, with the added bonus that it could potentially be something that I end up using (not for any added benefit over other, existing URL shorteners, but just because it would be cool to use my own thing, y'know?).

### Some things I learned
- How to **setup a simple backend** for a full CRUD app from scratch, specifically **using FastAPI and SQLite**.
- How to **create a simple frontend** to handle user input and make calls to the REST API that I made.
- How to organize such a project, even if the project is small in scale.

### Some challenges I faced
- **How to get started setting up a project like this**, like just in general. Even though it's probably one of the simplest CRUD apps out there, it still took a bit to figure out what I'd need and how to organize things to get stuff up and running. This is especially true given that I made it from scratch; I've contributed to apps before, but never had to build one from the ground up.
- **Making successful calls to the API from the UI**. I had used basic JavaScript before to handle things like executing small code blocks or sending popup alerts to the user. However, sending requests to an API was new territory for me, and I had to learn a lot about the structure of HTTP requests and how to actually send those in order to even just get the core functionality down.
- **Correctly handling redirects using FastAPI**. For a while, I was butting my head against my code because entering a shortened url would either redirect indefinitely or present a 404 - both of which would break the page - even when I knew the slug existed in the database. Turns out all the logic was correct - but I was simply missing an `https://` in the URL parameter for a RedirectRequest. If only I had thought to done that sooner (I finally thought of it when I was reading through the documentation and saw that there was an `https://` in the example code and not one in my code and I thought to try it).
- Getting used to Python syntax (I miss you, semicolons).
