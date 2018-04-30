import urllib.request as rq

from posixpath import basename as bn
from urllib.parse import urlparse as pr

with open("file.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)

for x in array:
  print (x) # Just for debugging, to see if an URL pauses the process
  url = pr(x)
  print (bn(url.path)) # Just for debugging, to see the filename for the URL above
  rq.urlretrieve(x, bn(url.path))
