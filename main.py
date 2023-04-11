import os
from pathlib import Path

# Dictionary of directories to organize different file formats into
DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  ".pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "TEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py", ".ipynb"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"],
    "C": [".c", ".cpp"]
}

# Dictionary to map file formats to their corresponding directories
FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}


def organize_junk():
    """
    Organize files in the current directory based on their file format.
    """

    # Loop through every entry in the current directory
    for entry in os.scandir():
        # Skip directories
        if entry.is_dir():
            continue

        # Get the file path and format
        file_path = Path(entry)
        file_format = file_path.suffix.lower()

        # Check if the file format is in the dictionary of directories
        if file_format in FILE_FORMATS:
            # Get the directory to move the file to
            directory_path = Path(FILE_FORMATS[file_format])
            # Create the directory if it doesn't exist
            directory_path.mkdir(exist_ok=True)
            # Move the file to the new directory
            file_path.rename(directory_path.joinpath(file_path))

    # Loop through all directories again to remove empty ones
    for dir in os.scandir():
        try:
            os.rmdir(dir)
        except:
            # Ignore errors if the directory is not empty
            pass


if __name__ == "__main__":
    organize_junk()
