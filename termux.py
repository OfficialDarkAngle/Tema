#!usr/bin/python

#author noiz

import os

import sys

import time

w = "\033[90;1m"

m = "\033[91;1m"

h = "\033[92;1m"

k = "\033[93;1m"

b = "\033[94;1m"

p = "\033[95;1m"

a = "\033[96;1m"

s = "\033[97;1m"

def noiz(x):

    w = {'w':90, 'm':31, 'h':32, 'k':33, 'b':34, 'p':35, 'a':96, 's':97}

    for i in w:

        x = x.replace('\r%s'%i, '\033[%s;1m'%w[i])

    x += '\033[0m'

    x = x.replace('\r0','\033[0m')

    print (x)

#os.system('pkg install ruby cowsay toilet figlet')

#os.system('gem install lolcat')

def runntxt(lolz):

    for noobs in lolz:

        sys.stdout.write(noobs)

        sys.stdout.flush()

        time.sleep(10. / 100)

def banner():

    os.system("clear")

    runntxt(h+"     Assalamu'alaikum       .")

    os.system('python banner.py')

def main():

    banner()

    print a+",~~~~~",h+"[",s+" Pilih Opsinya ",h+"]"

    pilih = input("\033[96m'~~~~~>   ")

    if pilih == 1:

        pertama()

        runntxt(w+"...................")

        print " "

        os.system('cowsay -f eyes "termux" | lolcat')

        os.system('toilet -f standard "termux" -F gay')

        runntxt(h+"         S u c c s e s s ...")

        print "  "

        runntxt(a+" Silahkan buka jendela termux baru")

        print " "

        print " "

    elif pilih == 2:

        print w+'sedang proses.......'

        time.sleep(1)

        noobs()

    elif pilih == 3:

        install()

    elif pilih == 4:

        keluar()

    else:

        main2()

def main2():

    os.system("clear")

    print """

\033[91;1m           TOOLS EDIT TERMUX KEREN

\033[94;1m+---------------------------------------------+              

\033[92;1m|  Author: Noiz ID

\033[92;1m|  Team  : PARANOID CYBER

\033[94;1m|   +-----------------------------------------+

\033[91;1m|   | [1]  Ubah termux kamu sekarang          |

\033[91;1m|   | [2]  Cara Mengedit                      |              

\033[91;1m|   | [3]  Install paketnya dulu bos....      |

+---------------------------------------------+

\033[91;1m    4. Exit"""                                               

    print a+",~~~~~",h+"[",s+" Pilih Opsinya ",h+"]"

    pilih = input("\033[96m'~~~~~>   ")

    if pilih == 1:

        pertama()

        runntxt(w+"...................")

        print " "

        os.system('cowsay -f eyes "termux" | lolcat')

        os.system('toilet -f standard "termux" -F gay')

        runntxt(h+"         S u c c s e s s ...")

        print "  "

        runntxt(a+" Silahkan buka jendela termux baru")

        print " "

        print " "

    elif pilih == 2:

        print w+'sedang proses.......'

        time.sleep(1)

        noobs()

    elif pilih == 3:

        install()

    elif pilih == 4:

        keluar()

    else:

        main2()

def pertama():

    os.system('rm $HOME/../usr/etc/bash.bashrc')

    os.system('cp -f bash.bashrc $HOME/../usr/etc')

    os.system('clear')

    print w+"sedang proses....."

def install():

    os.system('pkg install ruby cowsay toilet figlet')

    os.system('gem install lolcat')

    main2()

def keluar():

    sys.exit()

def noobs():

    print a+'''

  CARA EDIT SCRIPT BASH.BASHRC

\033[97m

   Ganti string yg bertuliskan

"\033[91mtermux\033[97m" dengan nama kamu

atau dengan kata-kata lain yang kamu inginkan

jangan ubah string selain yg bertuliskan "\033[91mtermux\033[97m",

dikhawatirkan program menjadi error...

kecuali anda memang sudah paham pemrograman shell

jika sudah di edit, tinggal save dengan cara tekan

tombol \033[95mCTRL + X + Y + ENTER

\033[90m

                 Powered by: Noiz ID

'''

    lol = raw_input('\033[92;1m  E D I T  S E K A R A N G ?\033[91m  [ Y / N ]: ')

    if lol == 'y' or lol == 'Y':

        os.system('pkg install nano')

        os.system('nano bash.bashrc')

        main2()

    else:

        main2()

if __name__ == '__main__':

    main()
