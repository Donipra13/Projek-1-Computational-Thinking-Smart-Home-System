#Sistem Lightning Smart Home

import random
import time


#KAMUS
#ada_orang: string
#area_dalam: array of string
#area_luar: array of string

#waktu: string


area_dalam = ["Ruang Tamu", "Kamar Tidur", "Dapur"]
area_luar = ["Teras", "Taman", "Garasi"]

lampu_dalam = [False]*len(area_dalam)
lampu_luar = [False]*len(area_luar)

while True:
    
    print("=== 🌟 Smart Home Lighting System🌟 ===")
    print("1. Mode Otomatis (sensor & waktu)")
    print("2. Mode Manual (atur lampu)")
    print("3. Ganti Nama Ruangan")
    print("4. Lihat Status Lampu")
    print("5. Keluar")

    pilihan = input("Pilih menu (1/2/3/4/5): ").strip()

    #MODE OTOMATIS
    if pilihan == "1":
        waktu = input("\nMasukkan waktu (pagi/siang/sore/malam): ").strip().lower()
        while waktu not in["pagi", "siang", "sore", "malam"]:
            waktu = input("⚠️ Masukkan waktu yang valid (pagi/siang/sore/malam): ").strip().lower()
        
        print("───────────────────────────────────────────────────────────")
        print("🔎 Deteksi sensor pada area dalam rumah...")
        time.sleep(1)

        #area dalam rumah otomatis nyala & mati berdasarkan ada tidaknya orang
        for i in range(len(area_dalam)):
            ada_orang = random.choice([True, False])
            lampu_dalam[i] = ada_orang
            if ada_orang:
                print(f"[SYSTEM] Sensor di {area_dalam[i]}: TERDEKSI ORANG 🧍")

            else:
                print(f"[SYSTEM] Sensor di {area_dalam[i]}: TIDAK TERDEKSI ORANG 🚫  ")

        time.sleep(1)

        #area luar menyala atau mati berdasarkan waktu
        for i in range(len(area_luar)):
            lampu_luar[i] = (waktu == "malam")
            if lampu_luar[i]:
                print(f"[SYSTEM] {area_luar[i]}: LAMPU HIDUP ✅")

            else:
                print(f"[SYSTEM] {area_luar[i]}: LAMPU PADAM ❌")  
           

        print("──────────────────────────────────────────────────────────")
        print("--- 💡 Status Lampu Otomatis ---")
        print("🏠 Area Dalam Rumah:")
        for i in range(len(area_dalam)):
            if lampu_dalam[i]:
                print(f"   {area_dalam[i]}: HIDUP ✅")

            else:
                print(f"   {area_dalam[i]}: PADAM ❌")

        print("\n🌳 Area Luar Rumah:")
        for i in range(len(area_luar)):
            if lampu_luar[i]:
                print(f"   {area_luar[i]}: HIDUP ✅")

            else:
                print(f"   {area_luar[i]}: PADAM ❌")

        print("──────────────────────────────────────────────────────────")
    # MODE MANUAL
    elif pilihan == "2":
        print("──────────────────────────────────────────────────────────")
        print("--- Mode Manual ---")
        print("1. Atur lampu area dalam")
        print("2. Atur lampu area luar")
        sub_pilihan = input("Pilih area (1/2): ").strip()
        print("──────────────────────────────────────────────────────────")
        print("Status Lampu:")
        # Manual area dalam
        if sub_pilihan == "1":
            for i in range(len(area_dalam)):
                if lampu_dalam[i]:
                    print(f"{i+1}. {area_dalam[i]} (HIDUP)")

                else:
                    print(f"{i+1}. {area_dalam[i]} (PADAM)")
            try:
                pilih = int(input("Pilih nomor ruangan untuk ubah status: "))
                if 1 <= pilih <= len(area_dalam):
                    aksi = input("Hidupkan atau matikan lampu? (hidup/padam): ").strip().lower()
                    lampu_dalam[pilih - 1] = (aksi == "hidup")
                    if lampu_dalam[pilih - 1]:
                        print("──────────────────────────────────────────────────────────")
                        print(f"Lokasi: {area_dalam[pilih - 1]}")
                        print(f"💡 Status Lampu : HIDUP ✅")
                        print("──────────────────────────────────────────────────────────")
                    else:
                        print("──────────────────────────────────────────────────────────")
                        print(f"Lokasi: {area_dalam[pilih - 1]}")
                        print(f"💡 Status Lampu : PADAM ❌")
                        print("──────────────────────────────────────────────────────────")
                else:
                    print("⚠️ Nomor ruangan tidak valid.")
            except ValueError:
                print("⚠️ Harap masukkan angka yang benar.")

        # Manual area luar
        elif sub_pilihan == "2":
            for i in range(len(area_luar)):
                print(f"{i+1}. {area_luar[i]} ({'HIDUP' if lampu_luar[i] else 'PADAM'})")
            try:
                pilih = int(input("Pilih nomor ruangan untuk ubah status: "))
                if 1 <= pilih <= len(area_luar):
                    aksi = input("Hidupkan atau matikan lampu? (hidup/padam): ").strip().lower()
                    lampu_luar[pilih - 1] = (aksi == "hidup")
                    if lampu_luar[pilih - 1]:
                        print("──────────────────────────────────────────────────────────")
                        print(f"Lokasi: {area_luar[pilih - 1]}")
                        print(f"💡 Status Lampu : HIDUP ✅")
                        print("──────────────────────────────────────────────────────────")
                    else:
                        print("──────────────────────────────────────────────────────────")
                        print(f"Lokasi: {area_luar[pilih - 1]}")
                        print(f"💡 Status Lampu : PADAM ❌")
                        print("──────────────────────────────────────────────────────────")
                else:
                    print("⚠️ Nomor ruangan tidak valid.")
            except ValueError:
                print("⚠️ Harap masukkan angka yang benar.")

        else:
            print("⚠️ Pilihan area tidak valid!")

    # GANTI NAMA RUANGAN
    elif pilihan == "3":
        print("\n--- Ganti Nama Ruangan ---")
        print("1. Area Dalam Rumah")
        print("2. Area Luar Rumah")
        sub = input("Pilih area (1/2): ").strip()
        print()
        if sub == "1":
            for i in range(len(area_dalam)):
                print(f"{i+1}. {area_dalam[i]}")
            try:
                pilih = int(input("Pilih nomor ruangan untuk diubah: "))
                if 1 <= pilih <= len(area_dalam):
                    nama_baru = input("Masukkan nama baru: ").strip().title()
                    if nama_baru:
                        print(f"✅ {area_dalam[pilih - 1]} diganti menjadi {nama_baru}")
                        area_dalam[pilih - 1] = nama_baru
                else:
                    print("⚠️ Nomor tidak valid.")
            except ValueError:
                print("⚠️ Harap masukkan angka yang benar.")
        elif sub == "2":
            for i in range(len(area_luar)):
                print(f"{i+1}. {area_luar[i]}")
            try:
                pilih = int(input("Pilih nomor ruangan untuk diubah: "))
                if 1 <= pilih <= len(area_luar):
                    nama_baru = input("Masukkan nama baru: ").strip().title()
                    if nama_baru:
                        print("──────────────────────────────────────────────────────────")
                        print(f"✅ {area_luar[pilih - 1]} diganti menjadi {nama_baru}")
                        area_luar[pilih - 1] = nama_baru
                        print("──────────────────────────────────────────────────────────")
                else:
                    print("⚠️ Nomor tidak valid.")
            except ValueError:
                print("⚠️ Harap masukkan angka yang benar.")
        else:
            print("⚠️ Pilihan tidak valid!")

    #LIHAT STATUS
    elif pilihan == "4":
        print("──────────────────────────────────────────────────────────")
        print("--- 💡 Status Lampu Saat Ini ---")
        print("🏠 Area Dalam Rumah:")
        for i in range(len(area_dalam)):
            if lampu_dalam[i]:
                print(f"{area_dalam[i]}: HIDUP ✅")

            else:
                print(f"{area_dalam[i]}: PADAM ❌")

        print("\n🌳 Area Luar Rumah:")
        for i in range(len(area_luar)):
            if lampu_luar[i]:
                print(f"{area_luar[i]}: HIDUP ✅")

            else:
                print(f"{area_luar[i]}: PADAM ❌")
        print("──────────────────────────────────────────────────────────")

    # KELUAR
    elif pilihan == "5":
        print("\nTerima kasih telah menggunakan Smart Home Lighting System! 👋")
        break

    else:
        print("⚠️ Pilihan tidak valid. Silakan coba lagi.")

    time.sleep(1)