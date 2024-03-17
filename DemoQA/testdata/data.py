# Format: [('email', 'isValid')]

test_emails = [
    ("invalidemail", False),  # Invalid email format
    ("", False),  # Empty field
    ("valid@example.com", True),  # Valid email
]

# Format: [('firstName', 'lastName', isValid)]

test_names = [
    ("123", "456", False),            # Invalid: Numeric characters
    ("Jane$", "Doe!", False),         # Invalid: Special characters
    ("", "", False),                   # Invalid: Empty fields
    ("A" * 51, "B" * 51, False),      # Invalid: Exceeds maximum length
    ("John", "Doe", True),           # Valid alphabetic characters
]


test_genders = ['male', 'others', 'female']

# Format: [('mobile', 'isValid')]
test_mobiles = [
    ("", False),                 # Invalid: Empty field
    ("123456", False),           # Invalid: Less than 10 digits
    ("12345678901", False),      # Invalid: More than 10 digits
    ("abc1234567", False),       # Invalid: Contains alphabet
    ("123456$7890", False),      # Invalid: Contains special character
    ("1234567890", True),      # Valid: 10 digits without alphabet or special characters
]

test_dates = [
    ("future_date", "2025-December-31"),
    ("past_date", "1998-July-17"),
]

test_pictures = [
    ("invalid_picture", "invalid_file.pdf"),
    ("valid_picture", "valid_file.png"),
]

test_states = {
    "NCR": ["Delhi", "Gurgaon", "Noida"],
    "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
    "Haryana": ["Karnal", "Panipat"],
    "Rajasthan": ["Jaipur", "Jaiselmer"]
}


test_subjects = ['math', 'chemistry', 'english']
