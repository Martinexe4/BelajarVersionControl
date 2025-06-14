def penjumlahan(a, b):
    """Fungsi untuk menjumlahkan dua angka."""
    return a + b

def pengurangan(a, b):
    """Fungsi untuk mengurangi dua angka."""
    return a - b

def perkalian(a, b):
    """Fungsi untuk mengalikan dua angka."""
    return a * b

def pembagian(a, b):
    """Fungsi untuk membagi dua angka."""
    if b == 0:
        raise ValueError("Pembagian dengan nol tidak diperbolehkan.")
    return a / b

def pangkat(a, b):
    """Fungsi untuk menghitung pangkat dari suatu angka."""
    return a ** b


nilai1 = float(input("Masukkan angka pertama: "))
nilai2 = float(input("Masukkan angka kedua: "))

operasi = input("Pilih operasi (tambah, kurang, kali, bagi, pangkat): ").strip().lower()
if operasi == "tambah":
    hasil = penjumlahan(nilai1, nilai2)
elif operasi == "kurang":
    hasil = pengurangan(nilai1, nilai2)
elif operasi == "kali":
    hasil = perkalian(nilai1, nilai2)
elif operasi == "bagi":
    try:
        hasil = pembagian(nilai1, nilai2)
    except ValueError as e:
        print(e)
        hasil = None
elif operasi == "pangkat":
    hasil = pangkat(nilai1, nilai2)
else:
    print("Operasi tidak dikenali.")
    hasil = None

