import time     #untuk memberi jeda pada program & menampilkan waktu real time
import random   #untuk generate number
#KAMUS
#password: int
#door_locked: boolean
#sisa_percobaan: int
#deteksi_motion: array of boolean


password = 4325                                           # password untuk pintu
door_locked = True                                        # True = terkunci
sisa_percobaan = 3                                        # sisa percobaan tiap pintu
riwayat_aktivitas = []                                    # menyimpan riwayat aktivitas
deteksi_motion = [False, False, False, False, False]      # status deteksi gerak di area area tertentu (5 area)


# ALGORITMA
while True:
    #MAIN MENU
    print("=== SMART HOME SISTEM KEAMANAN ===")
    print("1. Buka kunci Pintu")
    print("2. Deteksi Pergerakan")
    print("3. Tampilkan Riwayat Aktivitas")
    print("4. Kunci Pintu")
    print("5. Exit")
    choice = input("Pilih opsi (1-4): ")

    #PILIHAN1
    if choice == "1":

        if not door_locked:
            print("───────────────────────────────────────────────────────────")
            print("Pintu tidak terkunci")
            print("───────────────────────────────────────────────────────────")
            time.sleep(1)
            continue

        for i in range(3):
            try:
                entered = int(input("Masukkan Password : "))
                if entered == password:
                    door_locked = False
                    sisa_percobaan= 3
                    
                    print("───────────────────────────────────────────────────────────")
                    print("[SYSTEM] Pintu sukses diunlock!")
                    print("───────────────────────────────────────────────────────────")
                    riwayat_aktivitas.append((time.ctime(),"Pintu","UNLOCKED: AKSES DITERIMA"))
                    break


                else:
                    sisa_percobaan -= 1
                    print(f"[ERROR] Password salah. Percobaan tersisa: {sisa_percobaan}\n")
                    riwayat_aktivitas.append((time.ctime(),"Pintu","LOCKED: AKSES DITOLAK"))

                    if sisa_percobaan<= 0:
                        #Menyalakan alarm jika password gagal terlalu banyak.
                        print("───────────────────────────────────────────────────────────")
                        print(f"[ALERT] ALARM DIAKTIFKAN! 🚨\n")
                        riwayat_aktivitas.append((time.ctime(), "Door","ALARM DIAKTIFKAN"))

                        for _ in range(3):
                            print("🚨 Alarm Berbunyi 🚨")
                            time.sleep(1)

                        print("[SYSTEM] Alarm Berhenti.")
                        sisa_percobaan = 3
                        print("───────────────────────────────────────────────────────────")
            except ValueError:
                sisa_percobaan -= 1
                print(f"Masukkan angka yang benar! Sisa percobaan: {sisa_percobaan}")
                


    #PILIHAN 2
    elif choice == "2":
        #Simulasi deteksi gerakan pada setiap sensor.
        print("───────────────────────────────────────────────────────────")
        print("=== MOTION DETECTION SYSTEM ===")

        for i in range(len(deteksi_motion)):

            # Simulasi apakah sensor mendeteksi gerakan
            deteksi_motion[i] = random.choice([True, False])
            if deteksi_motion[i] and door_locked:
                print(f"[ALERT] Ada aktivitas mencurigakan di area {i+1}⚠️")
                riwayat_aktivitas.append((time.ctime(), f"Area {i+1}","DETEKSI AKTIVITAS MENCURIGAKAN"))
            else:
                print(f"[INFO] Tidak ada aktivitas di area {i+1}.")
                riwayat_aktivitas.append((time.ctime(), f"Area {i+1}", "TIDAK ADA AKTIVITAS MENCURIGAKAN"))
        print("───────────────────────────────────────────────────────────")

    #PILIHAN3
    elif choice == "3":
        #Menampilkan riwayat aktivitas sistem.
        print("───────────────────────────────────────────────────────────")
        print("=== Riwayat Aktivitas ===")

        if not riwayat_aktivitas:
            print("Tidak ada riwayat aktivitas.")
            break

        for data in riwayat_aktivitas:
            print(f"{data[0]} | {data[1]} | {data[2]}")
        print("───────────────────────────────────────────────────────────")

    #PILIHAN4
    elif choice == "4":
        #Mengunci Pintu Melalui System
        print("───────────────────────────────────────────────────────────")
        if door_locked :
            print("Pintu sudah terkunci.")

        
        else:
            #Verifikasi kepada user untuk melakukan penguncian pintu
            print("[NOTIFIKASI] Apakah anda ingin mengunci pintu: ya / tidak")
            try:
                choice = input("Pilihan: ").strip().lower()
                
                if choice == "ya":
                    print("[SYSTEM] Mengunci Pintu.")
                    door_locked = True
                    riwayat_aktivitas.append((time.ctime(), "Pintu", "LOCKED"))
                elif choice == "tidak":
                    print("[INFO] Pintu tetap tidak dikunci.")
                else:
                    print("[ERROR] Pilihan tidak valid")
            except ValueError:
                print("[ERROR] Pilihan tidak valid")

        print("───────────────────────────────────────────────────────────")

            
    #PILIHAN5
    elif choice == "5":
        print("Exiting System")
        break

    else:
        print("[ERROR] Pilihan tidak valid.\n")

    time.sleep(1)
