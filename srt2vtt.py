#!/usr/bin/env python
import re, sys

if sys.argv[1] != "":
    subtitles = sys.argv[1]

    print "Converting subtitle to WebVTT"

    with open(subtitles, 'r') as srtfile:
       content = srtfile.read()
       content = re.sub(r'([\d]+)\,([\d]+)', r'\1.\2', content)
       subtitles = subtitles.replace('.srt', '.vtt')

       with open(subtitles, 'w') as vttfile:
           vttfile.write("WEBVTT\n\n" + content)
