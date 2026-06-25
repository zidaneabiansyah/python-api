"""
CUSTOM EXCEPTION & EXCEPTION HIERARCHY
========================================
 Membuat exception sendiri untuk error handling yang lebih baik
"""

from typing import Optional, Any


# =============================================
# 1. CUSTOM EXCEPTION DASAR
# =============================================

class AppError(Exception):
    """Base exception untuk semua error di aplikasi ini"""
    pass


class ValidationError(AppError):
    """Error saat validasi data gagal"""
    pass


class NotFoundError(AppError):
    """Error saat data tidak ditemukan"""
    pass


class PermissionError(AppError):
    """Error saat user tidak punya akses"""
    pass


print("CUSTOM EXCEPTION DASAR")

try:
    raise ValidationError("Email tidak valid")
except ValidationError as e:
    print(f"ValidationError: {e}")
except AppError as e:
    print(f"AppError: {e}")


# =============================================
# 2. EXCEPTION DENGAN CUSTOM ATTRIBUTES
# =============================================

class DetailedError(Exception):
    def __init__(self, message: str, code: int, details: Optional[dict] = None):
        super().__init__(message)
        self.code = code
        self.details = details or {}

    def __repr__(self):
        return f"DetailedError('{self}', code={self.code})"

    def to_dict(self):
        return {
            "error": str(self),
            "code": self.code,
            "details": self.details,
        }


print("\nCUSTOM ATTRIBUTES")
try:
    raise DetailedError(
        "Gagal memproses",
        code=422,
        details={"field": "email", "reason": "invalid format"}
    )
except DetailedError as e:
    print(f"Error: {e}")
    print(f"Code: {e.code}")
    print(f"Details: {e.details}")
    print(f"Dict: {e.to_dict()}")


# =============================================
# 3. EXCEPTION HIERARCHY
# =============================================

# Base
class AppException(Exception):
    def __init__(self, message: str, error_code: str = "UNKNOWN"):
        super().__init__(message)
        self.error_code = error_code


# Authentication errors
class AuthError(AppException):
    pass

class LoginError(AuthError):
    pass

class TokenExpiredError(AuthError):
    pass


# Database errors
class DatabaseError(AppException):
    pass

class ConnectionError(DatabaseError):
    pass

class QueryError(DatabaseError):
    pass


# API errors
class APIError(AppException):
    def __init__(self, message: str, status_code: int, **kwargs):
        super().__init__(message, **kwargs)
        self.status_code = status_code


class NotFoundAPIError(APIError):
    def __init__(self, resource: str, resource_id: Any):
        super().__init__(
            f"{resource} with id {resource_id} not found",
            status_code=404,
            error_code="NOT_FOUND"
        )
        self.resource = resource
        self.resource_id = resource_id


print("\nEXCEPTION HIERARCHY")


def login(username: str, password: str):
    if username != "admin":
        raise LoginError(f"User {username} not found")
    if password != "secret":
        raise LoginError("Invalid password")
    return True


# Handle specific exceptions
try:
    login("user", "wrong")
except LoginError as e:
    print(f"LoginError: {e}")
except AuthError as e:
    print(f"AuthError: {e}")
except AppException as e:
    print(f"AppException: {e}")


# =============================================
# 4. EXCEPTION CHAINING
# =============================================

print("\nEXCEPTION CHAINING")


def connect_db(host: str):
    try:
        # Simulasi connection error
        raise OSError("Connection refused")
    except OSError as e:
        # Chain the exception
        raise ConnectionError(f"Database connection failed to {host}") from e


try:
    connect_db("localhost")
except ConnectionError as e:
    print(f"Error: {e}")
    print(f"Original: {e.__cause__}")


# =============================================
# 5. RAISE FROM
# =============================================

print("\nRAISE FROM")


def validate_age(age: Any):
    try:
        age_int = int(age)
        if age_int < 0 or age_int > 150:
            raise ValueError(f"Age {age_int} out of range")
        return age_int
    except ValueError as e:
        # Raise new exception, preserve original traceback
        raise ValidationError(f"Invalid age: {age}") from e


try:
    validate_age("abc")
except ValidationError as e:
    print(f"ValidationError: {e}")
    print(f"Original error: {e.__cause__}")


# =============================================
# 6. SUPPRESS EXCEPTION
# =============================================

from contextlib import suppress

print("\nSUPPRESS EXCEPTION")

# Tangkap dan suppress error tertentu
with suppress(FileNotFoundError):
    import os
    os.remove("file_yang_tidak_ada.txt")
    print("File dihapus")

print("Program lanjut...")


# =============================================
# 7. CONTOH NYATA - User Service
# =============================================

print("\nCONTOH NYATA - User Service")


class UserServiceException(AppException):
    pass

class UserNotFoundError(UserServiceException):
    def __init__(self, user_id: int):
        super().__init__(f"User {user_id} not found", "USER_NOT_FOUND")
        self.user_id = user_id

class DuplicateUserError(UserServiceException):
    def __init__(self, email: str):
        super().__init__(f"User with email {email} already exists", "DUPLICATE_USER")
        self.email = email


# Simulasi database
users_db = {
    1: {"id": 1, "nama": "Budi", "email": "budi@test.com"},
    2: {"id": 2, "nama": "Andi", "email": "andi@test.com"},
}


def get_user(user_id: int) -> dict:
    if user_id not in users_db:
        raise UserNotFoundError(user_id)
    return users_db[user_id]


def create_user(nama: str, email: str) -> dict:
    for user in users_db.values():
        if user["email"] == email:
            raise DuplicateUserError(email)

    new_user = {"id": len(users_db) + 1, "nama": nama, "email": email}
    users_db[new_user["id"]] = new_user
    return new_user


# Test
try:
    user = get_user(1)
    print(f"Found: {user}")
except UserNotFoundError as e:
    print(f"Error: {e}")

try:
    user = get_user(999)
except UserNotFoundError as e:
    print(f"Error: {e}")
    print(f"Error code: {e.error_code}")

try:
    new_user = create_user("Budi", "budi@test.com")
except DuplicateUserError as e:
    print(f"Error: {e}")


# =============================================
# 8. BUILT-IN EXCEPTION YANG SERING DIPAKAI
# =============================================

print("\nBUILT-IN EXCEPTION COMMON")

# ValueError - invalid value
try:
    int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

# TypeError - wrong type
try:
    "hello" + 123
except TypeError as e:
    print(f"TypeError: {e}")

# KeyError - dict key not found
try:
    d = {"a": 1}
    d["b"]
except KeyError as e:
    print(f"KeyError: {e}")

# IndexError - list index out of range
try:
    lst = [1, 2, 3]
    lst[10]
except IndexError as e:
    print(f"IndexError: {e}")

# AttributeError - attribute not found
try:
    s = "hello"
    s.append("x")
except AttributeError as e:
    print(f"AttributeError: {e}")

# ImportError - module not found
try:
    import nonexistent_module
except ImportError as e:
    print(f"ImportError: {e}")

# FileNotFoundError - file not found
try:
    open("nonexistent.txt")
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

# StopIteration - iterator exhausted
try:
    it = iter([1, 2])
    next(it)
    next(it)
    next(it)
except StopIteration as e:
    print(f"StopIteration: {e}")
