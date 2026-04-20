import re

def password_strength_checker(password):
    # Shart 1: Parol uzunligi kamida 8 belgidan iborat bo'lishi kerak
    if len(password) < 8:
        return False

    # Shart 2: Parolda kamida 1 katta harf bo'lishi kerak
    if not re.search("[A-Z]", password):
        return False

    # Shart 3: Parolda kamida 1 kichik harf bo'lishi kerak
    if not re.search("[a-z]", password):
        return False

    # Shart 4: Parolda kamida 1 raqam bo'lishi kerak
    if not re.search("[0-9]", password):
        return False

    # Shart 5: Parolda kamida 1 maxsus belgi bo'lishi kerak
    if not re.search("[!@#$%^&*()_+=-{};:'<>,./?]", password):
        return False

    # Agar barcha shartlar to'g'ri bo'lsa, parol kuchli
    return True

# Test qilish
print(password_strength_checker("Parol123"))  # False
print(password_strength_checker("Parol123!"))  # True
print(password_strength_checker("parol123!"))  # False
print(password_strength_checker("PAROL123!"))  # True
print(password_strength_checker("parol123"))  # False
print(password_strength_checker("PAROL123"))  # False
print(password_strength_checker("parol123!@#"))  # True
print(password_strength_checker("PAROL123!@#"))  # True
