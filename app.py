def validate_student(name, age):
    return len(name) > 0 and age > 0

def validate_email(email):
    return "@" in email and "." in email

if __name__ == "__main__":
    print("Student Management System Initialized")