
# for example, this code does an assertion on content of an element:

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://www.example.com')
element = browser.find_element_by_tag_name('h1')
assert element.text == 'Example Domains'
browser.quit()
# note this example is pure python with a bare assert. It is better to use a test framework like python's unittest, which has more powerful assertions.