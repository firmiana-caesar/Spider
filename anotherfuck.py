import urllib2, sys
import codecs

defaultencoding = 'gb2312'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

class Spider:
    def __init__(self,url):
        self.newurl = url
        print('init spider')

    def get_page(self):
        m = urllib2.urlopen(self.newurl).read()
        f = codecs.open('00001.html', 'w', 'gb2312')
        f.write(m)
        f.close()


new_url = 'http://jxgl.cqu.edu.cn/_data/index_login.aspx'
mySpider = Spider(new_url)
mySpider.get_page()

