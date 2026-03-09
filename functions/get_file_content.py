import os

from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    """
    Get the content of a file in the specified directory.

    Args:
        working_directory (str): The base directory to search for the file.
        file_path (str): The relative path to the file within the working directory.
    """

    # Construct the absolute path to the target file and ensure it is within the working directory
    try:
        working_dir_absolute_path = os.path.abspath(working_directory)
        full_path = os.path.join(working_dir_absolute_path, file_path)
        target_file = os.path.normpath(full_path)
                
        # Ensure the target file is within the working directory
        if not os.path.commonpath([working_dir_absolute_path, target_file]) == working_dir_absolute_path:  
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        # Check if the target file exists and is a file
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read and return the content of the target file
        with open(target_file, 'r') as f:
            content = f.read(MAX_CHARS)
            if f.read(1):  # Check if there is more content beyond the limit
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content

    # Handle exceptions that may occur during file access and reading
    except Exception as e:
        return f"Error: {str(e)}"
