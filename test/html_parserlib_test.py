from unittest import TestCase, main
import import_module
from PYSTUDY.html_parserlib import LinksParser
from PYSTUDY.loglib import Logger


LOG = Logger('html_parserlib')


class HtmlParserLibTestCase(TestCase):
    def test_link_parser(self):
        text = None
        with open('html_parser_data/test.html', 'r') as f:
            text = f.read()

        LOG.log(text)
        lp = LinksParser(text=text)
        for i in lp.links():
            print(i.text, i.url)


if __name__ == '__main__':
    main()
