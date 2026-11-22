# Asking for information
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
fav_subject = input("Enter favorite subject: ")

# Formatting information
name = [first_name.strip().capitalize(), last_name.strip().capitalize()]
full_name = " " .join(name)
name_code = (full_name.upper())
clean_section = (section.strip().upper())
clean_subject = (fav_subject.strip().title())

# Displaying formatted output
print("Formatted Output:")
print("Name: ", full_name)
print("Name Code: ", name_code)
print("Section: ", clean_section)
print("Favorite Subject: ", clean_subject)
print("Character Count (full name): ", len(full_name))
