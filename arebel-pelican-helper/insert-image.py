#!/usr/bin/env python3
import sys
import os
import shutil
import subprocess

def insert_image(current_buffer_name, source_image_path, name_suffix=""):
    """Copy image to blog directory and return Pelican image syntax."""
    # Check if source image exists
    if not os.path.exists(source_image_path):
        print(f"ERROR: Image file {source_image_path} does not exist!")
        sys.exit(1)
    
    # Get extension from source file
    _, extension = os.path.splitext(source_image_path)
    
    # Generate image filename based on current buffer name
    base_name = current_buffer_name.replace('.md', '')
    if name_suffix:
        image_filename = f"{base_name}-{name_suffix}{extension}"
    else:
        # Find next available number
        i = 1
        while True:
            image_filename = f"{base_name}-{i:02d}{extension}"
            if not os.path.exists(f"content/images/{image_filename}"):
                break
            i += 1
    
    # Copy image to content/images/
    target_path = f"content/images/{image_filename}"
    os.makedirs("content/images", exist_ok=True)
    shutil.copy2(source_image_path, target_path)
    
    # Resize image if ImageMagick is available (optional)
    try:
        subprocess.run(['convert', target_path, '-resize', '800x800>', target_path], 
                      capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        # ImageMagick not available or failed, skip resizing
        pass
    
    # Return the Pelican image syntax
    image_syntax = f"![{image_filename}]({{attach}}/images/{image_filename})"
    print(image_syntax)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("ERROR: Current buffer name and source image path are required")
        sys.exit(1)
    
    current_buffer_name = sys.argv[1]
    source_image_path = sys.argv[2]
    name_suffix = sys.argv[3] if len(sys.argv) > 3 else ""
    
    insert_image(current_buffer_name, source_image_path, name_suffix)