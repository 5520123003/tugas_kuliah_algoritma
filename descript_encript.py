import string
abjad = string.printable

while True:
    def encript(pesan):
        global abjad

        key = int(input("[+] Masukkan key       : "))
        print('------------------------------------------------')

        cipher = ' ' # menampikan chiper encripsio sesuai kaidah chiper caesar

        for i in pesan:
            if i in abjad:
                k = abjad.find(i) # menampilkan variabel sebelumnya yang sudah dijadikan pemanggil
                k = (k + key) %100
                cipher = cipher + abjad[k]
            else:
                cipher = cipher + i
        return cipher

    def descript(cipher):
        global abjad
        key = int(input("[+] Masukkan key       : "))
        pesan = ' ' # menampilkan pesan descript sesuai kaidah chiper caesar
        for i in cipher:
            if i in cipher:
                k = abjad.find(i)
                k = (k - key) %100
                pesan = pesan + abjad[k]
            else:
                pesan = pesan + i
        return pesan

    if __name__ == '__main__':
        print('------------------------------------------------')
        print('|------------ 1194059 Ahmad Syaerozi------------')
        print('------------------------------------------------')

        option = int(input('1. encripsi\n2. Descripsi\npilihan option       : '))
        print('------------------------------------------------\n')
        if option == 1:
            pesan = input("[+] Masukkan Pesan (plaintxt)     : ")
            print('------------------------------------------------')
            print(f"[=] {encript(pesan)}")
            print('------------------------------------------------\n')
        elif option == 2:
            print('------------------------------------------------\n')
            cipher = input('[+] Masukkan pesan (chipertext)    : ')
            print('------------------------------------------------\n')
            print(f"[=] {descript(cipher)}")
            print('------------------------------------------------\n')
            if option == cipher:
                break
        else:
            print('------------------------------------------------\n')
            print('Masukkan 1 atau 2!!')
            print('------------------------------------------------\n')



























































































