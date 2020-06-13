from selenium import webdriver 
import time 

print("enter username") 
username = input() 

print("enter password") 
password = input() 

print("enter the url") 
url = input() 

def path(): 
	global chrome 
	#add your own PATH
	exe_path = "/Users/kimberlyzhu/Documents/InstagramLiker/chromedriver"
	if not exe_path:
		print("enter the driver path") 
		exe_path = input() 

	# starts a new chrome session 
	chrome = webdriver.Chrome(executable_path = exe_path)

def url_name(url): 
	# the web page opens up 
	chrome.get(url) 
	
	# webdriver will wait for 4 sec before throwing a 
	# NoSuchElement exception so that the element 
	# is detected and not skipped. 
	time.sleep(4) 

def login(username, your_password): 
	
	# # finds the login button 
	# log_but = chrome.find_element_by_class_name("L3NKy") 
	# time.sleep(2) 

	# # clicks the login button 
	# log_but.click()	 
	# time.sleep(4) 

	# finds the username box 
	usern = chrome.find_element_by_name("username")	 

	# sends the entered username 
	usern.send_keys(username) 

	# finds the password box 
	passw = chrome.find_element_by_name("password")	 

	# sends the entered password 
	passw.send_keys(your_password)	 

	# finds the login button 
	log_cl = chrome.find_element_by_class_name("L3NKy")	 
	log_cl.click() # clicks the login button 
	time.sleep(20) #to click away any notifications manually

def like_pic(): 
	
	# finds the first picture 
	pic = chrome.find_element_by_class_name("_8-yf5") 
	pic.click() # clicks on the first picture 

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

def continue_liking(): 
	index = 0
	while True:
	    #divs = chrome.find_elements_by_class_name("_8-yf5") 
	    #divs = chrome.find_elements_by_css_selector("[aria-label=Like]")
	    #divs = chrome.find_element_by_xpath("//div[@aria-label='Like']/div[@class='_8-yf']");
	    list1 = chrome.find_elements_by_css_selector("[aria-label=Like]")
	    list2 = chrome.find_elements_by_class_name("_8-yf5") 
	    divs = intersection(list1, list2)

	    try: 
	    	divs[index].click()
	    	time.sleep(2)
	    	print("liked" + str(index))
	    except IndexError:
	        break
	    index += 1



path() 
time.sleep(1) 

url_name(url) 

login(username, password) 

#first_picture() 
#like_pic() 

continue_liking() 
