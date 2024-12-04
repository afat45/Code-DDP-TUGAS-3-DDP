#import yang dipakai------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from prettytable import PrettyTable
import time
import pwinput as pin
import random
import os
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#template design
def temp(text):
    print("-"*80)
    print(text)
    print("-"*80)

#visual gacha
def visual_gacha(i):
    print("----------------------------------------------------------------------------")
    print(f"|                               {i:<43}|")
    print("----------------------------------------------------------------------------")

#template clear
def clear():
    os.system("cls || clear")

#delay
def delay():
    time.sleep(1)

#error handling
error = [ValueError,SyntaxError,KeyboardInterrupt,EOFError,NameError,TypeError,IndexError,AttributeError,ZeroDivisionError,ImportError]

#vip
status = {"vip": False}

#waktu 
waktu = time.localtime()
waktu_spesifik = {"jam" : waktu.tm_hour,
                  "bahasa": ""}

waktu_x = int(waktu_spesifik["jam"]) 

if waktu_x <= 5 or waktu_x >= 19:               
    waktu_spesifik["bahasa"] = "MALAM"

elif waktu_x >= 12:            
    waktu_spesifik["bahasa"] = "SIANG"

elif waktu_x >= 6:           
    waktu_spesifik["bahasa"] = "PAGI"

#account
akun = {"akun_1": {"user_id":"user123","pass":"12345678"},
        "akun_2":{"user_id":"afatxd45","pass":"xd45"},
        "akun_3":{"user_id":"test123","pass":"test"}}

akun_vip = {"akun_vip1": {"user_id_vip":"uservip123","pass":"vip123"},
            "akun_vip2":{"user_id_vip":"kosong45","pass":"pass123"},
            "akun_vip3":{"user_id_vip":"test","pass":"test"}}

#mata uang
mata_uang = {"Rp":0,"diamond":0}

#voucher
voucher ={
    "lootbox 500":0,
    "lootbox 1000":0,
    "lootbox 2000":0
    }

#inventory
inventory = {
    "Flashbang": 0,
    "Smoke Granade": 0,
    "Granade": 0,
    "Molotov": 0,
    "Kevlar Vest":0,
    "Kevlar + Helmet": 0,
    "Zeus x27": 0,
    "Defuse_kit": 0,
    "Glock 18": 0,
    "Dual Berettas": 0,
    "P250": 0,
    "tec-9": 0,
    "Desert Eagle": 0,  
    "P2000": 0,
    "Five-Seven": 0,
    "Shotgun": 0,
    "xm1014": 0,
    "mp5-50": 0,
    "p90": 0,
    "mac-10": 0,
    "mp-9": 0,
    "Galil AR": 0,
    "AK-47": 0,
    "SSG 08": 0,
    "SG 553": 0,
    "Famas": 0,
    "M4A1-S": 0,
    "AUG": 0,
    "AWP": 0
}

#market senjata------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
utility = {
    "Flashbang": 200,
    "Smoke Granade": 300,
    "Granade": 300,
    "Molotov": 400,
}

market_pagi = {
    "Kevlar Vest":650,
    "Glock 18": 200,
    "Dual Berettas": 300,
    "P250": 300,
    "tec-9": 500,
    "Desert Eagle": 700,  
}

market_siang = {
    "Shotgun": 1050,
    "xm1014": 2050,
    "mp5-50": 1500,
    "p90": 2350,
    "mac-10": 1050,
}

market_malam = {
    "Galil AR": 1800,
    "AK-47": 2700,
    "SSG 08": 1700,
    "SG 553": 3000,
    "AWP": 4750
}

#tambahan market untuk vip

market_vip_pagi = {
    "Kevlar + Helmet": 1000,
    "Zeus x27": 200,
    "Defuse_kit": 400,
    "P2000": 200,
    "Five-Seven": 500
}

market_vip_siang = {
    "mp-9": 1250
}

market_vip_malam = {
    "Famas": 2050,
    "M4A1-S": 2000,
    "AUG": 3300
}

#tabel list------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def tabel_market(market):
    tabel = PrettyTable(["No", "Barang", "Harga ($)"])
    items_list =list(utility.items())  +  list(market.items())
    for i, (barang, harga) in enumerate(items_list, 1):
        tabel.add_row([i, barang, harga])
    print(tabel)
    return items_list

def tabel_market_vip(market,vip):
    tabel = PrettyTable(["No", "Barang", "Harga ($)"])
    items_list =list(utility.items())  +  list(market.items()) + list(vip.items())
    for i, (barang, harga) in enumerate(items_list, 1):
        tabel.add_row([i, barang, harga])
    print(tabel)
    return items_list

def tabel_akun():
    tabel = PrettyTable()
    tabel.field_names = ["USER ID","PASS"]
    tabel.add_row(["user123","12345678"])
    tabel.add_row(["afatxd45","xd45"])
    tabel.add_row(["test123","test"])
    return tabel
show_akun = tabel_akun()

def tabel_akun_vip():
    table = PrettyTable()
    table.field_names = ["USER ID","PASS"]
    table.add_row(["uservip123","vip123"])
    table.add_row(["kosong45","pass123"])
    table.add_row(["test","test"])
    return table
show_akun_vip = tabel_akun_vip()

def tabel_top_up():
    table = PrettyTable()
    table.field_names = ["NO","DIAMOND","HARGA (RP)"]
    table.add_row(["1","100","RP 15000"])
    table.add_row(["2","300","RP 40000"])
    table.add_row(["3","500","RP 60000"])
    table.add_row(["4","1000","RP 100000 (Best Seller)"])
    table.add_row(["5","2000","RP 175000"])
    table.add_row(["6","5000","RP 400000"])
    table.add_row(["7","10000","RP 750000 (50% OFF)"])
    return table
show_top_up = tabel_top_up()

def tabel_inventory():
    tabel = PrettyTable()
    tabel.field_names = ["Barang", "Jumlah"]
    for barang, jumlah in {**inventory}.items():
        tabel.add_row([barang, jumlah])
    print(tabel)


#menu------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def menu():
    clear()
    try:
        temp("""SELAMAT DATANG DI TOKO SENJATA 505
            
apa yang bisa kami bantu?
1.login
2.help
3.exit""")
        input_menu = int(input("pilihan: "))
        if input_menu == 1:
            login()
        elif input_menu == 2:
            help()
        elif input_menu == 3:
            clear()
            print("Sampai Jumpa ")
            delay()
            exit()
        else:
            print("pilihan anda tidak valid! ")
            delay()
            menu()
    except tuple(error):
        print("pilihan anda bukan angka")
        menu()

#help
def help():
    try:
        clear()
        temp(f"""anda bisa login terlebih dahulu, untuk melakukan transaski! 
akun yang tersedia: """)
        print(show_akun)
        temp("AKUN VIP")
        print(show_akun_vip)
        x = input("\nPRESS ENTER TO EXIT: ") 
        if not x:
            menu()
        else:
            menu()
    except tuple(error):
        print("apa yang anda lakukan! ")
        help()


#login
def login():                
    try:
        clear()
        temp("""Selamat Datang, Silahkan Login

ketik 0 jika ingin keluar""")
        id = input("Masukan ID: ")
        if id == "user123":
            template_pass("12345678")
        elif id == "afatxd45":
            template_pass("xd45")
        elif id == "test123":
            template_pass("test")
        elif id == "uservip123":
            status["vip"] = True
            template_pass("vip123")
        elif id == "kosong45":
            status["vip"] = True
            template_pass("pass123")   
        elif id == "test":
            status["vip"] = True
            template_pass("test")
        elif id == "0":
            menu()
        else:
            print("akun tidak ditemukan")
            delay()
            login()
    except tuple(error):
        print("Apa Yang Anda Lakukan! ")
        login()


def template_pass(password1):
    percobaan = 0
    while True:
        clear()
        try:
            if percobaan == 3:
                print("percobaan anda habis")
                delay()
                login()
            else:
                password = pin.pwinput("masukan password: ")
                if password == password1:
                    print("selamat datang di toko senjata 505")
                    delay()
                    menu_user()
                else:
                    percobaan += 1
                    print(f"password anda salah, anda mempunyai {3 - percobaan}x kesempatan lagi")
                    delay()
        except tuple(error):
            print("Password tidak valid")


#menu user------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def menu_user():
    try:
        clear()
        temp("TOKO SENJATA 505")
        temp("""1.Top Up
2.Beli Senjata
3.Gacha Senjata
4.Inventory
5.Log Out""")
        c = int(input("pilihan: "))
        if c == 1:
            top_up()
        elif c == 2:
            beli_senjata()
        elif c == 3:
            gacha_senjata()
        elif c == 4:
            inv()
        elif c == 5:
            status["vip"] = False
            mata_uang["diamond"] = 0
            mata_uang["Rp"] = 0
            for item in inventory:
                inventory[item] = 0
            menu()
        else:
            print("pilihan tidak valid")
            delay()
            menu_user()
    except tuple(error):
        print("pilihan tidak valid")
        menu_user()


#top up------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def top_up():
    try:
        clear()
        temp("PROMO GACOR AKHIR TAHUN 2024 DIAMOND")
        print(show_top_up)
        print(f"\nSaldo = RP {mata_uang["Rp"]:,}")
        print(f"Diamond = {mata_uang["diamond"]:,}")
        temp("""1.BELI DIAMOND
2.ISI SALDO
3.EXIT""")
        z = int(input("pilihan: "))
        if z == 1:
            beli_diamond()
        elif z == 2:
            isi_saldo()
        elif z == 3:
            menu_user()
        else:
            print("pilihan tidak valid")
            delay()
            top_up()
    except tuple(error):
        print("pilihan tidak valid")
        top_up()


def template_beli_diamond(diamond,harga):
    while True:
        try:
            clear()
            if mata_uang["Rp"] >= int(harga):
                cv = input(f"apakah anda yakin dengan RP {harga} = {diamond} DM ? (y/t): ").lower()
                if cv == "y":
                    mata_uang["Rp"] -= int(harga)
                    mata_uang["diamond"] += int(diamond)
                    print("transaksi berhasil")
                    delay()
                    beli_diamond()
                elif cv == "t":
                    beli_diamond()
                else:
                    print("Inputan tidak valid")
                    delay()
            else:
                print("uang anda tidak cukup untuk melakukan transaksi! ")
                delay()
                beli_diamond()
        except tuple(error):
            print("inputan tidak valid")


def beli_diamond():
    try:
        clear()
        temp(f"""BELI DIAMOND, PROMO AKHIR TAHUN 2024

Saldo = RP {mata_uang["Rp"]:,}        
Diamond = {mata_uang["diamond"]:,}

ketik 0 jika ingin keluar""")
        print(show_top_up) 
        k = int(input("\nPilih Nomor Untuk Top Up: "))
        if k < 0:
            print("nomor tidak bisa minus ")
            delay()
            beli_diamond()
        elif k == 0:
            top_up()
        elif k == 1:
            template_beli_diamond(100,15000)
        elif k == 2:
            template_beli_diamond(300,40000)
        elif k == 3:
            template_beli_diamond(500,60000)
        elif k == 4:
            template_beli_diamond(1000,100000)
        elif k == 5:
            template_beli_diamond(2000,175000)
        elif k == 6:
            template_beli_diamond(5000,400000)
        elif k == 7:
            template_beli_diamond(10000,750000)
        else:
            print("Inputan tidak valid")
            delay()
            beli_diamond()
    except tuple(error):
        print("Inputan tidak valid")
        beli_diamond()


def isi_saldo(): 
    try:
        clear()
        temp(f"""ISI SALDO 

Saldo = Rp {mata_uang["Rp"]:,}

ketik 0 jika Ingin Keluar""")
        i = int(input("\nMasukan Saldo (RP): "))
        if i < 0:
            print("saldo tidak bisa minus ")
            delay()
            isi_saldo()
        elif i == 0:
            top_up()
        elif i < 10000:
            print("Minimal Harus isi saldo sebesar RP 10000")
            delay()
            isi_saldo()
        elif i > 1000000000:
            print("Maksimal isi saldo sebesar RP 1,000,000,000 Atau 1 M")
            delay()
            isi_saldo()
        else:
            mata_uang["Rp"] += i
            print("saldo berhasil ditambahkan")
            delay()
            top_up()
    except tuple(error):
        print("Inputan tidak valid")
        isi_saldo()


#beli senjata------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def beli_senjata(): #belum selesai
    v = int(waktu_spesifik["jam"])
    try:
        if status["vip"] == False:
            if v <= 5 or v >= 19:               #waktu malam 19:00 wita - 05:59 wita
                beli_senjata_biasa(market_malam)
            elif v >= 12:                      #waktu siang 12:00 wita - 18:59 wita
                beli_senjata_biasa(market_siang)
            elif v >= 6:                       #waktu pagi 06:00 wita - 11:59 wita
                beli_senjata_biasa(market_pagi)

        elif status["vip"] == True:
            if v <= 5 or v >= 19:                                                  #waktu malam 19:00 wita - 05:59 wita
                beli_senjata_vip(market_malam,market_vip_malam)
            elif v >= 12:                                                          #waktu siang 12:00 wita - 18:59 wita
                beli_senjata_vip(market_siang,market_vip_siang)
            elif v >= 6:                                                           #waktu pagi 06:00 wita - 11:59 wita
                beli_senjata_vip(market_pagi,market_vip_pagi)

    except tuple(error):
        print("error 505")
        beli_senjata()
    

def beli_senjata_biasa(market):
    try:
        clear()
        temp(f"""SELAMAT DATANG DI MARKET {waktu_spesifik['bahasa']}, TOKO SENJATA 505

Voucher lootbox 500  = {voucher['lootbox 500']}
Voucher lootbox 1000 = {voucher['lootbox 1000']}
Voucher lootbox 2000 = {voucher['lootbox 2000']}

Diamond = {mata_uang['diamond']}""")
        items_list = tabel_market(market)
        temp("Ketik 0 jika ingin keluar.")

        po = int(input("\nPilih Nomor barang yang ingin dibeli: "))
        if po == 0:
            menu_user()
        elif 1 <= po <= len(items_list):
            barang, harga = items_list[po - 1]
            if mata_uang["diamond"] >= int(harga):
                print(f"Anda telah membeli {barang} seharga {harga} Diamond.")
                inventory[f"{barang}"] += 1
                mata_uang["diamond"] -= int(harga)
                if waktu_spesifik["bahasa"] == "MALAM":
                    voucher['lootbox 2000'] += 1
                elif waktu_spesifik["bahasa"] == "SIANG":
                    voucher['lootbox 1000'] += 1
                elif waktu_spesifik["bahasa"] == "PAGI":
                    voucher['lootbox 500'] += 1             
                delay()
                beli_senjata_biasa(market)
            else:
                print("Diamond anda tidak cukup")
                delay()
                beli_senjata_biasa(market)
        else:
            print("pilihan tidak valid")
            delay()
            beli_senjata_biasa(market)
    except tuple(error):
        print("Inputan tidak valid.")
        beli_senjata_biasa(market)


def beli_senjata_vip(market,vip):    
    try:
        clear()
        temp(f"""SELAMAT DATANG DI MARKET VIP {waktu_spesifik['bahasa']}, TOKO SENJATA 505

Voucher lootbox 500  = {voucher['lootbox 500']}
Voucher lootbox 1000 = {voucher['lootbox 1000']}
Voucher lootbox 2000 = {voucher['lootbox 2000']}

Diamond = {mata_uang['diamond']}""")
        items_list = tabel_market_vip(market,vip)
        temp("Ketik 0 jika ingin keluar.")

        po = int(input("\nPilih Nomor barang yang ingin dibeli: "))
        if po == 0:
            menu_user()
        elif 1 <= po <= len(items_list):
            barang, harga = items_list[po - 1]
            if mata_uang["diamond"] >= int(harga):
                print(f"Anda telah membeli {barang} seharga {harga} Diamond.")
                inventory[f"{barang}"] += 1
                mata_uang["diamond"] -= int(harga)
                if waktu_spesifik["bahasa"] == "MALAM":
                    voucher['lootbox 2000'] += 1
                elif waktu_spesifik["bahasa"] == "SIANG":
                    voucher['lootbox 1000'] += 1
                elif waktu_spesifik["bahasa"] == "PAGI":
                    voucher['lootbox 500'] += 1     
                delay()
                beli_senjata_vip(market,vip)
            else:
                print("Diamond anda tidak cukup")
                delay()
                beli_senjata_vip(market,vip)
        else:
            print("pilihan tidak valid")
            delay()
            beli_senjata_vip(market,vip)
    except tuple(error):
        print("Inputan tidak valid.")
        beli_senjata_vip(market,vip)


#gacha senjata------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def gacha_senjata(): 
    try:
        clear()
        temp(f"""selamat datang di gacha 505

Voucher lootbox 500  = {voucher['lootbox 500']}
Voucher lootbox 1000 = {voucher['lootbox 1000']}
Voucher lootbox 2000 = {voucher['lootbox 2000']}

Diamond = {mata_uang['diamond']}""")
        temp("""|----------LOOTBOX----------|
1.LootBox 500 Diamond
2.LootBOX 1000 Diamond
3.LootBox 2000 Diamond 
4.Exit """)
        bh = int(input("pilihan: "))

        if bh == 1:
            if mata_uang["diamond"] < 500:
                print("diamond anda tidak cukup")
                delay()
                gacha_senjata()
            else:
                template_voucher_gacha("lootbox 500",400,500,list(market_pagi.keys()),list(utility.keys()))

        elif bh == 2:
            if mata_uang["diamond"] < 1000:
                print("diamond anda tidak cukup")
                delay()
                gacha_senjata()
            else:
                template_voucher_gacha("lootbox 1000",800,1000,list(market_siang.keys()),[])

        elif bh == 3:
            if mata_uang["diamond"] < 2000:
                print("diamond anda tidak cukup")
                delay()
                gacha_senjata()
            else:
                template_voucher_gacha("lootbox 2000",1600,2000,list(market_malam.keys()),[])

        elif bh == 4:
            menu_user()
        else:
            print("Pilihan tidak valid")
            delay()
            gacha_senjata()
    except tuple(error):
        print("Inputan tidak valid")
        gacha_senjata()


def template_voucher_gacha(voucher_box,harga_potongan,harga,list_1,list_2):
    if voucher[f"{voucher_box}"] > 0:
        while True:
            try:
                x = input("apakah anda ingin menggunakan voucher? potongan 20% (y/t): ").lower()
                if x == "y":
                    mata_uang["diamond"] -= int(harga_potongan)
                    voucher[f"{voucher_box}"] -= 1
                    lootbox(list_1, list_2)
                elif x == "t":
                    mata_uang["diamond"] -= int(harga)
                    lootbox(list_1, list_2)
                else:
                    print("inputan tidak valid")
                    delay()
            except tuple(error):
                print("inputan tidak valid")
    else:
        mata_uang["diamond"] -= int(harga)
        lootbox(list_1,list_2)


def lootbox(satu,dua):
    try:
        clear()
        gacha = satu + dua
        for detik in range(15, 0, -1):
            i = random.choice(gacha)
            clear()
            visual_gacha(i)
            time.sleep(0.1)

        for detik in range(10, 0, -1):
            i = random.choice(gacha)
            clear()
            visual_gacha(i)
            time.sleep(0.2)

        for detik in range(5, 0, -1):
            i = random.choice(gacha)
            clear()
            visual_gacha(i)
            time.sleep(0.5)
        clear()
        print(f"selamat kamu mendapatkan {i}")
        inventory[f"{i}"] += 1
        delay()
        gacha_senjata()
    except tuple(error):
        print("Inputan tidak valid")


#inventory------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def inv(): 
    try:
        clear()
        temp(f"""INVENTORY

Voucher lootbox 500  = {voucher['lootbox 500']}
Voucher lootbox 1000 = {voucher['lootbox 1000']}
Voucher lootbox 2000 = {voucher['lootbox 2000']}

Diamond = {mata_uang['diamond']}""")
        tabel_inventory()
        ab = input("\nPRESS ENTER TO EXIT: ")
        if not ab:
            menu_user()
        else:
            menu_user()
    except tuple(error):
        menu_user()


#run command------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

menu()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------