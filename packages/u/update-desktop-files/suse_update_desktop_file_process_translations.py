#!/usr/bin/python3

import sys

file = sys.argv[1]
po_raw = open(file + '-downstream-translated-raw.desktop', 'r')
po_clean = open(file + '-downstream-translated.desktop', 'w')
lines = po_raw.readlines()

items = dict()
name_processing = False
genericname_processing = False
comment_processing = False
keywords_processing = False
for line in lines:
	if ( name_processing and not (line.startswith("Name[") or\
	                              line.startswith("Name="))) or\
	   ( genericname_processing and not (line.startswith("GenericName[") or\
	                                     line.startswith("GenericName="))) or\
	   ( comment_processing and not (line.startswith("Comment[") or\
	                                 line.startswith("Comment="))) or\
	   ( keywords_processing and not (line.startswith("Keywords[") or\
	                                  line.startswith("Keywords="))):
		name_processing = False
		genericname_processing = False
		comment_processing = False
		keywords_processing = False
		for item in sorted(items):
			po_clean.write(items[item])
		items = dict()
	# Why lang = "AAAA"? Untranslated string is supposed to be first,
	# but not all desktop files conform to this conventions. Expect it
	# anywhere, but move it to the beginning of the list.
	if line.startswith("Name["):
		name_processing = True
		lang = line[5:line.find(']')]
		items[lang] = line
	elif line.startswith("Name="):
		name_processing = True
		lang = "AAAA"
		items[lang] = line
	elif line.startswith("GenericName["):
		genericname_processing = True
		lang = line[12:line.find(']')]
		items[lang] = line
	elif line.startswith("GenericName="):
		genericname_processing = True
		lang = "AAAA"
		items[lang] = line
	elif line.startswith("Comment["):
		comment_processing = True
		lang = line[8:line.find(']')]
		items[lang] = line
	elif line.startswith("Comment="):
		comment_processing = True
		lang = "AAAA"
		items[lang] = line
	elif line.startswith("Keywords["):
		keywords_processing = True
		lang = line[9:line.find(']')]
		items[lang] = line
	elif line.startswith("Keywords="):
		keywords_processing = True
		lang = "AAAA"
		items[lang] = line
	else:
		po_clean.write(line)
