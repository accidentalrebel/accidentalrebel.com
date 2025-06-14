#!/usr/bin/env python3
import sys
import os
from datetime import datetime

def create_blog_post(title, tags="", category="", image=""):
    """Create a new Pelican blog post with proper formatting."""
    # Generate slug from title
    slug = title.lower()
    slug = ''.join(c if c.isalnum() or c == ' ' else '' for c in slug)
    slug = slug.replace(' ', '-')
    slug = '-'.join(filter(None, slug.split('-')))  # Remove multiple hyphens
    
    # Get current date and time
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Create filename
    filename = f"content/{slug}.md"
    
    # Check if file already exists
    if os.path.exists(filename):
        print(f"ERROR: File {filename} already exists!")
        sys.exit(1)
    
    # Create the content
    content = f"""Title: {title}
Date: {date}
Slug: {slug}
Tags: {tags}
Category: {category}
Image: {image}

Write your post content here...

"""
    
    # Write the file
    with open(filename, 'w') as f:
        f.write(content)
    
    # Return the filename for Emacs to open
    print(filename)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: Title is required")
        sys.exit(1)
    
    title = sys.argv[1]
    tags = sys.argv[2] if len(sys.argv) > 2 else ""
    category = sys.argv[3] if len(sys.argv) > 3 else ""
    image = sys.argv[4] if len(sys.argv) > 4 else ""
    
    create_blog_post(title, tags, category, image)