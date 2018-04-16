import string, urllib2
import codecs
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


def baidu_tieba(url, beginpage, endpage):
    for i in range(beginpage, endpage+1):
        sName = string.zfill(i, 5) + '.html'
        print("downloading" + str(i) + "page and stored by named " + sName + ".......")
        f = codecs.open(sName, 'w', 'gbk')
        m = urllib2.urlopen(url + str(i)).read()
        f.write(m)
        f.close()


bdurl = 'http://tieba.baidu.com/p/2296017831?pn='
iPostbegin = 1
iPostend = 10

baidu_tieba(bdurl, iPostbegin, iPostend)