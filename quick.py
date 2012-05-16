from Markdownipy import Markdownipy
from lxml import html
dom = html.parse('samples/first_in_line_test.html')
body = dom.xpath('/html/body')[0]
t = Markdownipy(True, True)
