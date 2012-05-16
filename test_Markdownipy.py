from Markdownipy import *
from lxml.html import fromstring
import unittest

# Tests
class TestMarkdownipy(unittest.TestCase):
    def setUp(self):
        self.t = Markdownipy(True,False)
        f = open('samples/first_in_line_test.html','r')
        self.sample = f.read()
        self.sample_dom = fromstring(self.sample)
        f.close()

    def test_is_first_in_line_html(self):
        print "Testing first in line check:"

        print "\tTesting a root element that has content...",
        el = self.sample_dom.xpath('/html/body')[0]
        err_msg = 'Error testing a root element that contains content'
        self.assertEqual(self.t.is_first_in_line_html(el), True, err_msg)
        print "OK"

        print "\tTesting a block level that contains content...",
        el = self.sample_dom.xpath('/html/body/span/a/b/h1')[0]
        err_msg = 'Error testing a block level that contains content'
        self.assertEqual(self.t.is_first_in_line_html(el), True, err_msg)
        print "OK"

        print "\tTesting a span that is the first content containing element of a div...",
        el = self.sample_dom.xpath('/html/body/div[2]/span[1]')[0]
        err_msg = 'Error testing a span with first content inside of a div'        
        self.assertEqual(self.t.is_first_in_line_html(el), True, err_msg)
        print "OK"

        print "\tTesting a div that does not contain text of its own...",
        el = self.sample_dom.xpath('/html/body/div[2]')[0]
        err_msg = 'Error testing a div that contains elements, but does not have content of its own.'
        self.assertEqual(self.t.is_first_in_line_html(el), False, err_msg)
        print "OK"

        print "\tTesting a span which contains the first content following a block level among its left cousins...",
        el = self.sample_dom.xpath('/html/body/span[1]/span')[0]
        err_msg = 'Error testing a span which contains the first content following a block level among its left cousins'
        self.assertEqual(self.t.is_first_in_line_html(el), True, err_msg)
        print "OK"
        
    def tearDown(self):
        pass
    def test_a_translator(self):
        print "Testing 'a' translator...",
        el = fromstring('<a href="http://www.friendlytos.org">Friendly ToS</a>')
        correct_response = '[Friendly ToS](http://www.friendlytos.org)'
        response = self.t.translate(el)
        err_msg = 'Links are not translating correctly\n'\
                    'Expected:\n' + correct_response + '\n---\n'\
                    'Recieved:\n' + response + "\n---"
        self.assertEqual(response, correct_response, err_msg)
        print "OK"
    def test_b_translator(self):
        print "Testing 'b' translator...",
        el = fromstring('<b>Text</b>')
        correct_response = '**Text**'
        response = self.t.translate(el)
        err_msg = 'Bolds are not translating correctly\n'\
                    'Expected:\n' + correct_response + '\n---\n'\
                    'Recieved:\n' + response + "\n---"
        self.assertEqual(response, correct_response, err_msg)
        print "OK"
    def test_br_translator(self):
        print "Testing 'br' translator...",
        el = fromstring('<br><br />')
        correct_response = '\n\n\n\n'
        response = self.t.translate(el)
        err_msg = 'Line breaks are not translating correctly\n'\
                    'Expected:\n' + correct_response + '\n---\n'\
                    'Recieved:\n' + response + "\n---"
        self.assertEqual(response, correct_response, err_msg)
        print "OK"
    def test_div_translator(self):
        print "Testing 'div' translator...",
        el = fromstring('<div>Text!</div>')
        correct_response = '\n\nText!\n\n'
        response = self.t.translate(el)
        err_msg = 'Divs are not translating correctly\n'\
                    'Expected:\n' + correct_response + '\n---\n'\
                    'Recieved:\n' + response + "\n---"
        self.assertEqual(response, correct_response, err_msg)
        print "OK"
    def test_em_translator(self):
        print "Testing 'em' translator...",
        el = fromstring('<em>Text</em>')
        correct_response = '*Text*'
        response = self.t.translate(el)
        err_msg = 'Emphases are not translating correctly\n'\
                    'Expected:\n' + correct_response + '\n---\n'\
                    'Recieved:\n' + response + "\n---"
        self.assertEqual(response, correct_response, err_msg)
        print "OK"
    def test_h_translators(self):
        print "Testing header translators"
        # Loop through <h[1:6]>
        for i in xrange(1, 7):
            print "\tTesting 'h" + `i` + "' translator...",
            el = fromstring('<h' + `i` + '>Heading</h' + `i` + '>')
            correct_response = '\n' + ('#' * i) + 'Heading' + '\n\n' 
            response = self.t.translate(el)
            err_msg = 'Level ' + `i` + ' headings are not translating correctly\n'\
                        'Expected:\n' + correct_response + '\n---\n'\
                        'Recieved:\n' + response + "\n---"
            self.assertEqual(response, correct_response, err_msg)
            print "OK"
    def test_i_translator(self):
        print "Testing 'i' translator...",
        el = fromstring('<i>Text</i>')
        correct_response = '*Text*'
        response = self.t.translate(el)
        err_msg = 'Italics are not translating correctly\n'\
                    'Expected:\n' + correct_response + '\n---\n'\
                    'Recieved:\n' + response + "\n---"
        self.assertEqual(response, correct_response, err_msg)
        print "OK"
    def test_img_translator(self):
        print "Testing 'img' translator...",
        el = fromstring('<img src="http://www.google.com/images/logos/logo.png" alt="Google!">')
        correct_response = '![Google!](http://www.google.com/images/logos/logo.png)'
        response = self.t.translate(el)
        err_msg = 'Images are not translating correctly\n'\
                    'Expected:\n' + correct_response + '\n---\n'\
                    'Recieved:\n' + response + "\n---"
        self.assertEqual(response, correct_response, err_msg)
        print "OK"
    def test_li_translator(self):
        print "Testing 'li' translator...",
        el = fromstring('<li>List Text</li>')
        correct_response = 'List Text\n'
        response = self.t.translate(el)
        err_msg = 'List items are not translating correctly\n'\
                    'Expected:\n' + correct_response + '\n---\n'\
                    'Recieved:\n' + response + "\n---"
        self.assertEqual(response, correct_response, err_msg)
        print "OK"
    def test_p_translator(self):
        print "Testing 'p' translator...",
        el = fromstring('<p>Text!</p>')
        correct_response = '\n\nText!\n\n'
        response = self.t.translate(el)
        err_msg = 'Paragraphs are not translating correctly\n'\
                    'Expected:\n' + correct_response + '\n---\n'\
                    'Recieved:\n' + response + "\n---"
        self.assertEqual(response, correct_response, err_msg)
        print "OK"
    def test_pre_translator(self):
        print "Testing 'pre' translator...",
        el = fromstring('<pre>This is\nsome preformated\ntext</pre>')
        correct_response = '    This is\n    some preformated\n    text\n\n'
        response = self.t.translate(el)
        err_msg = 'Preformated text is not translating correctly\n'\
                    'Expected:\n' + correct_response + '\n---\n'\
                    'Recieved:\n' + response + "\n---"
        self.assertEqual(response, correct_response, err_msg)
        print "OK"
    def test_span_translator(self):
        print "Testing 'span' translator...",
        el = fromstring('<span>Text</span>')
        correct_response = 'Text'
        response = self.t.translate(el)
        err_msg = 'Spans are not translating correctly\n'\
                    'Expected:\n' + correct_response + '\n---\n'\
                    'Recieved:\n' + response + "\n---"
        self.assertEqual(response, correct_response, err_msg)
        print "OK"
    def test_strong_translator(self):
        print "Testing 'strong' translator...",
        el = fromstring('<strong>Text</strong>')
        correct_response = '**Text**'
        response = self.t.translate(el)
        err_msg = 'Strongs are not translating correctly\n'\
                    'Expected:\n' + correct_response + '\n---\n'\
                    'Recieved:\n' + response + "\n---"
        self.assertEqual(response, correct_response, err_msg)
        print "OK"

    def test_ul_translator(self):
        print "Testing 'ul' translator",
        el = fromstring('<ul><li>This is</li>\n<li>a list</li><li>of elements</li></ul>')
        correct_response = '\n\n* This is\n* a list\n* of elements\n\n\n'
        response = self.t.translate(el)
        err_msg = 'Unordered lists are not translating correctly\n'\
                    'Expected:\n' + correct_response + '\n---\n'\
                    'Recieved:\n' + response + "\n---"
        self.assertEqual(response, correct_response, err_msg)
        print "OK"
"""
    def test_files(self):
        print "Testing files from " + self.samples_dir + "..."
        import os, re, codecs
        from lxml.html.diff import htmldiff
        cases = os.listdir(self.samples_dir)
        for case in cases:
            parts = re.search('(.+)\.(.+)', case)
            if parts.group(2) == 'md': continue
            case_name = parts.group(1)
            
            case_name_html = self.samples_dir + case_name + '.html'
            f_html = codecs.open(case_name_html, 'r', 'utf-8')
            case_html = f_html.read()
            f_html.close()
            
            case_name_md = self.samples_dir + case_name + '.md'
            f_md = codecs.open(case_name_md, 'r', 'utf-8')
            case_md = f_md.read()
            f_md.close()

            case_challenge = self.t.translate(fromstring(case_html))
            if isinstance(case_challenge, str):
                case_challenge = unicode(case_challenge, 'utf-8')
            f_challenge = codecs.open(case_name_md + '.challenge', 'w', 'utf-8')
            f_challenge.write(case_challenge)
            f_challenge.close()

            err_msg = 'Translation of ' + case_name_html + ' does not match ' + case_name_md + '\n' \
                        + '\tTranslation of ' + case_name_html + ' will be saved as ' + case_name_md + '.challenge\n'
            self.assertEqual(case_md.rstrip(), case_challenge.rstrip(), err_msg)
            os.remove(case_name_md + '.challenge')
        print "OK"
"""

# Run Tests
if __name__ == '__main__':
    unittest.main()

            
