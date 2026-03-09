from functions.get_file_content import get_file_content

# Test 1. Show the truncation message
lorem = get_file_content("calculator", "lorem.txt")
print(lorem[-200:])

# Note: The following tests are not checking the full content, just that the expected lines are present. 
# The full content is not printed to avoid overwhelming the output.

# Test 2. Print snippet of main.py to show 'def main():'
main_content = get_file_content("calculator", "main.py")
if "def main():" in main_content:
    print("Found: def main():")

# Test 3. Print the line for _apply_operator from calculator.py
calc_content = get_file_content("calculator", "pkg/calculator.py")
target = "def _apply_operator(self, operators, values)"
if target in calc_content:
    print(f"Found: {target}")

# Test 4. Print the error cases (these are short and required)
print(get_file_content("calculator", "/bin/cat"))
print(get_file_content("calculator", "pkg/does_not_exist.py"))