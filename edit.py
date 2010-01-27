from tumblr import Api
import sys

BLOG='latentflip.tumblr.com'
USER='phil@latentflip.com'
PASSWORD=raw_input('Password? ')

if len(sys.argv) != 2:
        print "Usage: tumbl <file>"
        sys.exit(-1)    

file = sys.argv[1]

infile = open(file).readlines()

post_id = int(infile[0])
title = infile[1]
slug = infile[2]
text = '\n'.join(infile[3:])

#Ignore the slug
api = Api(BLOG,USER,PASSWORD)
post = api.write_regular(post_id=post_id,body=text,title=title)