#scrape the flipkart website using selenium and beautifulsoup and store the results in a csv file
import csv
import bs4 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#function to extract the name of the product
def extract_name():
    names=[]
    tag=bs.select('._4rR01T')#select all the  elements that use a CSS class attribute named _4rR01T
    for i in range(len(tag)):
     names.append( tag[i].getText()) # getText() on the element returns the element’s text
    
    return names
#function to extract the current price of the product
def extract_price():
    price=[]
    tag=bs.select('._30jeq3._1_WHN1')#select all the  elements that use a CSS class attribute named _30jeq3._1_WHN1
    for i in range(len(tag)):
     price.append( tag[i].getText().split('₹')[1])#tag[i].getText() returns the price in ₹.... format .Inorder to get only the amount use split()
     
    
    return price

#function to extract the old price of the product
def extract_oldPrice():
    old_price=[]
    tag=bs.select('._3I9_wc._27UcVY')#select all the  elements that use a CSS class attribute named _3I9_wc._27UcVY
    for i in range(len(tag)):
     old_price.append( tag[i].getText().split('₹')[1])#tag[i].getText() returns the price in ₹.... format .Inorder to get only the amount use split()
    return old_price

#function to extract the old price of the product
def extract_discount():    
    discount=[]
    tag=bs.select('._3Ay6Sb')#select all the  elements that use a CSS class attribute named _3Ay6Sb
    
    for i in range(len(tag)):
     discount.append( tag[i].getText())# tag[i].getText() returns the text present in the tag
    return discount

#function to extract the rating of the product
def extract_rating():    
    rating=[]
    tag=bs.select('._3LWZlK')#select all the  elements that use a CSS class attribute named _3LWZlK
    
    for i in range(len(tag)):
     rating.append( tag[i].getText())# tag[i].getText() returns the text present in the tag
    return rating

search_term=input('Enter the term to be searched')#get the search term from user
search_term='+'.join(search_term.split())#the general format for a search term having more than 1 word is word1+word2

#launch chrome browser with selenium
browser=webdriver.Chrome()
browser.get('https://www.flipkart.com/search?q='+search_term)



bs=bs4.BeautifulSoup(browser.page_source)
#lists to store the names,prices,dicount percentage,ratings
names=[]
prices=[]
old_prices=[]
discounts=[]
ratings=[]

#select all the elements under span which is directly within  div tag with CSS class attribute _2MImiq 
elem2=bs.select('div[class=_2MImiq] >span') 

pages=elem2[0].getText().split()[3]#returns total number of pages in the search result

#for loop to extract all the necessary details from the search results
try: 
 for i in range(int(pages)):  
  bs=bs4.BeautifulSoup(browser.page_source)
  names=names+extract_name() #append the name list with product names
  prices=prices+extract_price() #append the prices list with product prices
  old_prices=old_prices+extract_oldPrice() #append the old_prices list with product old_prices
  discounts=discounts+extract_discount() #append the discount list with product discounts
  ratings=ratings+extract_rating() #append the ratings list with product ratings
  elem=browser.find_element_by_link_text('NEXT') 
  elem.click() #to move to next search page result
except:
  print('EOF')#executed on reaching the last page of the search result


 



#open a csv file to stored all the scraped data
file=open("output.csv","wt",newline="")
writer=csv.writer(file)
#first row
writer.writerow(['Title','Price','Price before discount','Discount','Rating'])
#for loop to insert all the scraped values into the csv file
for i in range(len(old_prices)): 

    writer.writerow([names[i],prices[i],old_prices[i],discounts[i],ratings[i]])

file.close() #close the csv file





    
 
