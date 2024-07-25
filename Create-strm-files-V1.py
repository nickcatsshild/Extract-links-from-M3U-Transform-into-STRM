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

# Example usage
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
