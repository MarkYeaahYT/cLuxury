from xlibluxuryx import *
import os
import time
BOLD = '\033[1m'
CEND = '\33[0m'
CSELECTED = '\33[7m'
WARNING = '\033[93m'
CWHITE2 = '\33[97m'
CRED2 = '\33[91m'
CGREEN2 = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2 = '\33[94m'
CVIOLET2 = '\33[95m'
CGREEN = '\33[32m'
CBEIGEBG = '\33[46m'
# waktu
def timex():
    t = time.localtime()
    hr = t.tm_hour
    mn = t.tm_min
    sc = t.tm_sec
    return '[{}:{}:{}] '.format(hr, mn, sc)


def logo():
    print CRED2+"\n     _ _  _        _               ___   ___"
    time.sleep(0.3)
    print CGREEN2+"  __| | || |  _ __| | ___ __ ___  / _ \ / _ \ _ __  ___"
    time.sleep(0.6)
    print CYELLOW2+" / _` | || |_| '__| |/ / '_ ` _ \| | | | | | | '_ \/ __|"
    time.sleep(0.9)
    print CBLUE2+"| (_| |__   _| |  |   <| | | | | | |_| | |_| | | | \__ \ "
    time.sleep(1)
    print CVIOLET2+" \__,_|  |_| |_|  |_|\_\_| |_| |_|\___/ \___/|_| |_|___/\n"+CEND
    time.sleep(1.5)
    print "|create by     : "+BOLD+CWHITE2+"d4rkm00ns"+CEND
    print "|contact person: "+BOLD+CWHITE2+"d4rkm00ns@protonmail.com"+CEND
    print "|date created  : 31 desember 2018"
    print "|date update   : 20 Januari 2019"
    print "|tools version : "+CBEIGEBG+"1.2 [ LUXURY Version ]"+CEND
    print "|what's new..? : - Update Domain"
    print "|Usage ?       : LifeTime"
    print "|tools for     : "+CSELECTED+"Email Valid Checker + Email Filter"+CEND
logo()
time.sleep(0.5)
# creating golder Result
try:
    if not os.path.exists('Result'):
        os.makedirs('./Result')
    else:
        print ""
except OSError:
    print ('Error: Creating directory')
    print "Buatlah folder Result"
finally:
    print "\t\t[^.^]-+ [d4rkm00ns] +-[^.^]"
print WARNING+"Note: Read 'PetunjukPenggunaan.txt' before using this Tools"+CEND
time.sleep(0.5)
print "List Tools ./d4rkm00ns"
#print "##_.~<-`+`-> $ [^.^] $ <-`+`->~._##\n"
print "##[^.^][^.^][^.^][^.^][^.^][^.^][^.^]##\n"
print CBLUE2+"[1]"+CEND+"Main Checker Valid Email"
print CBLUE2+"[2]"+CEND+"Custom Valid Email Server"
print CBLUE2+"[3]"+CEND+"Custom Filter Email"
print CRED2+"[0]"+CEND+"EXIT\n"
print "##[^.^][^.^][^.^][^.^][^.^][^.^][^.^]##"
#print "##_.~<-`+`-> $ [^.^] $ <-`+`->~._##\n"
print WARNING+"Copyright by d4rkm00ns. Please don't remove copyright"+CEND

# creating folder ResFiltered
try:
    if not os.path.exists('ResFiltered'):
        os.makedirs('./ResFiltered')
    else:
        print ""
except OSError:
    print ('Error: Creating directory')
    print "Buatlah folder ResFiltered"
finally:
    print "\t\t[^.^]-+ [Welcome to Undergrounds] +-[^.^]"

swit = input(timex()+BOLD+CWHITE2+"[+]Your Choose root@d4rkm00ns: "+CEND)
if swit == 1:
    print timex()+"[+]Set to Mail Checker"
    luxury(timex())
elif swit == 2:
    print timex()+"[+]Set to Custom Mail Checker"
    customserver(timex())
elif swit == 3:
    print timex()+"[+]Set to Custom Filter Email"
    customfilter(timex())
elif swit == 0:
    print timex() + "[!]Exit..!!"
    print timex() + "[+]See You Again..!!"
    print timex() + "[+]./d4rkm00ns"
    print CGREEN+"[^.^]-+ [Thanks Was using Tools ./d4rkm00ns] +-[^.^]" + CEND
    exit()
else:
    print timex()+WARNING+"Invalid Choosing"+CEND
print "\n\t\t"+CGREEN+"==--+ [Finished..!!] +--=="
print "[^.^] [Thanks Was using Tools ./d4rkm00ns] [^.^]"+CEND