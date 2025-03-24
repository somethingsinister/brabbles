from datetime import datetime

# Get user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
dob = input("Enter your date of birth (YYYY-MM-DD): ")

# Calculate age
birth_date = datetime.strptime(dob, "%Y-%m-%d")
today = datetime.today()
age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

# Print output
print(f"My name is {first_name} {last_name}")
print(f"I am {age} years old")
