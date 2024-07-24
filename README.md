# Extract-links-from-M3U-Transform-into-STRM
The purpose of the script is to create strm files by extracting video links from m3u lists

My project with jellyfin server is getting better and better, in order to organize films and series, I've come across m3u lists and that's when the problem started. Organize this, with this script I can create the strm and link the video inside and jellyfin does the magic.

%%
Here's the updated script that saves the .strm files in the "Strm" folder within the script's directory:
Python

import os
import re

# Sample M3U data with various encodings
m3u_data = """
#EXTM3U
#EXTINF:-1 tvg-name="Movie Name 1 (2023)" tvg-logo="",Movie Name 1 (2023)
http://example.com/movie1.mp4
#EXTINF:-1 tvg-name="Another Movie (2022)" tvg-logo="",Another Movie (2022)
#EXTINF:-1 tvg-name="電影名稱 (2021)" tvg-logo="",電影名稱 (2021)" (Chinese title)
http://example.com/movie2.mp4
#EXTINF:-1 tvg-name="Фильм Название (2020)" tvg-logo="",Фильм Название (2020)" (Russian title)
http://example.com/movie3.mp4
"""

# Extract movie titles and URLs using regular expressions
movies = []
for line in m3u_data.splitlines():
    if line.startswith("#EXTINF"):
        # Extract title (including characters outside the basic multilingual plane)
        match = re.search(r'tvg-name="([^"]+)', line)
        if match:
            title = match.group(1)
            movies.append((title, ""))
    elif line.startswith("http"):
        # Extract URL
        movies[-1] = (movies[-1][0], line.strip())

# Create .strm files with UTF-8 encoding
for title, url in movies:
    # Get the script's directory
    script_dir = os.path.dirname(__file__)

    # Create the path for the "Strm" folder
    strm_dir = os.path.join(script_dir, "Strm")

    # Ensure the "Strm" folder exists
    if not os.path.exists(strm_dir):
        os.makedirs(strm_dir)

    # Create the filename with path inside the "Strm" folder
    filename = os.path.join(strm_dir, f"{title}.strm")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(url)

print("Successfully created .strm files with movie URLs in the Strm folder!")

Use o código com cuidado.

Here's a breakdown of the changes:

    Import os library: We import the os library to work with directories and files.
    Get script directory: script_dir = os.path.dirname(__file__) retrieves the directory where the script resides.
    Create "Strm" folder path: strm_dir = os.path.join(script_dir, "Strm") combines the script directory and "Strm" to create the complete path.
    Check for "Strm" folder existence: if not os.path.exists(strm_dir) verifies if the "Strm" folder exists.
    Create "Strm" folder (if needed): os.makedirs(strm_dir) creates the "Strm" folder if it's missing.
    Combine filename with path: filename = os.path.join(strm_dir, f"{title}.strm") constructs the complete filename with the path inside the "Strm" folder.

Now, when the script runs, it will save the .strm files within the "Strm" folder located in the same directory as the script itself.
