import requests

BASE_URL = 'http://localhost:5000/books'

def show_menu():
    print("\n=== Menu Perpustakaan ===")
    print("1. Tampilkan Buku")
    print("2. Tambah Buku")
    print("3. Update Buku")
    print("4. Hapus Buku")
    print("5. Keluar")
    return input("Pilih menu: ")

while True:
    pilihan = show_menu()

    if pilihan == "1":
        r = requests.get(BASE_URL)
        for i, book in enumerate(r.json()):
            print(f"{i+1}. {book['title']} oleh {book['author']}")
    elif pilihan == "2":
        title = input("Judul: ")
        author = input("Penulis: ")
        r = requests.post(BASE_URL, json={"title": title, "author": author})
        print(r.json()['message'])
    elif pilihan == "3":
        idx = int(input("Index buku yang ingin diperbarui (0-based): "))
        title = input("Judul Baru: ")
        author = input("Penulis Baru: ")
        r = requests.put(f"{BASE_URL}/{idx}", json={"title": title, "author": author})
        print(r.json()['message'] if r.ok else r.json()['error'])
    elif pilihan == "4":
        idx = int(input("Index buku yang ingin dihapus (0-based): "))
        r = requests.delete(f"{BASE_URL}/{idx}")
        print(r.json()['message'] if r.ok else r.json()['error'])
    elif pilihan == "5":
        break
    else:
        print("Pilihan tidak valid.")
