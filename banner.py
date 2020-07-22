import os,sys,time,random

os.system("clear")

def mengetik(s):

    for c in s + '\n':

        sys.stdout.write(c)

        sys.stdout.flush()

        time.sleep(random.random() * 0.1)

mengetik('          \033[91;1mTOOLS EDIT TERMUX KEREN\n\033[94;1m+---------------------------------------------+\n\033[92;1m|  Author: Noiz ID\n|  Team  : PARANOID CYBER\n\033[94;1m|   +-----------------------------------------+\n\033[91;1m|   | [1]  Ubah termux kamu sekarang          |\n|   | [2]  Cara Mengedit                      |\n|   | [3]  Install paketnya dulu bos....      |\n\033[94;1m+---------------------------------------------+\n\033[91;1m     4. Exit')
