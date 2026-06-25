# Testing dalam Python

## Daftar Isi
1. [Unittest](#1-unittest)
2. [Pytest](#2-pytest)
3. [Perbandingan](#3-perbandingan)

---

## 1. Unittest

Unittest adalah **built-in** Python untuk unit testing.

### Fungsi Assert Unittest

| Assert | Keterangan |
|--------|------------|
| `assertEqual(a, b)` | a == b |
| `assertNotEqual(a, b)` | a != b |
| `assertTrue(x)` | x == True |
| `assertFalse(x)` | x == False |
| `assertIsNone(x)` | x is None |
| `assertIn(a, b)` | a in b |
| `assertRaises(exc)` | Exception terjadi |
| `assertAlmostEqual(a, b)` | a ≈ b |

### Cara Jalankan

```bash
# Jalankan semua test
python -m unittest discover

# Jalankan file tertentu
python -m unittest test_unittest.py

# Jalankan class tertentu
python -m unittest test_unittest.TestFungsiMatematika

# Verbose mode
python -m unittest -v
```

---

## 2. Pytest

Pytest adalah third-party testing framework yang lebih **powerful** dan **mudah**.

### Install

```bash
pip install pytest
```

### Fitur Utama

1. **Simple Assert** - Cukup pakai `assert` biasa
2. **Parameterize** - Test dengan banyak input
3. **Fixture** - Setup/teardown yang bisa di-reuse
4. **Mark** - Kategorisasi test
5. **Plugin** - Banyak extension tersedia

### Cara Jalankan

```bash
# Jalankan semua test
pytest

# Verbose mode
pytest -v

# Jalankan file tertentu
pytest test_pytest.py

# Jalankan test tertentu
pytest test_pytest.py::test_tambah

# Skip test
pytest -k "not skip"
```

---

## 3. Perbandingan

| Fitur | Unittest | Pytest |
|-------|----------|--------|
| Builtin | Ya | Tidak (install dulu) |
| Assert | Banyak metode | Cukup `assert` |
| Readability | Lebih verbose | Lebih simpel |
| Fixture | `setUp/tearDown` | `@pytest.fixture` |
| Parameterize | Rumit | Mudah |
| Community | Standar | Lebih besar |

---

## Tips

1. **Naming**: Gunakan prefix `test_` untuk semua fungsi test
2. **Satu Assert**: Idealnya satu assert per test function
3. **Independence**: Test harus bisa jalan sendiri-sendiri
4. **Readability**: Buat test yang mudah dipahami
5. **Coverage**: Pastikan semua kode punya test
