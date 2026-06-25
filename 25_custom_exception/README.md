# Custom Exception dalam Python

## Daftar Isi
1. [Custom Exception Dasar](#1-custom-exception-dasar)
2. [Custom Attributes](#2-custom-attributes)
3. [Exception Hierarchy](#3-exception-hierarchy)
4. [Exception Chaining](#4-exception-chaining)
5. [Context Manager](#5-context-manager)

---

## 1. Custom Exception Dasar

```python
class AppError(Exception):
    """Base exception untuk aplikasi"""
    pass

class ValidationError(AppError):
    """Error saat validasi"""
    pass

# Gunakan
raise ValidationError("Email tidak valid")
```

---

## 2. Custom Attributes

```python
class DetailedError(Exception):
    def __init__(self, message, code, details=None):
        super().__init__(message)
        self.code = code
        self.details = details or {}
        self.timestamp = datetime.now()

    def to_dict(self):
        return {
            "error": str(self),
            "code": self.code,
            "details": self.details,
        }
```

---

## 3. Exception Hierarchy

```
AppException
├── AuthError
│   ├── LoginError
│   └── TokenExpiredError
├── DatabaseError
│   ├── ConnectionError
│   └── QueryError
└── APIError
    ├── NotFoundAPIError
    └── ValidationError
```

### Best Practice
```python
# Handle dari spesifik ke umum
try:
    login()
except LoginError:
    # Handle login error
except AuthError:
    # Handle auth error
except AppException:
    # Handle app error
except Exception:
    # Handle unexpected error
```

---

## 4. Exception Chaining

```python
def connect_db():
    try:
        raise OSError("Connection refused")
    except OSError as e:
        # Chain exception - pertahankan traceback
        raise DatabaseError("DB failed") from e

# Hasil: DatabaseError disebabkan oleh OSError
```

### Raise From
```python
try:
    validate(age)
except ValueError as e:
    raise ValidationError("Invalid") from e  # Preserve original
```

---

## 5. Context Manager

```python
from contextlib import suppress

# Suppress error tertentu
with suppress(FileNotFoundError):
    os.remove("file.txt")

# Error di-suppress, program lanjut
```

---

## Built-in Exceptions Common

| Exception | Keterangan |
|-----------|------------|
| `ValueError` | Invalid value |
| `TypeError` | Wrong type |
| `KeyError` | Dict key not found |
| `IndexError` | List index out of range |
| `AttributeError` | Attribute not found |
| `ImportError` | Module not found |
| `FileNotFoundError` | File not found |
| `StopIteration` | Iterator exhausted |

---

## Best Practices

1. **Buat Exception Spesifik** - Jangan pakai `Exception` generik
2. **Gunakan Hierarchy** - Base exception untuk grup error
3. **Include Context** - Tambahkan info berguna di exception
4. **Chaining** - Pertahankan original exception
5. **Naming** - Akhiri dengan `Error` atau `Exception`
