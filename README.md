# kcet_bot

A simple bot created using [```Selenium```](http://www.seleniumhq.org/download/) to scrape cet rankings for the [kcet results website](http://karresults.nic.in/indexcet2016.asp)

You can use Firefox or Chrome to run the bot.

**Note**: Since selenium doesn't support the latest verison of ffox, you must use ffox ver 45.2.

Simply download the req. version and link the directory

```python
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

ffox = FirefoxBinary('/home/kashyap/myprograms/firefox45/firefox')
browser = webdriver.Firefox(firefox_binary=ffox)
```
Things that I had to check while doing this:  
* Verifying the proper version of ffox  
* Check if the computer is connected to network  
* To do this I used ```requests``` and tried to connect to [google](www.google.com)

To find the particular object I used ```.find_element_by_class_name()``` and ```.send_keys() ``` to send keys and ```.click() ``` to perform a mouse click.

Finally entered the record scraped by ```Selenium Webdriver``` to a csv file by importing it.

**Modules used**:  
1. ```selenium```  
2. ```csv```  
3. ```requests```  
4. ```time``` (*for noting certain times*)
