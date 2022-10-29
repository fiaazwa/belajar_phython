#membuat struk belanja
import datetime
from tkinter import Y

waktu = datetime.datetime.now().strftime("%X")
tanggal = datetime.datetime.now().strftime("%X")

#nama dari kasir
nama_kasir = input("masukkan nama kasir: ")
#tanpilkan nama
print("""
SAGA SUPERMARKET & FRESH REMU
Jln.Mabruk No. 10 - Remu Utara
Kota Sorong - Papua Barat
Hp. 0821 9750 9639
{tanggal} {waktu} 
""")

Tambahkan_barang = 'y'
Total_belanja = 0
Jumblah_blanja = 0
while ('y' in Tambahkan_barang) :

#nama barang
nama_barang = input("nama barang: ")

#harga barang
harga_barang = input ("harga barang: ")

#jumblah barang
jumblah_barang = input("jumblah barang: ")

#tampilkan barang
print(f"""
(nama_barang)
pcs    (jumblah_barang) (harga_barang)     
""")

#kalkulasi belanja dan jumblah belanja



tambahkan_barang = input ("ada barang lagi?(y/n): ")