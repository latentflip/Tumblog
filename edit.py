#!/usr/bin/python
from tumblr import Api
import yaml
import sys

BLOG = 'latentflip.tumblr.com'
USER = 'phil@latentflip.com'
PASSWORD = raw_input('Password? ')
#PASSWORD = ''

if len(sys.argv) != 2:
	print "Usage: tumbl <file>"
	sys.exit(-1)

#Get the file and load the YAML
file = sys.argv[1]
infile = ''.join(open(file).readlines())
post = yaml.load(infile)

#Init the API
api = Api(BLOG,USER,PASSWORD)

type = post.pop('type')
if 'id' in post:
	post['post_id'] = post.pop('id')

no_html = ['title']
for k,v in post.items():
	if k not in no_html and hasattr(v, 'encode'):
		post[k] = v.encode('ascii', 'xmlcharrefreplace')

try:
	do_func = getattr(api, 'write_'+type)
except:
	print 'Type '+type+' is not supported.'
	
if do_func:
	saved_post = do_func(**post)

	if not 'post_id' in post:
		f = open(file, "r+")
		old = f.read() # read everything in the file
		f.seek(0) # rewind
		f.write("id: "+str(saved_post['id'])+"\n" + old) # write the new line before
	
	from pprint import pprint
	pprint(saved_post)

