# urlfinder

Pull the links out of a piece of text. One function, no dependencies.

## Install

```bash
pip install git+https://github.com/accessibleapps/urlfinder.git
```

Needs Python 3.8 or newer.

## Use it

```python
from urlfinder import find_urls

find_urls("New episode is up (https://example.com/ep42), and the notes are at www.example.org/notes.")
# ['https://example.com/ep42', 'www.example.org/notes']
```

`find_urls(text)` returns a list of strings, in the order they appear. It finds:

- anything that starts with a scheme like `http://`, `https://` or `ftp://`
- anything that starts with `www.`

It trims quotes, brackets, braces, parentheses, periods, commas, colons, semicolons and backslashes from both ends of each match, so a link at the end of a sentence or inside parentheses comes out clean. Other characters, such as `!` and `?`, are kept.

[Accessible Apps](https://getaccessibleapps.com) uses it to find the links in posts and messages so people can open them from the keyboard.
