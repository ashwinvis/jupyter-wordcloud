import unittest
import matplotlib
matplotlib.use('agg')

import jupyter_wordcloud


class TestJupyterWordcloud(unittest.TestCase):
    def test_all(self):
        args = jupyter_wordcloud.parser.parse_args(
            ['test.ipynb'])
        jupyter_wordcloud.main(args)

if __name__ == '__main__':
    unittest.main()
