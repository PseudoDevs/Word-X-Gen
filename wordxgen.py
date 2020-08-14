#!/usr/bin/python
# Joshua Alcantara - IamPseudoX 
# Website : http://iampseudox.uk

import sys
import os
import itertools
import time


sudoColorGrey = '\033[40m'
sudoColorLightGrey = '\033[40m'
sudoSpammMessage = "\n\033[1;31;40m Sending Spam Mail to the Victim !.. \033[0m"
if len(sys.argv) < 2:
    os.system("cls||clear")
    sys.stdout.write(sudoColorGrey+"""         

██╗    ██╗ ██████╗ ██████╗ ██████╗      ██╗  ██╗      ██████╗ ███████╗███╗   ██╗
██║    ██║██╔═══██╗██╔══██╗██╔══██╗     ╚██╗██╔╝     ██╔════╝ ██╔════╝████╗  ██║
██║ █╗ ██║██║   ██║██████╔╝██║  ██║█████╗╚███╔╝█████╗██║  ███╗█████╗  ██╔██╗ ██║
██║███╗██║██║   ██║██╔══██╗██║  ██║╚════╝██╔██╗╚════╝██║   ██║██╔══╝  ██║╚██╗██║
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝     ██╔╝ ██╗     ╚██████╔╝███████╗██║ ╚████║
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚═╝  ╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝

    Created by Pseudo-X [ A WordList Generator for Windows / Linux / Termux ].

\n"""+sudoColorLightGrey)

else:
    sys.exit("Usage: python wordxgen.py")
    os.system("cls||clear")

print("\033[1;31;40m[ How to use in Windows / Linux / Termux : \033[1;33;40m python wordxgen.py \033[0m \033[1;31;40m]\033[0m \n") 

combination = input("Enter Word or Number to Generate the Combination : ")
minimumCharacters = int(input("Enter Minimun Number of Character: "))
maxCharacters = int(input("Enter Maximum Number of Character: "))
output = input("Enter FileName -> [ex: list.txt] : ")

fileWriteIT = open(output, 'wb')
timeS = time.localtime()
timerStart = time.time()
current_time = time.strftime("%H:%M:%S", timeS)

for i in range(minimumCharacters,maxCharacters + 1):
  r = 100 * i / maxCharacters
  l = "Progress : " + str(r) +' %'

  sys.stdout.write("\r%s" % l+ " Successfully Completed" )
  sys.stdout.flush()
  fileWriteIT.flush()

  for comb in itertools.product(combination, repeat = i):
    fileWriteIT = open(output, "a")
    fileWriteIT.write("".join(comb) + "\n")

endTime = time.time()
finished = endTime - timerStart

print("\033[1;31;40m \n --+[ Done ]+-- \033[1;33;40m")
print("\033[1;32;40m Finished : \033[0m"+ current_time)
print("\033[1;32;40m Time Consumed : \033[0m", finished, "sec")
print("\033[1;32;40m Filename is : \033[0m" + output)
print("\033[1;32;40m Location : \033[0m" +os.getcwd() + "/" + output)


fileWriteIT.flush()    
fileWriteIT.close()