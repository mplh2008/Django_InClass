from selenium import webdriver

#Sohail heard about a cool online app.
#He decided to check its homepage...
browser = webdriver.Firefox()

#He noticed a page title and header contained a to-do list
assert 'To-Do' in browser.title

#He is prompted for a to-do list

#He types "Buy more Jordans" into a test box

#He hits enter and the page updates
#"1: Buy more Jordans"

#There is an additional test box reqesting another item to add to the list

#He enters "Ask Danielle how the activity is going"(Sohail is very helpful XD)

#The page updates and shows bot items on his list

#He wonders if the list is saved, luckily he sees a text box that has a link to his generated list
#He happily saves the list and turns on the TV

browser.quit()