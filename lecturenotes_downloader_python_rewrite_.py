import requests
import re
import urllib.request
import sys 
from tqdm import tqdm
import os  

#https://lecturenotes.in/uploads/upload/note/8d/8djmG7OoAg/22-5b1fbff199859ee950086584be28405c.jpeg
url = sys.argv[1] + "/"
#jpeg downloader
def dl_jpg(url,file_path,file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url,full_path)

if (len(sys.argv) != 2):
    print("Usage : lecturenotes.py <url>")
    quit()

if (not(os.path.isdir('./images/'))):
	os.mkdir('./images/')


#getting & searching totalpages(https://lecturenotes.in/notes/....../ is not working)
r = requests.get(url+'1')
res = r.text

totalpages = re.search(r'"numberOfPages":\s(\d+),',res)
print('Total Pages: ' + str(totalpages.group(1)) + '\n')

#initialize page counter
page=1

#loop 
with tqdm(total=int(totalpages.group(1))) as pbar:
  while(page<=int(totalpages.group(1))):
    #GETting and searching for jpeg url
    #print((requests.get(url +str(page))).text)
    jpg_url = re.findall(r'(/uploads/upload/note/\w+/\w+/[a-zA-Z0-9-]+\.(jpeg|jpg))',(requests.get(url +str(page))).text,)
    #temp = jpg_url[-1]
    #print(jpg_url)
    #print(temp)
    #calling downloader
    dl_jpg('https://lecturenotes.in'+str(jpg_url[-1][0]), './images/' , str(page))
    
    #debug
    #print(page)
    #print(jpg_url[-1][0])
    page = page + 1
    pbar.update(1)

