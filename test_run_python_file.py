from functions.run_python_file import run_python_file

# Case 1
print(run_python_file("calculator", "main.py"))

#Case 2
print(run_python_file("calculator", "main.py", args=["3 + 5"]))

# Case 3
print(run_python_file("calculator", "tests.py"))

# Case 4
print(run_python_file("calculator", "../main.py"))

# Case 5
print(run_python_file("calculator", "nonexistent.py"))

#Case 6
print(run_python_file("calculator", "lorem.txt"))