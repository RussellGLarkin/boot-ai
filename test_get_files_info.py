from functions.get_files_info import get_files_info

# Case 1
print("Result for current directory:")
print(f"{get_files_info('calculator', '.')}")

# Case 2
print("\nResult for 'pkg' directory:")
print(f"{get_files_info('calculator', 'pkg')}")

# Case 3
print("\nResult for '/bin' directory:")
print(f"    {get_files_info('calculator', '/bin')}")

# Case 4
print("\nResult for '../' directory:")
print(f"    {get_files_info('calculator', '../')}")