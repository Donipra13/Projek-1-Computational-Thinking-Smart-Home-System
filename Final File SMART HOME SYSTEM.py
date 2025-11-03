import time
import random
import os
#KAMUS
#password: int
#door_locked: boolean
#sisa_percobaan: int
#deteksi_motion: array of boolean
#data: array of string
#ada_orang: boolean
#area_dalam: array of string
#area_luar: array of string
#lampu_dalam: array of boolean
#lampu_luar: array of boolean
#waktu: string

#Inisialisasi data

#Security system
password = 4325                                           # password untuk pintu
door_locked = True                                        # True = terkunci
sisa_percobaan = 3                                        # sisa percobaan tiap pintu
riwayat_aktivitas = []                                    # menyimpan riwayat aktivitas
deteksi_motion = [False, False, False, False, False]      # status deteksi gerak di area area tertentu (5 area)


#Lighting System
area_dalam = ["Ruang Tamu", "Kamar Tidur", "Dapur"]
area_luar = ["Teras", "Taman", "Garasi"]

lampu_dalam = [False]*len(area_dalam)
lampu_luar = [False]*len(area_luar)



# SMART HOME MAIN MENU

while True:
    print("=== SMART HOME SYSTEM ===")
    print("1. Temperature Control")
    print("2. Lighting System")
    print("3. Security System")
    print("4. Exit")

    choice = input("Select option (1-4): ")
    if choice == "1":
        system = "Temperature System"
    elif choice == "2":
        system = "Lighting System"
    elif choice == "3":
        system = "Security System"

    if choice in ("1", "2", "3"):
        print(f"Memasuki {system}...")
        time.sleep(1)
        os.system('cls')
    if choice == "1":
        ###################################
        ####### ASUMSI KONDISI ############
        ###################################
        rho_udara = 1.2 #kg/m3...massa jenis udara
        volume = 300 #m3...volume ruangan
        c_udara = 718 #J/kg K...kalor jenis udara
        cop = 3.14 #...koefisien performa
        Q_masuk = 1400  #J...kalor yang masuk ke ruangan
        T_set = 24 #Celcius...temperatur setpoint
        offset = 2 #C...simpangan maksimum yang ditolerir sistem
        unit = ["[Celcius]","[Kelvin]","[Fahrenheit]","[Reamur]"] #...satuan suhu
        unit_opt = 1 #...satuan suhu bawaan
        menu_opt = 5 #...deklarasi variabel pilihan menu
        ac_on = False #...pada kondisi awal AC sedang mati
        fire = False #...pada kondisi awal tidak terdeteksi api 
        T_akt = False #...suhu aktual belum dideteksi
        daya = 0 #...besar daya kompresor pada kondisi awal

        persen = random.randrange(1,100)#########################
        if persen < 80 :######################################### MENDETEKSI
            T_aktual = random.randrange(150000,330000)/10000##### SUHU
        else :################################################### AKTUAL
            T_aktual = random.randrange(570000,750000)/10000#####

        while fire!=True:###program terus berjalan sampai user memilih keluar atau terdeteksi api
            T = [T_aktual for i in range(1,2)] #deklarasi variabel array suhu
            old_unit = unit[unit_opt-1] #menyimpan data satuan suhu yang dipakai di variabel old_unit

            print("===========SISTEM TEMPERATUR===========")##################
            print("koefisien performa :",cop)#################################
            print("temperatur setpoint :",int(T_set*10000)/10000, old_unit)### TAMPILAN
            print("offset :",int(offset*10000)/10000,old_unit)################ MENU
            print("temperatur aktual :",T[0],old_unit)########################
            print("konsumsi daya :",daya,"kWh")###############################

            ###################################################################################
            ################ jika terdeteksi api, program akan memberi alert ##################
            ###################################################################################
            if (T[0] > 57 and old_unit==unit[0]) or (T[0] > 330 and old_unit==unit[1]) or (T[0] > 134.6 and old_unit==unit[2]) or (T[0] > 45.6 and old_unit==unit[3] ):
                os.system('cls')
                print("API TERDETEKSI !!!")
                fire=True
                print("[System] Alarm diaktifkan 🚨")
                time.sleep(1)
                print("[System] Sprinkler diaktifkan 💧")
            ###################################################################################
            ############### jika tidak terdeteksi api, program akan menampilkan menu ##########
            ###################################################################################
            else :
                print("1. Atur satuan", old_unit)
                print("2. Atur offset [",int(offset*10000)/10000,"]")
                print("3. Kontrol temperatur dan pantau konsumsi daya")
                print("4. Keluar")
                menu_opt = int(input("Pilih (1-4):"))
                
                if menu_opt!=4:
                    os.system('cls')

            ###################################################################################
            ######################### KONVERSI SUHU ###########################################
            ###################################################################################
            if menu_opt == 1:
                # tampilkan pilihan satuan suhu yang diinginkan user
                print("Satuan :")
                print("1. Celcius")
                print("2. Kelvin")
                print("3. Fahrenheit")
                print("4. Reamur")
                unit_opt = int(input("Pilih (1-4):"))
                if old_unit==unit[0] : # dari Celcius
                    if unit_opt == 2 : # ke Kelvin
                        T_set+=273
                        T_aktual+=273
                    elif unit_opt ==3: #ke Fahrenheit
                        c_udara /=1.8
                        T_set=T_set*1.8 + 32
                        T_aktual=T_aktual*1.8 + 32
                        offset *=1.8
                    elif unit_opt==4: #ke Reamur
                        c_udara /=0.8
                        T_set*=0.8
                        T_aktual*=0.8
                        offset*=0.8
                elif old_unit==unit[1] : #dari Kelvin
                    if unit_opt == 1 : #ke Celcius
                        T_set-=273
                        T_aktual-=273
                    elif unit_opt == 3: #ke Fahrenheut
                        c_udara /=1.8
                        T_set=(T_set-273)*1.8 + 32
                        T_aktual=(T_aktual-273)*1.8 + 32
                        offset*=1.8
                    elif unit_opt == 4: #ke Reamur
                        c_udara /=0.8
                        T_set = (T_set-273)*0.8
                        T_aktual = (T_aktual-273)*0.8
                        offset*=0.8
                elif old_unit==unit[2] : #dari Fahrenheit
                    if unit_opt == 1 : #ke Celcius
                        T_set=(T_set-32)/1.8
                        T_aktual=(T_aktual-32)/1.8
                        c_udara*=1.8
                        offset/=1.8
                    elif unit_opt == 2 : #ke Kelvin
                        T_set=(T_set-32)/1.8 +273
                        T_aktual=(T_aktual-32)/1.8 +273
                        c_udara*=1.8
                        offset/=1.8
                    elif unit_opt == 4 : #ke Reamur
                        T_set=(T_set-32)*4/9
                        T_aktual=(T_aktual-32)*4/9
                        c_udara=c_udara*9/4
                        offset*=(4/9)
                elif old_unit==unit[3] : #dari Reamur
                    if unit_opt == 1 : #ke Celcius
                        T_set/=0.8
                        T_aktual/=0.8
                        c_udara*=0.8
                        offset/=0.8
                    elif unit_opt == 2 : #ke Kelvin
                        T_set=T_set/0.8 + 273
                        T_aktual=T_aktual/0.8 + 273
                        c_udara*=0.8
                        offset/=0.8
                    elif unit_opt == 3 : #ke Fahrenheit
                        T_set=T_set*9/4 + 32
                        T_aktual=T_aktual*9/4 + 32
                        offset*=(9/4)
                        c_udara/=(9/4)
                old_unit=unit[unit_opt-1] #simpan satuan suhu yang baru
                print("[SYSTEM] Pergantian Unit Suhu...")

            #########################################################################
            #################### ATUR OFFSET ########################################
            #########################################################################
            if menu_opt ==2:
                quest ="Masukkan nilai offset "+old_unit+" :"
                offset=float(input(quest))

            #########################################################################
            ####################### KONTROL SUHU ####################################
            #########################################################################
            if menu_opt == 3 :
                h = int(input("Durasi Pengontrolan (menit) :")) #berapa lama ingin suhu dikontrol
                intrvl = int(input("Interval Pemantauan (menit) :")) #setiap berapa menit suhu dipantau
                for i in range(0,h*60): 
                    if T[i] > T_set+offset: #jika simpangan suhu diatas offset
                        ac_on = True #AC menyala
                    elif T[i] < T_set-offset: #jika simpangan suhu dibawah offset
                        ac_on = False #AC dimatikan
                    p_comp = ac_on and 1500 or not ac_on and 0 #nilai daya kompresor
                    Q_ac = p_comp*cop #menghitung kalor yang diterima AC
                    delta_T = (Q_masuk-Q_ac)/(rho_udara*volume*c_udara) #menghitung selisih suhu akibat kalor Q_ac
                    T_new=(T[i] + delta_T) #menghitung nilai suhu yang baru
                    T = T + [T_new] #menambahkan data suhu yang baru pada array suhu
                    if i%(intrvl*60)==1 : #tampilkan data suhu dan daya pada interval yang sudah ditentukan
                        print ("Temperatur di menit ke-",(i-1)/60,":",T[i],old_unit)
                        print("Konsumsi daya di menit ke-",(i-1)/60,":",p_comp,"Watt")
                    daya+=p_comp/(1000*3600) #akumulasi daya
                    time.sleep(0.03)
                T_aktual = T[h*60-1] #memperbaharui data suhu aktual
            
            if menu_opt == 4:
                print("Exiting Temperature System...")
                time.sleep(2)
                os.system('cls')
                break
            time.sleep(3)
            os.system('cls')
            

    elif choice == "2":
        while True:
    
            print("=== 🌟 Smart Home Lighting System🌟 ===")
            print("1. Mode Otomatis")
            print("2. Mode Manual")
            print("3. Ganti Nama Ruangan")
            print("4. Lihat Status Lampu")
            print("5. Keluar")

            pilihan = input("Pilih menu (1/2/3/4/5): ").strip()
            if pilihan in("1","2","3","4"):
                os.system('cls')
            #MODE OTOMATIS
            if pilihan == "1":
                waktu = input("\nMasukkan waktu (pagi/siang/sore/malam): ").strip().lower()
                while waktu not in["pagi", "siang", "sore", "malam"]:
                    waktu = input("⚠️  Masukkan waktu yang valid (pagi/siang/sore/malam): ").strip().lower()
                
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
                time.sleep(1)

                print("──────────────────────────────────────────────────────────")
                print("--- 💡 Status Lampu Otomatis ---")
                print("🏠 Area Dalam Rumah:")
                for i in range(len(area_dalam)):
                    if lampu_dalam[i]:
                        print(f"   {area_dalam[i]}: HIDUP ✅")

                    else:
                        print(f"   {area_dalam[i]}: PADAM ❌")
                time.sleep(1)
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
                            aksi = input("Hidupkan atau padamkan lampu? (hidup/padam): ").strip().lower()
                            if(aksi == "hidup"):
                                lampu_dalam[pilih-1] = True
                            elif aksi == "padam":
                                lampu_dalam[pilih-1] = False

                            else:
                                print("──────────────────────────────────────────────────────────")
                                print("Pilihan tidak valid. Keluar Menu")
                                print("──────────────────────────────────────────────────────────")
                                time.sleep(1)
                                continue
                                
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
                            aksi = input("Hidupkan atau padamkan lampu? (hidup/padam): ").strip().lower()
                            if(aksi == "hidup"):
                                lampu_luar[pilih-1] = True
                            elif aksi == "padam":
                                lampu_luar[pilih-1] = False

                            else:
                                print("──────────────────────────────────────────────────────────")
                                print("Pilihan tidak valid. Keluar Menu")
                                print("──────────────────────────────────────────────────────────")
                                time.sleep(1)
                                continue
                                
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
                print("──────────────────────────────────────────────────────────")
                if sub == "1":
                    for i in range(len(area_dalam)):
                        print(f"{i+1}. {area_dalam[i]}")
                    try:
                        pilih = int(input("Pilih nomor ruangan untuk diubah: "))
                        if 1 <= pilih <= len(area_dalam):
                            nama_baru = input("Masukkan nama baru: ").strip().title()
                            if nama_baru:
                                print("──────────────────────────────────────────────────────────")
                                print(f"✅ {area_dalam[pilih - 1]} diganti menjadi {nama_baru}")
                                area_dalam[pilih - 1] = nama_baru
                                print("──────────────────────────────────────────────────────────")
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
                print("Exiting Lighting System...")
                time.sleep(1)
                os.system('cls')
                break

            else:
                print("⚠️ Pilihan tidak valid. Silakan coba lagi.")

            time.sleep(1)

    elif choice == "3":

        while True:
            #MAIN MENU
            print("=== SMART HOME SECURITY SYSTEM ===")
            print("1. Buka kunci Pintu")
            print("2. Deteksi Pergerakan")
            print("3. Tampilkan Riwayat Aktivitas")
            print("4. Kunci Pintu")
            print("5. Exit")
            choice = input("Pilih opsi (1-4): ")
            if choice in("1","2","3","4"):
                os.system('cls')

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

                    except ValueError:
                        sisa_percobaan -= 1
                        print(f"Masukkan angka yang benar! Sisa percobaan: {sisa_percobaan}")
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
                        


            #PILIHAN 2
            elif choice == "2":
                #Simulasi deteksi gerakan pada setiap sensor.
                print("───────────────────────────────────────────────────────────")
                print("=== MOTION DETECTION SYSTEM ===")

                for i in range(len(deteksi_motion)):
                    time.sleep(1)
                    # Simulasi apakah sensor mendeteksi gerakan
                    deteksi_motion[i] = random.choice([True, False])
                    if deteksi_motion[i]:
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
                    print("───────────────────────────────────────────────────────────")
                    continue

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
                print("Exiting Security System...")
                time.sleep(1)
                os.system('cls')
                break

            else:
                print("[ERROR] Pilihan tidak valid.\n")

            time.sleep(1)



    elif choice == "4":
        print("Exiting Smart Home System...")
        time.sleep(1)
        break

    else:
        print("Pilihan tidak valid!\n")
