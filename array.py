def cari_laptop(laptop_list, brand): # fungsi untuk mencari laptop berdasarkan merk
    for laptop in laptop_list: # looping untuk mencari laptop
        if laptop['nama'] == brand: # jika merk laptop sama
            return laptop # return laptop
    return None # jika tidak ada return none

laptop = [
    {"nama": "asus", "jumlah": 10}, # membuat array yang berisikan nama dan jumlah laptop 
    {"nama": "lenovo", "jumlah": 5},
    {"nama": "macbook", "jumlah": 8},
    {"nama": "hp", "jumlah": 15},
    {"nama": "dell", "jumlah": 12},
    {"nama": "acer", "jumlah": 20}
]

#searching laptop
user1 = input("Masukkan merk laptop: ")
user1_lower = user1.lower().strip() # mengconvert menjadi lower case dan mmenghilangkan spasi

cari_laptop = cari_laptop(laptop, user1_lower)

if cari_laptop:
    print(f"Laptop {user1} ada di list. Jumlahnya: {cari_laptop['jumlah']}")
else:
    print(f"{user1}, laptop kamu tidak ada di list")

# Mengurutkan berdasarkan jumlah, lalu nama (jika jumlah sama) menggunakan fungsi sort dengan lambda
laptop.sort(key=lambda x: (x['jumlah'], x['nama']))
print(f'Ini adalah data laptop yang sudah diurutkan berdasarkan jumlah dan nama: {laptop}')



# Membuat array menggunakan while
print("ini array data laptop menggunakan while")
i = 0
while i < len(laptop):
    print( laptop[i])
    i += 1
