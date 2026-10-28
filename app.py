def validate_student(name, age):
    return len(name) > 0 and age > 0

def validate_email(email):
    return "@" in email and "." in email

# New validation logic added for SMS-2
def validate_course(course_code):
    return len(course_code) > 0