#!/usr/bin/python

# icalfetcher.py: fetch an iCalendar file, turn it into a JSON file.
# Copyright (C) 2010 Casey Marshall.
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
import icalendar
import urllib2
import urlparse

def event2dict(event):
	d = {}
	for k in event.keys():
		if k == 'DTSTART':
			d['begins'] = str(event[k])
		if k == 'SUMMARY':
			d['summary'] = str(event[k])
		if k == 'LOCATION':
			d['location'] = str(event[k])
		if k == 'DESCRIPTION':
			d['description'] = str(event[k])
	return d

def cal2dict(cal):
	d = {}
	for k in cal.keys():
		if k == 'X-WR-CALNAME':
			d['name'] = str(cal[k])
	d['events'] = map(lambda (e): event2dict(e), cal.subcomponents)
	return d

def main(argv):
	if len(argv) < 2:
		print "usage: icalfetcher.py URL [output.json]"
		return 1
	url = argv[1]
	u = urlparse.urlparse(url)
	if len(argv) >= 3:
		outfile = argv[2]
	else:
		outfile = u.netloc + ".json"
	req = urllib2.urlopen(url)
	ical = req.read()
	cal = icalendar.Calendar.from_string(ical)
	d = cal2dict(cal)
	d['source'] = url
	d['format'] = 'ical'
	f = open(outfile, 'w')
	json.dump(d, f)
	f.close()
	return 0
	
if __name__ == "__main__":
	sys.exit(main(sys.argv))
