import hashlib
import sys
import os
import time
import urllib2
import urllib 
import re

def main():
    os.system("clear")
    print ("MD5 and SHA1 ENCRYTION AND DECRYTION SCRIPT"); print
    print ('1 - ENCRYTION USING MD5 AND SHA1')
    print ('2 - MD5 DECRYTION')
    select = input("select option :")    
    if select == 1:
        encrytion()
    elif select == 2:
        decrytion()
 
def encrytion():
    os.system("clear")
    print ("MD5 and SHA1 ENCRYTION SCRIPT"); print
    print ('1 - ENCRYTION USING MD5')
    print ('2 - ENCRYTION USING SHA1')
    select = input("select option :")
 
    
    if select == 1:
        md5encrytion()
    elif select == 2:
        sha1encrytion()
 
 
def md5encrytion():
    os.system("clear")
    string=raw_input("string you want to convert to MD5 >")
    algorithim=hashlib.md5()
    algorithim.update(string)
    encrypted=algorithim.hexdigest()
    print('%s to MD5 hash %s' %(string,encrypted))
    mainmenu=raw_input("Press [ENTER] to go to main menu.")
    main()
 
def sha1encrytion():
    os.system("clear")
    string=raw_input("string you want to convert to SHA1 > ")
    algorithim=hashlib.sha1()
    algorithim.update(string)
    encrypted=algorithim.hexdigest()
    print('%s to MD5 hash %s' %(string,encrypted))
    mainmenu=raw_input("Press [ENTER] to go to main menu.")
    main()
def decrytion():
    os.system("clear")
    print ("MD5 DECRYTION"); print
    print ('1 - MD5 ONLINE DECRYTION ')
    print ('2 - MD5 OFFLINE DECRYTION ')
    select = input("select option :")
 
    if select == 1:
        md5onlinedecrytion()
    elif select == 2:
        md5offlinedecrytion()
 
def md5onlinedecrytion():
    os.system("clear")
    string=raw_input("paste MD5 Hash > ")
    website = 'http://md5decryption.com/'
    weburl = urllib.urlencode({'hash':string,'submit':'Decrypt+It!'})
    req = urllib2.Request(website)
    try:
          fd = urllib2.urlopen(req, weburl)
          data = fd.read()
          match = re.search(r'(Decrypted Text: </b>)(.+[^>])(</font><br/><center>)', data)
          if match: print ('[-] site: %s\t\t\tPassword: %s' % (website, match.group(2)))
          else: print ('[-] site: %s\t\t\tPassword: Not found' % website)
    except urllib2.URLError: print ('[+] site: %s \t\t\t[+] Error: seems to be down' % website)

def md5offlinedecrytion():
    os.system("clear")
    counter = 0
    lines = 0
    string=raw_input("paste MD5 Hash > ")
    wordList = raw_input("Dictionary path > ")
    try:
        wordlistfile = open(wordList)
        for line in open(wordList):
            lines += 1
    except IoError:
        print('Dictionary is not valid')
        raw_input("Press [ENTER] to try Again")     
        main()
    else:
        pass
    for line in wordlistfile:
        algorithim = hashlib.md5()
        line = line.replace("\n","")
        algorithim.update(line)
        wordlistdecrypted = algorithim.hexdigest()
        counter += 1
        percentage_raw = float(counter) / float(lines) * 100
        percentage_raw ="%.0f" % percentage_raw; percentage = str(percentage_raw) + " " + "%"
        os.system("clear")
        print(percentage)
        if wordlistdecrypted == string:
            print('Hash Crackrd - %s' % line)
            mainmenu= raw_input("Press [ENTER] to go to main menu")
            main()
main()