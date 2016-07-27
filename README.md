# kcet_bot

A simple bot created using [Selenium](http://www.seleniumhq.org/download/) to scrape cet rankings for the [kcet results website](http://karresults.nic.in/indexcet2016.asp)

You can use Firefox or Chrome to run the bot.
**Note**: Since selenium doesn't support the latest verison of ffox, you must use ffox ver 45.2.
... Simply download the req. version and link the directory
'''python
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

ffox = FirefoxBinary('/home/kashyap/myprograms/firefox45/firefox')
browser = webdriver.Firefox(firefox_binary=ffox)
'''