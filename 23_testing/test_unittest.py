"""
Testing dengan UNSTANDARD LIBRARY: unittest
============================================
 unittest adalah built-in Python untuk testing

 Jalankan: python -m unittest test_untest.py
 Atau: python -m unittest discover (otomatis cari test_*.py)
"""

import unittest
from main import tambah, kurang, kali, bagi, cek_genap, sapa, Kalkulator


class TestFungsiMatematika(unittest.TestCase):
    """Test untuk fungsi matematika"""

    def test_tambah_positif(self):
        self.assertEqual(tambah(5, 3), 8)

    def test_tambah_negatif(self):
        self.assertEqual(tambah(-5, -3), -8)

    def test_tambah_nol(self):
        self.assertEqual(tambah(5, 0), 5)

    def test_kurang(self):
        self.assertEqual(kurang(10, 5), 5)

    def test_kurang_hasil_negatif(self):
        self.assertEqual(kurang(5, 10), -5)

    def test_kali(self):
        self.assertEqual(kali(4, 3), 12)

    def test_kali_nol(self):
        self.assertEqual(kali(5, 0), 0)

    def test_bagi_normal(self):
        self.assertEqual(bagi(10, 2), 5.0)

    def test_bagi_desimal(self):
        self.assertAlmostEqual(bagi(10, 3), 3.3333, places=3)

    def test_bagi_nol_error(self):
        with self.assertRaises(ValueError) as context:
            bagi(10, 0)
        self.assertEqual(str(context.exception), "Tidak bisa membagi dengan nol")


class TestFungsiLainnya(unittest.TestCase):
    """Test untuk fungsi non-matematika"""

    def test_cek_genap_true(self):
        self.assertTrue(cek_genap(4))

    def test_cek_genap_false(self):
        self.assertFalse(cek_genap(3))

    def test_cek_genap_nol(self):
        self.assertTrue(cek_genap(0))

    def test_sapa_normal(self):
        self.assertEqual(sapa("Budi"), "Halo, Budi!")

    def test_sapa_kosong_error(self):
        with self.assertRaises(ValueError):
            sapa("")


class TestKalkulator(unittest.TestCase):
    """Test untuk class Kalkulator"""

    def setUp(self):
        """Setup sebelum setiap test"""
        self.kalk = Kalkulator()

    def test_tambah(self):
        hasil = self.kalk.tambah(5, 3)
        self.assertEqual(hasil, 8)

    def test_riwayat(self):
        self.kalk.tambah(5, 3)
        self.kalk.tambah(10, 2)
        self.assertEqual(len(self.kalk.riwayat), 2)

    def test_riwayat_format(self):
        self.kalk.tambah(5, 3)
        self.assertEqual(self.kalk.riwayat[0], "5 + 3 = 8")

    def test_reset(self):
        self.kalk.tambah(5, 3)
        hasil = self.kalk.reset()
        self.assertTrue(hasil)
        self.assertEqual(len(self.kalk.riwayat), 0)

    def tearDown(self):
        """Cleanup setelah setiap test"""
        self.kalk = None


if __name__ == "__main__":
    unittest.main()
