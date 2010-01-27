from tumblr import Api
import sys

BLOG='latentflip.tumblr.com'
USER='phil@latentflip.com'
PASSWORD=raw_input('Password? ')

if len(sys.argv) != 3:
        print "Usage: tumbl <title> <body>"
        sys.exit(-1)    

title = sys.argv[1]
body = sys.argv[2]

api = Api(BLOG,USER,PASSWORD)
post = api.write_regular(title,body)
print "Published: ", post['url']