from app import validate_student, validate_email

def test_validate_student():
    assert validate_student("Alice", 20) == True
    assert validate_student("", -1) == False

def test_validate_email():
    assert validate_email("student@example.com") == True
    assert validate_email("invalid-email") == False