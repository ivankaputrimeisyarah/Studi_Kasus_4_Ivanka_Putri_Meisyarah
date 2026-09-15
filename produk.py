produk = {
    "nama" : "Apple Pie",
    "harga" : "13000",
    "stok" : "28"
}

while True :
    print("==== MENU DATA PRODUK MCD ====")
    print("1. Tampilkan produk")
    print("2. Tambahkan kategori")
    print("3. Mengubah harga")
    print("4. Menghapus kategori")
    print("5. Keluar")

    pilihan = input("Pilih menu :")

    if pilihan == "1":
        print("=== Data produk ===")  
        print("Nama  :", produk["nama"])
        print("Harga :", produk["harga"])
        print("stok  :", produk["stok"])

        if "kategori" in produk:
            print("Kategori :", produk["kategori"])

    elif pilihan == "2":
        kategori = input("Masukkan kategori :")
        produk["kategori"] = kategori
        print("Kategori berhasil ditambahkan!")
        print("Data terbaru:", produk)

    elif pilihan == "3":
        harga_baru = int(input("Masukkan harga baru:"))
        produk["harga"] = harga_baru
        print("Harga berhasil ditambahkan!")
        print("Data terbaru:", produk)

    elif pilihan == "4":
        if "kategori" in produk:
            del produk["kategori"]
            print("Kategori berhasil dihapus!")
            print("Data terbaru:", produk)

    elif pilihan == "5":
        print("Data produk sementara :")
        print(produk)
        print("SELESAI")
        break

    else:
        print("Menu tidak tersedia")