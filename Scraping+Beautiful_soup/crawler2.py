from bs4 import BeautifulSoup
import requests
import json
import hashlib
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.request import urlopen
import hashlib
import calendar
import requests
import sys
import concurrent.futures
import time
import os

urls = []
# File you want to extract
with open("part1") as f:
    content = f.readlines()
urls = [x.strip() for x in content]
all_data = []

# Already extracted URLS

# Retrieve a single page and report the url and contents


def load_url(url):
    r = requests.get(url, headers={'Connection': 'close'}, timeout=10)
    return r.content


file="A_output"
filename=file+"json"
i = 0
count = 0
start = time.time()

## http://masnun.com/2016/03/29/python-a-quick-introduction-to-the-concurrent-futures-module.html
# Using 20 workers was the sweet spot on the low-RAM host I used, but you
# should tweak this
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        # Start the load operations and mark each future with its URL
    url_future = {executor.submit(load_url, link): link for link in urls}
    for future in concurrent.futures.as_completed(url_future):
        this_id = url_future[future][0]
        try:
           # print(url_future[future],"\n\n\n")
            url = url_future[future]
            response = future.result()
            soup = BeautifulSoup(response, "lxml")

        # Loop through all URLS ans extarct
            data = {}

            md5_id = hashlib.md5(url.encode('utf-8')).hexdigest()

            time = datetime.utcnow()
            unixtime = calendar.timegm(time.utctimetuple())
            last_crawled = datetime.utcfromtimestamp(
                (unixtime)).isoformat()+"Z"

            if "pdf" in url or "404" in url or ".js" in url or ".css" in url:
                data["url"] = url
                data["id"] = md5_id
                data["title"] = ""
                data["body"] = ""
                data["description"] = ""
                data["keywords"] = ""
                data["last_crawled"] = last_crawled
                continue

            # Extract Body

            body = " ".join([soup.find_all('p')[count].get_text()
                             for count in range(1, len(soup.find_all('p')))])
            body = (" ".join(body.split()))

            md5_id = hashlib.md5(url.encode('utf-8')).hexdigest()

            # Extract Title
            if soup.title:
                title = soup.title.string
            else:
                title = []

            # time
            time = datetime.utcnow()
            unixtime = calendar.timegm(time.utctimetuple())

            last_crawled = datetime.utcfromtimestamp(
                (unixtime)).isoformat()+"Z"

            # Extract Description
            if soup.select('meta[name="description"]'):
                description = soup.select('meta[name="description"]')[
                    0].attrs['content']
            else:
                description = []

            # Extract Keywords
            if soup.select('meta[name="keywords"]'):
                keywords = soup.select('meta[name="keywords"]')[
                    0].attrs['content']
                keywords = "".join(keywords)
            else:
                keywords = []

            # Clean fields of stray line breakers
            for character in ["\r", "\n", "\xa0", "\t"]:
                if character in body:
                    body = body.replace(character, "")
                if character in title:
                    title = title.replace(character, "")

            body = ' '.join(body.split())

            count=count+1
            print(count)
            data["url"] = url
            data["id"] = md5_id
            data["title"] = title
            data["body"] = body
            data["description"] = description
            data["keywords"] = keywords
            data["last_crawled"] = last_crawled
            all_data=[]
            all_data.append(data)

            #sys.stdout.write("Completed link {} with title {}\r".format(i, title))
            sys.stdout.flush()
            with open('PART1', 'a') as f:
              json.dump(all_data, f)
              f.write(os.linesep)
        except Exception as ex:
            title = ''
            content = ''
            i = i + 1
            print(ex)

            # Print out things so you know what's going on behind the scenes
   #     sys.stdout.write("Completed link {} with title {}\r".format(i,title))
        sys.stdout.flush()

    runtime = float(time.time()) - float(start)
    sys.stdout.write(
        "took {} seconds or {} links per second".format(runtime, 100/runtime))


