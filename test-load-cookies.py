from urllib import request

from http import cookiejar
cj = cookiejar.MozillaCookieJar('cookies.txt')
cj.load()

# Fill in the following
ID = ''
url = 'http://www.youtube.com/get_video_info?video_id=' + ID

R = request.Request(url, headers={})
cj.add_cookie_header(R)
# WTF?? cookiejar's add_cookie_header only adds to unredirected_hdrs..
# What is unredirected_hdrs BTW?
# It is not used in the request..
# We manually add to the requesta header..
R.headers.update(R.unredirected_hdrs)

res = request.urlopen(R)
print(res.read())

