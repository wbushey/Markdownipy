# Requires nltk and and punkt via nltk.download()

from sites_dict import sites
from lxml import html, etree
from Markdownipy import Markdownipy
import urllib

# Set our Unicode enconding of choice
UNICODE_ENCODING = 'utf-8'

    
# Simply fetches a webpage and returns the page as a utf-8 encoded unicode
#
# Input: A url 
# Output: A utf-8 unicode containing the fetched page
def fetch(url):
    if not isinstance(url, str):
        raise ValueError("Expecting str, received " + `type(key)`)
        
    # Need to set the agentString, as some sites get snotty with uncommon agents
    class CrawlrURLOpener(urllib.FancyURLopener):
        version = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1042.0 Safari/535.21"

    urllib._urlopen = CrawlrURLOpener()

    # Retreive and return the webpage
    try:
        socket = urllib.urlopen(url)
        tosDoc = socket.read()
        socket.close()
        return unicode(tosDoc, UNICODE_ENCODING)
    except IOError as e:
        print "Something went wrong with the tubes"

# Fetchs a url and translates a specific element into markdown
#
# url is an address of an HTML document
# xpath is an xpath string to a given element in the above HTML
# t is an instance of Markdownipy
def fetchAndProcess(url, xpath, t):
    tosHtml = fetch(url)      # Retrieve the string of HTMl that makes up the page
    tosDom = html.fromstring(tosHtml)    # Convert string of HTML into an lxml.html.HtmlElement
    xpathResults = tosDom.xpath(xpath )# Search for the element that contains text. The result of .xpath() is a list of lxml.html.HtmlElements

    # Ideally, there will only be one element that matches our xpath query. Thus, xpathResults should only have one element.
    divHTML = etree.tostring(xpathResults[0], encoding=unicode, method='html')
    md = t.translate(html.fromstring(divHTML))
    if isinstance(md, str):
        md = unicode(md, UNICODE_ENCODING)
    return md

t = Markdownipy(True,True)
