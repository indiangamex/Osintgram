import time
from selenium import webdriver
import keyboard
import requests
import getpass
usr_id = input("enter the insta username of that person : ")
usr = input("enter your id : ")
while True:
    passwd = getpass.getpass(prompt="enter your passwd : ")
    sure = input("sure your password is correct[Y/n] : ")
    if sure == "Y" or "y":
        break
    elif sure == "N" or "n":
        continue
lnk = "https://www.instagram.com/{}/".format(usr_id)
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_name("username").send_keys(usr)
driver.find_element_by_name("password").send_keys(passwd)
keyboard.press_and_release("enter")
time.sleep(4)
driver.get(lnk)
time.sleep(2)
driver.minimize_window()
def posts():
    driver.maximize_window()
    feed = 0
    post = driver.find_elements_by_class_name('FFVAD')
    for x in range(0, len(post)):
        if post[x].is_displayed():
            feed = feed + 1
            src_lnk = post[x].get_attribute("src")
            request = requests.get(src_lnk)
            with open("post-{}-{}.jpg".format(usr_id, feed), "wb") as f:
                f.write(request.content)
        if feed == 5:
            driver.minimize_window()
            break
def propic():
    driver.maximize_window()
    element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/div/div/span/img")
    pro_pic_lnk = element.get_attribute('src')
    request = requests.get(pro_pic_lnk)
    with open("profile-pic-{}.jpg".format(usr_id), "wb") as f:
        f.write(request.content)
    driver.minimize_window()
def bio():
    try:
        for elem in driver.find_elements_by_xpath("/html/body/div[1]/section/main/div/header/section/div[2]/span"):
            text = elem.text
            print(text)
    except:
        print("no bio or some internal error occured !")
def bio_txt():
    import  codecs
    try:
        for elem in driver.find_elements_by_xpath("/html/body/div[1]/section/main/div/header/section/div[2]/span"):
            text = elem.text
            with codecs.open("bio {}".format(usr_id), "w+", "utf-8") as f:
                f.write(text)
                f.close()
    except:
        print("some internal error occured !")
while True:
    print("Commands for the script\npropic -> to download the profile pic of the victim\nbio -> to download the bio of the victim\nfeed -> to download the bio of the victim in txt file\nexit -> to exit program")
    command = input("enter your command : ")
    if command == "bio":
        bio()

        yn = input("Do you wanna save it in a txt file(yes/no) : ")
        if yn == "yes":
            bio_txt()
            continue
        elif yn == "no":
            continue
    elif command == "feed":
        print("Initiated Default download(12)")
        posts()
    elif command == "propic":
        propic()
    elif command == "exit":
        driver.close()
        print("closing....")
        exit()
    else:
        print("you entered wrong command !!")













