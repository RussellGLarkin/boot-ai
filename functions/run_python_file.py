import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    """
    Runs a Python file in a specified working directory with optional arguments.

    Args:
        working_directory (str): The directory in which to run the Python file.
        file_path (str): The path to the Python file to be executed.
        args (list, optional): A list of arguments to pass to the Python file.
    """
    try:
        # Construct the absolute path to the Python file and ensure it is within the working directory
        working_dir_absolute_path = os.path.abspath(working_directory)
        full_path = os.path.join(working_dir_absolute_path, file_path)
        target_path = os.path.normpath(full_path)

        # Ensure the target file is within the working directory to prevent unauthorized access
        if not os.path.commonpath([working_dir_absolute_path, target_path]) == working_dir_absolute_path:  
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # Check if the target file exists and is a Python file
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # If the file doesn't end with .py, return an error
        if not target_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        # Construct the command to run the Python file with optional arguments
        command = ['python', target_path]
        if args:
            command.extend(args)

        # Run the command and capture the output
        result = subprocess.run(command, cwd=working_directory, capture_output=True, text=True, timeout=30)

        output = []
        # Return the output or error message
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if not result.stderr and not result.stdout:
            output.append("No output produced")

        # Format the output to include both STDOUT and STDERR if available
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        # Return the combined output
        return "\n".join(output)
                
    except Exception as e:
        return f"Error: executing Python file: {str(e)}"