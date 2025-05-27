# Method 1: Slicing
def reverse_string_slicing(s):
  return s[::-1]

# Method 2: Using reversed() and join()
def reverse_string_reversed(s):
  return "".join(reversed(s))

# Method 3: Using a loop
def reverse_string_loop(s):
  reversed_s = ""
  for char in s:
    reversed_s = char + reversed_s
  return reversed_s

# Method 4: Using recursion
def reverse_string_recursive(s):
  if len(s) == 0:
    return s
  else:
    return reverse_string_recursive(s[1:]) + s[0]

# Example usage
string = "hello"
print("Original string:", string)

reversed_string_slicing = reverse_string_slicing(string)
print("Reversed string (slicing):", reversed_string_slicing)

reversed_string_reversed = reverse_string_reversed(string)
print("Reversed string (reversed):", reversed_string_reversed)

reversed_string_loop = reverse_string_loop(string)
print("Reversed string (loop):", reversed_string_loop)

reversed_string_recursive = reverse_string_recursive(string)
print("Reversed string (recursion):", reversed_string_recursive)
