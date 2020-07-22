black='\e[0;30m'

blue='\e[0;34m'

green='\e[0;32m'

cyan='\e[0;36m'

red='\e[0;31m'

purple='\e[0;35m'

brown='\e[0;33m'

lightgray='\e[0;37m'

darkgray='\e[1;30m'

lightblue='\e[1;34m'

lightgreen='\e[1;32m'

lightcyan='\e[1;36m'

lightred='\e[1;31m'

lightpurple='\e[1;35m'

yellow='\e[1;33m'

white='\e[1;37m'

nc='\e[0m'

clear

figlet -f standard 'Termux'   # UBAH STRING TERMUX JADI NAMA KAMU

echo -ne "${red}Today is:\t\t${cyan}" `date`; echo ""

echo -e "${red}Kernel Information: \t${cyan}" `uname -smr`

echo -ne "${cyan}";upinfo;echo ""

echo -e "${cyan}"; cal -3

PS1='\n\n\[\e[41m\]\[\e[1;37m\] root \[\e[47m\]\[\e[1;30m\] \w \[\e[0m\]\[\e[1;37m\]\[\e[42m\] # \[\e[0m\] @ \[\e[41m\]\[\e[1;33m\]\h\[\033[0m\033[0;32m\] ─┤├─┼─┼─  \[\e[44m\]\[\e[1;37m\]\t \d\[\033[0;32m\] ─┤├─ \[\033[1;33m\]\[TERMUX\033[0;32m\] ─┤ \n\[\033[0;32m\]└┼─\[\033[0m\033[0;32m\]\$\[\033[0m\033[0;32m\]─┤▶\[\033[0m\] ' 
