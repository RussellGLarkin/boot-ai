import os

def write_file(working_directory, file_path, content):
    """
    Writes content to a file at the specified path.

    Args:
        working_directory (str): The base directory to resolve the file path against.
        file_path (str): The relative path to the file from the working directory.
        content (str): The content to write to the file.

    Returns:
        str: The full path to the written file.
    """

    try:
        working_dir_absolute_path = os.path.abspath(working_directory)
        full_path = os.path.join(working_dir_absolute_path, file_path)
        target_file_path = os.path.normpath(full_path)

        # Ensure the target file path is within the working directory
        if not os.path.commonpath([working_dir_absolute_path, target_file_path]) == working_dir_absolute_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(target_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        # Create parent directories if they do not exist
        os.makedirs(os.path.dirname(target_file_path), exist_ok=True)

        # Write the content to the file
        with open(target_file_path, 'w') as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: {str(e)}'