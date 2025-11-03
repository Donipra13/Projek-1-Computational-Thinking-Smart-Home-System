###################################
####### BAGIAN IMPORT #############
###################################
import time                     
import os                                 
import random
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

while menu_opt!=4 and fire!=True:###program terus berjalan sampai user memilih keluar atau terdeteksi api
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
    ###################################################################################
    ############### jika tidak terdeteksi api, program akan menampilkan menu ##########
    ###################################################################################
    else :
        print("1. Atur satuan", old_unit)
        print("2. Atur offset [",int(offset*10000)/10000,"]")
        print("3. Kontrol temperatur dan pantau konsumsi daya")
        print("4. Keluar")
        menu_opt = int(input("Pilih (1-4):"))
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
            time.sleep(0.1)
        T_aktual = T[h*60-1] #memperbaharui data suhu aktual
    time.sleep(2)
    os.system('cls')
        