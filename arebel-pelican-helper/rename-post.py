#!/usr/bin/env python3
import sys
import os
import re

def rename_blog_post(old_filename, new_title):
    """Rename a blog post by updating its title, slug, and filename."""
    # Check if file exists
    if not os.path.exists(old_filename):
        print(f"ERROR: File {old_filename} does not exist!")
        sys.exit(1)
    
    # Generate new slug from title
    new_slug = new_title.lower()
    new_slug = ''.join(c if c.isalnum() or c == ' ' else '' for c in new_slug)
    new_slug = new_slug.replace(' ', '-')
    new_slug = '-'.join(filter(None, new_slug.split('-')))
    
    # Generate new filename
    directory = os.path.dirname(old_filename)
    new_filename = os.path.join(directory, f"{new_slug}.md")
    
    # Check if new filename already exists
    if new_filename != old_filename and os.path.exists(new_filename):
        print(f"ERROR: File {new_filename} already exists!")
        sys.exit(1)
    
    # Read the original file
    with open(old_filename, 'r') as f:
        content = f.read()
    
    # Update the title and slug in the content
    content = re.sub(r'^Title:.*$', f'Title: {new_title}', content, flags=re.MULTILINE)
    content = re.sub(r'^Slug:.*$', f'Slug: {new_slug}', content, flags=re.MULTILINE)
    
    # Write to new file
    with open(new_filename, 'w') as f:
        f.write(content)
    
    # Remove old file if filename changed
    if new_filename != old_filename:
        os.remove(old_filename)
    
    # Return the new filename for Emacs to open
    print(new_filename)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("ERROR: Both old filename and new title are required")
        sys.exit(1)
    
    old_filename = sys.argv[1]
    new_title = sys.argv[2]
    
    rename_blog_post(old_filename, new_title)