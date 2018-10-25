import random
import urllib2
from bs4 import BeautifulSoup
import re
import os
import datetime

print("[%s] Starting execution..." % datetime.datetime.now())

# Randomize the page number for the url of the image webpage
page_nr = random.randint(1,16)
url = "https://www.spacetelescope.org/images/archive/wallpapers/page/%d/" % page_nr

print("[%s] Fetching images..." % datetime.datetime.now())
# Page contains a script in which all the attributes of the images are listed in a Javascript array (only script in page)
page = BeautifulSoup(urllib2.urlopen(url), features="lxml")
images_as_string = str(page.find('script'))

print("[%s] Fetching ids..." % datetime.datetime.now())
# Now pick up all the image ids:s from the array that's in string format
ids = []
for row in images_as_string.split("\n"):
    if "id:" in row:
        id = re.search("'(.*)'", row).group(1)
        ids.append(id)

print("[%s] Randomizing id..." % datetime.datetime.now())
# Randomize an id from the list and fill it in to the url
random_id = ids[random.randint(0, len(ids))]

image_url = "https://cdn.spacetelescope.org/archives/images/large/%s.jpg" % random_id

print("[%s] Setting the new wallpaper with the url %s..." % (datetime.datetime.now(), image_url))
# Set the new wallpaper
os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-uri %s' % image_url)

print("[%s] Execution complete!" % datetime.datetime.now())
