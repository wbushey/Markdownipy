from Markdownipy import Markdownipy
from lxml import html
dom = html.parse('samples/unittest.html')
xpr = dom.xpath('/html/body/div[2]/div/div/div/div/div[7]/p/span')[0]
t = Markdownipy(True, True)
