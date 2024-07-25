# Extract Links from M3U and Transform into STRM

## Purpose

The purpose of this script is to create `.strm` files by extracting video links from `.m3u` lists. This helps organize films and series in Jellyfin by linking the videos in `.strm` files, allowing Jellyfin to manage and play them as if they were directly in the library.

## Description

My Jellyfin server project is getting better and better. To organize films and series, I came across `.m3u` lists, and the problem of organizing them started. With this script, I can create `.strm` files and link the videos inside, allowing Jellyfin to work its magic.

## Usage Instructions

### Handling Colon Characters

One issue I encountered is with names that contain colons (`:`). Before running the script, rename files with colons to use a dash (`-`). For example, change `Spider-Man: No Way Home` to `Spider-Man - No Way Home`.

### Script

Below is the updated script that saves `.strm` files in the "Strm" folder within the script's directory.

```python
import os
import re
import logging

logging.basicConfig(level=logging.INFO)

def create_strm_files(m3u_data, output_dir="Strm"):
    """
    Extracts movie titles and URLs from M3U data and creates .strm files.

    Args:
        m3u_data (str): The M3U data as a string.
        output_dir (str, optional): The directory to create .strm files in. Defaults to "Strm".
    """
    movies = []
    for line in m3u_data.splitlines():
        if line.startswith("#EXTINF"):
            match = re.search(r'tvg-name="([^"]+)', line)
            if match:
                title = match.group(1)
                title = re.sub(r':', ' - ', title)
                movies.append((title, ""))
        elif line.startswith("http"):
            movies[-1] = (movies[-1][0], line.strip())
    
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create .strm files with UTF-8 encoding
    for title, url in movies:
        filename = os.path.join(output_dir, f"{title}.strm")
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(url)
            logging.info(f"Created .strm file: {filename}")
        except IOError as e:
            logging.error(f"Error creating file {filename}: {e}")

    print("Successfully created .strm files with movie URLs!")

# Example usage
m3u_data = """#EXTM3U
#EXTINF:-1 tvg-name="Movie Name 1 (2023)" tvg-logo="",Movie Name 1 (2023)
http://example.com/movie1.mp4
#EXTINF:-1 tvg-name="Another Movie (2022)" tvg-logo="",Another Movie (2022)
http://example.com/movie2.mp4
#EXTINF:-1 tvg-name="電影名稱 (2021)" tvg-logo="",電影名稱 (2021)" (Chinese title)
http://example.com/movie3.mp4
"""
create_strm_files(m3u_data)
```

### Breakdown of Changes

1. **Import `os` Library:** Used for working with directories and files.
2. **Get Script Directory:** `script_dir = os.path.dirname(__file__)` retrieves the directory where the script resides.
3. **Create "Strm" Folder Path:** `strm_dir = os.path.join(script_dir, "Strm")` combines the script directory and "Strm" to create the complete path.
4. **Check for "Strm" Folder Existence:** `if not os.path.exists(strm_dir)` verifies if the "Strm" folder exists.
5. **Create "Strm" Folder (if needed):** `os.makedirs(strm_dir)` creates the "Strm" folder if it's missing.
6. **Combine Filename with Path:** `filename = os.path.join(strm_dir, f"{title}.strm")` constructs the complete filename with the path inside the "Strm" folder.

Now, when the script runs, it will save the `.strm` files within the "Strm" folder located in the same directory as the script itself.

### Future Steps

Currently, this script only creates `.strm` files. The next step is to develop a script that organizes these `.strm` files into their respective folders with the correct names. Stay tuned for updates!
