import time

waktu = time.localtime()
waktu_spesifik = {"jam": waktu.tm_hour ,
                  "menit" : waktu.tm_min ,
                  "detik" : waktu.tm_sec
}

#waktu menurut deifinisi saya
#pagi jam 1 subuh sampai 5 masi malam
#jam 6 sampai 12 pagi
#jam 12 sampai 18 siang
#jam 18 sampai 24 malam


x = int(waktu_spesifik["jam"]) #1-24

if x <= 5 or x >= 19:               #dibawah 12:00 wita
    print("malam lek")

elif x >= 12:            
    print("sudah siang")

elif x >= 6:            #dibawah 18:00 wita
    print("pagi lek")

