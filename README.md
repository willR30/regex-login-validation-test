# Email and Password Validation

This Python script provides a basic GUI application for validating email addresses and passwords using regular expressions. The application allows users to input an email address and a password, and upon clicking the "Validate" button, it verifies whether the provided email and password meet certain criteria.

## Regular Expressions
Regular expressions (regex) are used to define search patterns in strings, making it easier to search, manipulate, and validate text data. In this script, regex patterns are employed to validate email addresses and passwords.

## Email Validation
The `validate_email()` function checks whether the input email address conforms to the specified pattern. It verifies that the email address follows the format of username@domain.extension, where the domain is limited to Gmail, Outlook, or ProtonMail, and the extension can be either com, net, or site.

## Password Validation
The `validate_password()` function ensures that the input password meets certain criteria. It verifies that the password contains at least two uppercase letters, one digit, and a minimum length of eight characters.

## Validation Process
The `validate_credentials()` function retrieves the email and password entered by the user and validates them using the `validate_email()` and `validate_password()` functions. If both the email and password meet the specified criteria, a success message is displayed using a message box; otherwise, an error message is shown.

## GUI Setup
The script utilizes the Tkinter library to create a simple GUI interface. It includes fields for entering email and password, along with a "Validate" button to trigger the validation process.

## Requirements
To run this script, you need:
- Python installed on your system.
- The Tkinter library, which is included in the standard Python installation.
- No additional packages or dependencies are required.

---

The script combines the power of regular expressions with a user-friendly GUI, providing a convenient tool for validating email addresses and passwords.
