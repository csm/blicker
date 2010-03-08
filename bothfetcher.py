#!/usr/bin/python

# bothfetcher.py: fetches concert info for Bottom of the Hill, SF.
# Copyright (C) 2010 Casey Marshall
#
# Permission to use, copy, modify, distribute, and sell this software and its
# documentation for any purpose is hereby granted without fee, provided that
# the above copyright notice appear in all copies and that both that
# copyright notice and this permission notice appear in supporting
# documentation.  No representations are made about the suitability of this
# software for any purpose.  It is provided "as is" without express or 
# implied warranty.

import sys
import json
import urllib2
import HTMLParser

url = 'http://www.bottomofthehill.com/calendar.html'
outfile = 'www.bottomofthehill.com.json'

class MyParser (HTMLParser):
	

def main(argv):
	return 0
	
if __name__ == '__main__':
	sys.exit(main(sys.argv))
