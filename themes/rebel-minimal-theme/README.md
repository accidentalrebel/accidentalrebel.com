# Rebel Minimal Theme for Pelican

A clean, minimal Pelican theme with rebellious personality touches designed for AccidentalRebel.com.

## Features

✨ **Core Features:**
- Clean, minimal design focused on readability
- Mobile-first responsive layout
- Dark mode support (auto-detects system preference)
- Reading progress indicator
- Syntax highlighting for code blocks
- Zero external dependencies

🏴‍☠️ **Rebellious Elements:**
- Glitch effect on site title hover
- Animated comic strip divider with hidden message
- Red accent color scheme
- Modern typography

📱 **Performance:**
- Lightweight CSS and JavaScript
- No external fonts or libraries
- Fast page loads
- Hardware-accelerated animations

## Installation

1. **Place the theme in your Pelican site:**
   ```bash
   cp -r rebel-minimal-theme /path/to/your/pelican/site/themes/
   ```

2. **Update your `pelicanconf.py`:**
   ```python
   THEME = 'themes/rebel-minimal-theme'
   ```

3. **Optional: Configure theme settings in `pelicanconf.py`:**
   ```python
   # Site settings
   SITENAME = 'Your Site Name'
   SITEURL = 'https://yoursite.com'
   
   # Theme settings
   DISPLAY_PAGES_ON_MENU = True
   DEFAULT_PAGINATION = 10
   
   # Analytics (optional)
   GOOGLE_ANALYTICS = 'UA-XXXXXXXX-X'
   
   # Comments (optional)
   DISQUS_SITENAME = 'your-disqus-sitename'
   ```

## Article Format

For best results, use this metadata format in your articles:

```markdown
Title: Your Article Title
Date: 2023-01-01 10:00
Category: category_name
Tags: tag1, tag2, tag3
Slug: your-article-slug
Summary: Brief description of your article

Your article content here...
```

## Syntax Highlighting

The theme includes built-in syntax highlighting for:
- Python
- JavaScript
- Bash/Shell
- C/C++

To use syntax highlighting, specify the language in your code blocks:

```markdown
```python
def hello_world():
    print("Hello, World!")
```
```

## Customization

### Colors

Edit `static/css/main.css` and modify the CSS variables:

```css
:root {
    --color-accent: #ff0040;        /* Main accent color */
    --color-text: #1a1a1a;         /* Text color */
    --color-bg: #ffffff;           /* Background color */
    --color-border: #e5e5e5;       /* Border color */
}
```

### Comic Strip Message

To change the hidden message in the comic strip, edit the `content` property in `static/css/main.css`:

```css
.comic-strip::before {
    content: 'YOUR_CUSTOM_MESSAGE_HERE';
    /* ... */
}
```

### Glitch Effect

To modify or disable the glitch effect, edit the `.site-title:hover` rule in `static/css/main.css`.

## Browser Support

- Chrome/Chromium 60+
- Firefox 60+
- Safari 12+
- Edge 79+

## Performance

The theme is optimized for performance:
- CSS: ~15KB minified
- JavaScript: ~5KB minified
- No external dependencies
- Hardware-accelerated animations
- Lazy-loaded features

## Contributing

This theme was specifically designed for AccidentalRebel.com, but feel free to adapt it for your own use!

## License

MIT License - feel free to use and modify as needed.