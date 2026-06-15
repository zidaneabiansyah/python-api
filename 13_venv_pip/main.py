# Panduan Virtual Environment & pip
# ================================
#
# 1. BUAT VIRTUAL ENV
#    python3 -m venv venv
#
# 2. AKTIFKAN
#    Linux/Mac: source venv/bin/activate
#    Windows:   venv\Scripts\activate
#
# 3. CEK PATH (pastikan pake env)
#    which python
#
# 4. INSTALL PACKAGE
#    pip install requests
#    pip install flask
#    pip install pandas
#
# 5. INSTALL VERSI TERTENTU
#    pip install requests==2.31.0
#    pip install "flask>=2.0"
#
# 6. LIHAT INSTALLED PACKAGES
#    pip list
#    pip freeze
#
# 7. SAVE KE requirements.txt
#    pip freeze > requirements.txt
#
# 8. INSTALL DARI requirements.txt
#    pip install -r requirements.txt
#
# 9. UNINSTALL
#    pip uninstall requests -y
#
# 10. MATIKAN VENV
#     deactivate

# Contoh: install & pake package requests
# (uncomment baris bawah kalo mau tes, pastikan `pip install requests` dulu)

# import requests
# resp = requests.get("https://api.github.com")
# print(f"Status: {resp.status_code}")
# print(resp.json())

print("Lihat komentar di atas untuk panduan venv & pip")
print("Jalankan perintah di terminal, bukan di sini")
