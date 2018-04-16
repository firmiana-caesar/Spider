import urllib2
import sys
import string
import codecs
import re

defaultencoding = 'gb2312'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

class GetViewState:
    def __init__(self, url):
        self.url = url
        self.data = ''
        self.ViewState = ''

    def getPage(self):
        self.data = urllib2.urlopen(self.url)
        f = codecs.open('00001.html', 'w', 'gb2312')
        f.write(self.data)
        f.close()

    def getViewState(self):
        self.ViewState = re.findall('<input type="hidden" name="_VIEWSTATE" value=(.*?)/>', self.data, re.S)
        # myItems = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>', unicodePage, re.S)
        print(self.ViewState)


newurl = 'http://jxgl.cqu.edu.cn/_data/index_login.aspx'
mystate = GetViewState(newurl)
mystate.getPage()
mystate.getViewState()



