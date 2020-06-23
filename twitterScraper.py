import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

file = open("tempFile", 'w')

site = input("Please enter a Twitter URL associated with a twitter account: ")

if(site.find("twitter") != -1):
    print("Success.\n")
else:
    print("Error: Please enter a valid twitter address.")
    exit()

print("Please wait...")
driver = webdriver.Firefox()
driver.minimize_window()
driver.get(site)
time.sleep(5)

print("\nYou chose the account ", end = '')

nameString = ''
accountName = driver.title
for tempChar in accountName:
    if (tempChar == '/' or tempChar == '|'):
        print("\n")
        break
    else:
        print(tempChar, end = '')

for tempChar in accountName:
    if tempChar != " ":
        nameString += tempChar
    else:
        break

elem =  driver.find_element_by_css_selector("html")

keyword = input("Please enter a keyword: ")
tempWord = ''

numOfTweets = int(input("How many tweets do you want to search? "))
pgNum = numOfTweets / 14

for x in range(0, int(pgNum)):
    source = BeautifulSoup(driver.page_source, 'lxml')
    for multiTweet in source.find_all('div', class_= 'css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0'):
        for x in multiTweet.text:
            if((x != ' ') and (x != '\n') and x.isalpha()):
                tempWord += x
            else:
                if(tempWord.upper() == keyword.upper()):
                    file.write(multiTweet.text)
                    file.write("\n")
                    break
                tempWord = ''
        if multiTweet.find('\n\n'):
            print("memes")
    elem.send_keys(Keys.PAGE_DOWN)
    elem.send_keys(Keys.PAGE_DOWN)
    elem.send_keys(Keys.PAGE_DOWN)
    elem.send_keys(Keys.PAGE_DOWN)
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    print("Searching...")
driver.close()
file.close()

#file = open("tempFile", 'r+')

tempList = []
i = 0





print("Done.")

tweetList = []

file = open("tempFile", 'r')

for line in file:
    tweetList.append(line)

tweetList.sort()

file.close()

file = open("tweets.txt", 'w')


file.write("Here are all of " + nameString + "'s tweets that contain the keyword " "'" + keyword + "'\n")
file.write("____________________________________________________________\n\n")

lastLine = '!!!!!!!!!'

for x in tweetList:
    if x != lastLine:
        file.write(x)
        file.write("\n")
        lastLine = x
file.close()

#os.system("rm tempFile")
