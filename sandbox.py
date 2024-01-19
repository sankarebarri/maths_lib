# import re

# input_string = "42+3 - 3 * -3"  # Replace with your actual input string

# # Define the regex pattern
# pattern = r'\b\d+(?:\.\d+)?\b'

# # Find all matches in the input string
# matches = re.findall(pattern, input_string)

# # Print the extracted numbers
# print(matches)

# import re

# input_string = "42+3 + -58 - 3 * -3"  # Replace with your actual input string

# # Define the regex pattern with an optional minus sign
# pattern =  r'-?\b\s*\d+(?:\.\d+)?\b'

# # Find all matches in the input string
# matches = re.findall(pattern, input_string)

# # Print the extracted numbers
# print(matches)

# import re

# input_string = "42+3 + -58 - 3 * -3"  # Replace with your actual input string

# # Define the regex pattern to extract numbers with an optional minus sign and ignore spaces
# pattern = r'-?\b\s*\d+(?:\.\d+)?\b'

# # Find all matches in the input string, ignoring spaces between the minus sign and the number
# matches = [float(match.replace(" ", "")) if '-' in match else float(match) for match in re.findall(pattern, input_string)]

# # Print the extracted numbers
# print(matches)


# import re

# def extract_numbers(text):
#   """
#   Extracts all numbers from a string containing only numbers and operators.

#   Args:
#     text: The string to extract numbers from.

#   Returns:
#     A list of strings representing the extracted numbers.
#   """

import re

input_string = "42 - 3"  # Replace with your actual input string

# Define the regex pattern to extract numbers with an optional minus sign and handle spaces
pattern = r'-?\b\s*\d+(?:\.\d+)?(?:\s*-\s*\d+(?:\.\d+)?)*\b'

# Find all matches in the input string, considering spaces around the minus sign
matches = [float(num.replace(" ", "")) for match in re.finditer(pattern, input_string) for num in re.findall(r'-?\d+(?:\.\d+)?', match.group())]

# Print the extracted numbers
print(matches)

