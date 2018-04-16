import urllib
import urllib2
import cookielib
import sys
import codecs

defaultencoding = 'gb2312'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

postdata = urllib.urlencode({
    '_VIEWSTATE':'',
    '_VIEWSTATEGENERATOR':'CAA0A5A7',
    'Sel_Type':'STU',
    'txt_dsdsdsdjkjkjc':'20151656',
    'txt_dsdfdfgfouyy':'',
    'txt_ysdsdsdskgf':'',
    'pcInfo':'',
    'typeName':'',
    'aerererdsdxcxdfgfg':'',
    'efdfdfuuyyuuckjg':'EA93D82F2D1BB860F9B7897728FF3A'
})




url = 'http://jxgl.cqu.edu.cn/_data/index_login.aspx'

result = opener.open(url, postdata)

headers = result.headers
if 'set-cookie' in headers:
    print headers['set-cookie']

data = result.read()
print data[:]

f = codecs.open('00001.html', 'w', 'gb2312')
f.write(data)
f.close()