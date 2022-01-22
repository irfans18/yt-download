''' 
=================
Author : irfans18
=================

install pafy
$ python3 -m pip install git+https://github.com/mps-youtube/pafy
install youtube_dl
$ pip3 install youtube_dl

create alias on mac / linux
$ alias qwe="path_to_python_bin/python3 download.py"

'''

import sys
import pafy
# import youtube_dl
# import argparse

# get url from argument
url = sys.argv[1]

video = pafy.new(url)
best = video.getbest()

# print info
print('url\t\t:', url)
print('title\t\t:', best.title + '.' + best.extension)
print('Resolution\t:', best.resolution)
print('likes\t\t:', video.likes)

# best.download()
best.download(filepath='/Users/macpro/Downloads/youtube/')
