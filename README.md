# Extract-links-from-M3U-Transform-into-STRM
The purpose of the script is to create strm files by extracting video links from m3u lists

My project with jellyfin server is getting better and better, in order to organize films and series, I've come across m3u lists and that's when the problem started. Organize this, with this script I can create the strm and link the video inside and jellyfin does the magic.

Just one thing, I had a problem with names that contain : oh my, that didn't work so before running the script, change names that contain : ; In the middle example in the name of the film there is Spider-Man: No return home, that's the problem at the moment, I'm going to try to solve it currently I edit the name with a dash -.
%%
Here's the updated script that saves the .strm files in the "Strm" folder within the script's directory:
Python

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
      try:
        # Validate URL (optional)
        # from urllib.parse import urlparse
        # url = urlparse(movies[-1][1])
        # if not all([url.scheme, url.netloc]):
        #   raise ValueError("Invalid URL format")
        logging.info(f"Processing movie: {movies[-1][0]}")
      except ValueError as e:
        logging.error(f"Error processing movie: {e}")
        continue  # Skip invalid URLs

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

# Example usage:
# You can download a list of m3u or m3u8 movies, and add them to Jellyfin, but it's a mess, I want to organize them into libraries, hence this script. You copy the m3u content and paste it in the location, save and run the script, it will save in the same location where the script is running in a Strm folder (create this folder ok) run the script and that's it, all the films with names in .strm Jellyfin will read it as if the film were inside the library, but linked to the storage server. Well, then all you have to do is hunt for films around, right?
# You can replace this with user input or read from a file
m3u_data = """
#EXTM3U
#EXTINF:-1 tvg-name="Movie Name 1 (2023)" tvg-logo="",Movie Name 1 (2023)
http://example.com/movie1.mp4
#EXTINF:-1 tvg-name="Another Movie (2022)" tvg-logo="",Another Movie (2022)
#EXTINF:-1 tvg-name="電影名稱 (2021)" tvg-logo="",電影名稱 (2021)" (Chinese title)
http://example.com/movie2.mp4
"""
create_strm_files(m3u_data)

The script has a correction bug for errors that occurred when the film name has name : name now it ignores this and can create the strm file.

Here's a breakdown of the changes:

    Import os library: We import the os library to work with directories and files.
    Get script directory: script_dir = os.path.dirname(__file__) retrieves the directory where the script resides.
    Create "Strm" folder path: strm_dir = os.path.join(script_dir, "Strm") combines the script directory and "Strm" to create the complete path.
    Check for "Strm" folder existence: if not os.path.exists(strm_dir) verifies if the "Strm" folder exists.
    Create "Strm" folder (if needed): os.makedirs(strm_dir) creates the "Strm" folder if it's missing.
    Combine filename with path: filename = os.path.join(strm_dir, f"{title}.strm") constructs the complete filename with the path inside the "Strm" folder.

Now, when the script runs, it will save the .strm files within the "Strm" folder located in the same directory as the script itself.
!!!!! Hell, now I have a lot of movie files in strm that zone, next step is a script to put them in their respective folders with the name everything organized. Wait, I'll post it here.
