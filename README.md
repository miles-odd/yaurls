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

Some additional features _are_ planned, such as:

- creating custom slugs (i.e. `yaurls.it/customslug`)
- creating click-limited/self-destructing links
- tracking statistics, such as number of (unique) clicks, location and device information, etc.

and possibly even more things, if I come up with more things and feel like adding them.

## How do I use it?

Currently, the only way to use it is to access it via the web, so simply visit [yaurls.it](https://www.youtube.com/watch?v=dQw4w9WgXcQ) to try it out!

## Why am I making this?

As you may have figured out by now, this README hasn't been taking itself too seriously. And that's because this isn't supposed to be too serious of a project. It's not novel, impressively complex, or even better than other similar projects (`yaurls.it/blah` is actually pretty long for a "short" URL)... but that's okay, because I'm not trying to replace anything or invent something new!

This is actually my first time doing any sort of webdev-related project, so I needed something simple enough to actually finish that would maybe allow for a few additional features. A URL shortener just seemed like the right choice for that, with the added bonus that it could potentially be something that I end up using (not for any added benefit over other, existing URL shorteners, but just because it would be cool to use my own thing, y'know?).

### Some things I learned
- How to **setup a simple backend** for a full CRUD app from scratch, **using FastAPI and SQLite**
- How to **actually make requests** and call the API from the user interface **using JS**
- How to organize such a project.

### Some challenges I faced
- In general, just **how to get started setting up a project like this**. Even though it's probably one of the simplest CRUD apps out there, it still took a bit to figure out what I'd need and how to organize things to get stuff up and running. This is especially true given that I made it from scratch; I've contributed to apps before, but never had to build one from the ground up.
- **Making successful calls to the API from the UI**. I found that backend was easier for me; it's one thing to actually implement the API and play around with it using hardcoded tests or Swagger, but it's another thing to actually integrate it into a webpage and have everything working. It seems like I don't really like frontend work :/ but it's something I must learn anyway.
- Getting used to Python syntax (I miss you, semicolons).
