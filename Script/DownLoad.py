import os
import requests
from urllib.parse import urlparse


def download_image(url, output_folder, index):
    """
    Downloads an image from a URL and saves it to the specified folder.

    Args:
        url (str): The URL of the image.
        output_folder (str): The path to the output folder.
        index (int): The index of the image (used for naming the file).
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Determine the file extension from the URL
        parsed_url = urlparse(url)
        file_extension = os.path.splitext(parsed_url.path)[1]
        if not file_extension:
            file_extension = ".png"  # Default to .png if no extension found

        filename = os.path.join(output_folder, f"{index}{file_extension}")

        with open(filename, "wb") as outfile:
            for chunk in response.iter_content(chunk_size=8192):
                outfile.write(chunk)
        print(f"Downloaded: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image from {url}: {e}")
    except Exception as e:
        print(f"Error saving image: {e}")


def download_from_file(input_file, output_folder):
    """
    Reads URLs from a file and downloads each URL as an image.

    Args:
        input_file (str): Path to the input file.
        output_folder (str): Path to the output folder.
    """
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return
    except Exception as e:
        print(f"Error reading input file: {e}")
        return

    lines = content.split("\n")

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for index, url in enumerate(lines):
        if url.strip():  # Check if the line is not empty
            download_image(url, output_folder, index + 1)
        else:
            print(f"Skipping empty line at index {index}")


if __name__ == "__main__":
    input_file = "simple-lenormand.txt"
    output_folder = "SimpleLenormand"
    download_from_file(input_file, output_folder)
