import os

def get_files_info(working_directory, directory="."):
    """
    Get information about files in the specified directory.

    Args:
        working_directory (str): The base directory to search for files.
        directory (str): The subdirectory within the working directory to search.
        """

    # Construct the absolute path to the target directory and ensure it is within the working directory
    try:
        working_dir_absolute_path = os.path.abspath(working_directory)
        full_path = os.path.join(working_dir_absolute_path, directory)
        target_directory = os.path.normpath(full_path)

        # Ensure the target directory is within the working directory to prevent unauthorized access
        if not os.path.commonpath([working_dir_absolute_path, target_directory]) == working_dir_absolute_path:  
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        # Check if the target directory exists and is a directory
        if not os.path.isdir(target_directory):
            return f'Error: "{directory}" is not a directory'

        # List files in the target directory and gather their information
        file_list = []
        for file_name in os.listdir(target_directory):
            item_path = os.path.join(target_directory, file_name)
            file_size = os.path.getsize(item_path)
            is_directory = os.path.isdir(item_path)
            file_list.append(f"  - {file_name}: file_size={file_size} bytes, is_dir={is_directory}")
        return "\n".join(file_list)

    # Handle exceptions that may occur during directory access and file information retrieval
    except Exception as e:
        return f"Error listing files: {str(e)}" 