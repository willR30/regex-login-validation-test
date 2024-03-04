import re
import tkinter as tk
from tkinter import messagebox


# Regular expressions, also known as regex or regexp, are sequences of characters that define a search pattern.
# They are used for pattern matching in strings, making it easier to search, manipulate, and validate text data.

# Regular expressions in Python are implemented through the 're' module. The most common functions for using regular
# expressions in Python are re.match(), re.search(), re.findall(), and re.sub().

# Here's a basic example of how to use a regular expression in Python:
# Suppose we want to find all occurrences of the word 'apple' in a string.
# We can use the re.findall() function with the regular expression 'apple':
text = "I have an apple, she has an apple, and we all love apples."
apple_occurrences = re.findall(r'apple', text)
print(apple_occurrences)  # Output: ['apple', 'apple', 'apple']

# In this example, the regular expression 'apple' matches the word 'apple' in the string.

# Regular expressions can be quite powerful and versatile, allowing for complex pattern matching and text manipulation.
# However, they can also be complex and difficult to read, especially for beginners.

# Now let's proceed with the validation functions for email addresses and passwords.


def validate_email(email):
    # Regular expression to validate email address
    email_pattern = r'^[a-zA-Z0-9._%+-]+@(gmail|outlook|protonmail)\.(com|net|site)$'
    if re.match(email_pattern, email):
        return True
    else:
        return False


def validate_password(password):
    # Regular expression to validate password
    password_pattern = r'^(?=.*[A-Z].*[A-Z])(?=.*[0-9])(?=.*[a-zA-Z]).{8,}$'
    if re.match(password_pattern, password):
        return True
    else:
        return False


def validate_credentials():
    email = email_entry.get()
    password = password_entry.get()

    if validate_email(email) and validate_password(password):
        messagebox.showinfo("Validation Result", "Email and password are valid.")
    else:
        messagebox.showerror("Validation Result", "Invalid email or password.")


# GUI setup
root = tk.Tk()
root.title("Email and Password Validation")

# Email entry
email_label = tk.Label(root, text="Email:")
email_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
email_entry = tk.Entry(root)
email_entry.grid(row=0, column=1, padx=5, pady=5)

# Password entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

# Validate button
validate_button = tk.Button(root, text="Validate", command=validate_credentials)
validate_button.grid(row=2, columnspan=2, padx=5, pady=5)

root.mainloop()
