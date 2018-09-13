#!/usr/bin/env python
from selenium import webdriver
import sys
import warnings

print ("""\

 +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
 |A|u|t|o|m|a|t|i|c| |S|c|r|e|e|n| |G|e|n|e|r|a|t|o|r|
 +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
 |b|y| |A|k|1|t|4|
 +-+-+ +-+-+-+-+-+


usage: ./simpleshot.py 'domains-urls.txt' 'path/bin/phantomjs'

Warning: this is a really ugly script (im not coder) but works like a charm :)

@akita_zen

""")


print ""
print ""

warnings.simplefilter("ignore")
with open(sys.argv[1]) as f:
        for line in f:
                line2 = line.rstrip()
                url_domain = 'http://' + line2 + '/'
                url_domain_secure = 'https://'+line2+'/'
                print "URL:" + str(url_domain)
                print ""
                driver = webdriver.PhantomJS(sys.argv[2])
                driver.set_window_size(480, 320)
                print ""
                print "[Taking screenshot of site...]"
                driver.get(url_domain)
                screenshot = driver.save_screenshot( line2 + '.png')
                print "[OK]"
                print ""
                line3 = line2 + '.png'
                driver.get(url_domain_secure)
                screenshot2 = driver.save_screenshot(line2+'s'+'.png')
                print "[OK]"
