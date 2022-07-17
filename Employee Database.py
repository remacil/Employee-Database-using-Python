#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Data Karyawan Perusahaan

data=[{"NIK":"K01","Nama":"Randy","Gender":"Pria","Umur":26,"Jabatan":"Direktur"},
     {"NIK":"K02","Nama":"Nana","Gender":"Wanita","Umur":23,"Jabatan":"Wakil"}]  

def showData():
    print('''NIK\t\t|Nama\t\t|Gender\t\t|Umur\t\t|Jabatan\n''')
    for x in range(len(data)):
        print("{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}\n".format(data[x]["NIK"],data[x]["Nama"],data[x]["Gender"],data[x]["Umur"],data[x]["Jabatan"]))
    
def welcome():
    print('''
======Data Record=====
1. Report Data Karyawan
2. Menambahkan Data Karyawan
3. Mengubah Data Karyawan
4. Menghapus Data Karyawan
5. Exit''')

def report():
    while True:
        print('''
*** Report Data Karyawan***
1. Report Seluruh Data
2. Report Data Tertentu
3. Kembali Ke Menu Utama''')
        reportNo=input("Silahkan Pilih Sub Menu Read Data [1-3] : ")
        if reportNo=="1":
            if data== []:
                print("Data belum tersedia")
                break
            else:
                showData()
        elif reportNo=="2":
            dataSpecific=input("Masukkan NIK : ")
            for a in range(len(data)):
                if dataSpecific in data[a]["NIK"]:
                    print('''NIK\t\t|Nama\t\t|Gender\t\t|Umur\t\t|Jabatan\n''')
                    print("{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}\n".format(data[a]["NIK"],data[a]["Nama"],data[a]["Gender"],data[a]["Umur"],data[a]["Jabatan"]))
                    break
                elif a==max(range(len(data))):
                    print("Tidak ada karyawan dengan NIK tersebut!!")
                    break
                else:
                    continue
        elif reportNo=="3":
            break
        else:
            continue
                    

                    
def addKaryawan():
    while True:
        print('''
+++++ Menambah Data Karyawan +++++
1. Tambah data Karyawan
2. Kembali ke menu utama''')
        chooseAdd=input("Silahkan Pilih Sub Menu Create Data [1-2] : ")
        if chooseAdd=="1":
            nik=input("Masukkan NIK : ")
            for a in range(len(data)):
                if data[a]["NIK"]==nik:
                    print("Data Sudah Ada")
                    break
                elif a==max(range(len(data))):
                    nama=input("Masukkan nama karyawan : ")
                    gender=input("Jenis kelamin karyawan : ")
                    umur=input("Masukkan umur karyawan : ")
                    jabatan=input("Masukkan jabatan karyawan : ")
                    while True:
                        askInput=input("Apakah data akan disimpan? (Y/N) : ")
                        if askInput=="Y" or askInput== "y":
                            data.append({"NIK":nik,"Nama":nama,"Gender":gender,"Umur":umur,"Jabatan":jabatan})
                            print("Data Tersimpan")
                            break
                        elif askInput=="N" or askInput== "n":
                            print("Data tidak tersimpan")
                            break
                        else:
                            continue
                else:
                    continue
                
                
        elif chooseAdd=="2":
            break
        else:
            continue
            
def updateData():
    while True:
        print('''
===== Mengubah data karyawan =====
1. Ubah data karyawan
2. Kembali ke menu utama''')
        chooseUpdate=input("Silahkan pilih sub menu Update Data [1-2] : ")
        if chooseUpdate=="1":
            showData()
            nik=input("Masukkan NIK yang ingin di update : ")
            for a in range(len(data)):
                if nik==data[a]["NIK"]:
                    print('''NIK\t\t|Nama\t\t|Gender\t\t|Umur\t\t|Jabatan\n''')
                    print("{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}\n".format(data[a]["NIK"],data[a]["Nama"],data[a]["Gender"],data[a]["Umur"],data[a]["Jabatan"]))    
                    while True:
                        askUpdate=input("Tekan 'Y' apabila ingin lanjut update data atau 'N' apabila ingin cancel update (Y/N) : ")
                        if askUpdate=="y"or askUpdate=="Y":
                            askUpdate2=input("Masukkan kolom yang ingin di edit : ")
                            if askUpdate2=="nama"or askUpdate2=="Nama":
                                nama=input("Masukkan nama baru : ")
                                while True:
                                    askUpdate3=input("Apakah data akan diupdate? (Y/N) : ")
                                    if askUpdate3=="y"or askUpdate3=="Y":
                                        data[a]["Nama"]=nama
                                        print("data berhasil di update!!")
                                        break
                                    elif askUpdate3=="n"or askUpdate3=="N":
                                        print("data tidak diupdate..")
                                        break
                                    else:
                                        continue
                            elif askUpdate2=="NIK"or askUpdate2=="NIK":
                                gender=input("Masukkan NIK Baru : ")
                                while True:
                                    askUpdate3=input("Apakah data akan diupdate? (Y/N) : ")
                                    if askUpdate3=="y"or askUpdate3=="Y":                                
                                        data[a]["NIK"]=gender
                                        print("data berhasil di update!!")
                                        break
                                    elif askUpdate3=="n"or askUpdate3=="N":
                                        print("data tidak diupdate..")
                                        break
                                    else:
                                        continue
                            elif askUpdate2=="gender"or askUpdate2=="Gender":
                                gender=input("Masukkan Gender Baru : ")
                                while True:
                                    askUpdate3=input("Apakah data akan diupdate? (Y/N) : ")
                                    if askUpdate3=="y"or askUpdate3=="Y":                                
                                        data[a]["Gender"]=gender
                                        print("data berhasil di update!!")
                                        break
                                    elif askUpdate3=="n"or askUpdate3=="N":
                                        print("data tidak diupdate..")
                                        break
                                    else:
                                        continue
                            elif askUpdate2=="umur"or askUpdate2=="Umur":
                                umur=int(input("Masukkan Umur Baru : "))
                                while True:
                                    askUpdate3=input("Apakah data akan diupdate? (Y/N) : ")
                                    if askUpdate3=="y"or askUpdate3=="Y":                                
                                        data[a]["Umur"]=umur
                                        print("data berhasil di update!!")
                                        break
                                    elif askUpdate3=="n"or askUpdate3=="N":
                                        print("data tidak diupdate..")
                                        break
                                    else:
                                        continue
                            elif askUpdate2=="Jabatan"or askUpdate2=="jabatan":
                                jabatan=input("Masukkan Jabatan baru : ")
                                while True:
                                    askUpdate3=input("Apakah data akan diupdate? (Y/N) : ")
                                    if askUpdate3=="y"or askUpdate3=="Y":                                
                                        data[a]["Jabatan"]=jabatan
                                        print("data berhasil di update!!")
                                        break
                                    elif askUpdate3=="n"or askUpdate3=="N":
                                        print("data tidak diupdate..")
                                        break
                                    else:
                                        continue
                            else:
                                print("Tidak ada kolom tersebut pada data karyawan!!")
                                break
                        elif askUpdate=="n"or askUpdate=="N":
                            break
                        else:
                            continue
                elif a==max(range(len(data))):
                    print("Tidak ada karyawan yang memiliki NIK tersebut")
                    break
                else:
                    continue
        elif chooseUpdate=="2":
            break
        else:
            continue

def deleteData():
    while True:
        print('''
===== Menghapus Data Karyawan =====
1. Hapus data Karyawan
2. Kembali ke menu utama''')
        hapus=input("Silahkan pilih sub menu Hapus Data [1-2] : ")
        if hapus=="1":
            showData()
            keyDel=input("Silahkan masukkan NIK yang ingin dihapus : ")
            for x in range(len(data)):
                if keyDel==data[x]["NIK"]:
                    while True:
                        askDelete=input("Apakah data akan dihapus? (Y/N) : ")
                        if askDelete=="y"or askDelete=="Y":
                            for x in range(len(data)):
                                if keyDel==data[x]["NIK"]:
                                    data.pop(x)
                                    print("Data telah dihapus..")
                                    break
                                else:
                                    continue
                            break
                        elif askDelete=="n"or askDelete=="N":
                            print("Data tidak dihapus..")
                            break
                        else:
                            continue     
                elif x==max(range(len(data))):
                    print("data tidak tersedia!!")
                    break
                else:
                    continue
        elif hapus=="2":
            break
        else:
            continue

while True:
    welcome() 
    opsi=input("Silahkan Pilih Main_Menu [1-5] : ")
    if opsi=="1":
        report()
    elif opsi=="2":
        addKaryawan()
    elif opsi=="3":
        updateData()
    elif opsi=="4":
        deleteData()
    elif opsi=="5":
        print("Thank you and good bye!!!")
        break   
    else:
        print("****Silahkan masukkan angka yang benar*****")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




