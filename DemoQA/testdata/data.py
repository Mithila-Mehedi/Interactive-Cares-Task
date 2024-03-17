# Format: [('email', 'isValid')]

test_emails = [
    ("valid@example.com", True),  # Valid email
    ("invalidemail", False),  # Invalid email format
    ("", False),  # Empty field
]

# Format: [('firstName', 'lastName', isValid)]

test_names = [
    ("John", "Doe", True),           # Valid alphabetic characters
    ("123", "456", False),            # Invalid: Numeric characters
    ("Jane$", "Doe!", False),         # Invalid: Special characters
    ("", "", False),                   # Invalid: Empty fields
    ("A" * 51, "B" * 51, False),      # Invalid: Exceeds maximum length
]


test_genders = ['male', 'female', 'others']

# Format: [('mobile', 'isValid')]
test_mobiles = [
    ("1234567890", True),      # Valid: 10 digits without alphabet or special characters
    ("", False),                 # Invalid: Empty field
    ("123456", False),           # Invalid: Less than 10 digits
    ("12345678901", False),      # Invalid: More than 10 digits
    ("abc1234567", False),       # Invalid: Contains alphabet
    ("123456$7890", False),      # Invalid: Contains special character
]

test_dates = [
    ("past_date", "1998-July-17"),
    ("future_date", "2025-December-31")
]

test_pictures = [
    ("valid_picture", "valid_file.png"),
    ("invalid_picture", "invalid_file.pdf")
]

test_states = {
    "NCR": ["Delhi", "Gurgaon", "Noida"],
    "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
    "Haryana": ["Karnal", "Panipat"],
    "Rajasthan": ["Jaipur", "Jaiselmer"]
}


test_subjects = ['math', 'chemistry', 'english']
