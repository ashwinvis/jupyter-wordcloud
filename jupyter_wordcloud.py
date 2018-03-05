#!/usr/bin/env python
"""jupyter-wordcloud
====================
Generate wordcloud from Jupyter notebooks.

"""
from argparse import ArgumentParser
from nbconvert import RSTExporter
from os import path
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


parser = ArgumentParser(
    prog='jupyter-wordcloud',
    description='jupyter notebooks > RST > wordcloud as image')
parser.add_argument('path_ipynb', help='input Jupyter notebook')
parser.add_argument('-o', '--output', help='output image path', default=None)
parser.add_argument(
        '-r', '--keep-rstdir', help='keep RST directives',
        action='store_true')
parser.add_argument(
        '-k', '--keep-html', help='keep HTML tags',
        action='store_true')
parser.add_argument(
        '-v', '--verbose', help='display converted text',
        action='store_true')


def clean_rstdir(raw_rst):
    """Clean up RST directive blocks."""

    raw_rst = raw_rst.splitlines()
    clean_rst = []
    inside_rst_dir_block = False
    for line in raw_rst:
        if line.startswith('.. '):
            inside_rst_dir_block = True
            continue
        else:
            clean_rst.append(line)

        if inside_rst_dir_block and (
                line.startswith('    ') or line == ''):
            continue
        else:
            inside_rst_dir_block = False

    return '\n'.join(clean_rst)


def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def main(args=None):
    if args is None:
        args = parser.parse_args()

    notebook = args.path_ipynb

    # Instantiate it
    rst_exporter = RSTExporter()
    # Convert the notebook to RST format
    (body, resources) = rst_exporter.from_filename(notebook)
    if not args.keep_rstdir:
        body = clean_rstdir(body)

    if not args.keep_html:
        body = clean_html(body)

    if args.verbose:
        print(body)

    # TODO: unnecessary or remove hardcoding
    blacklist = {
        'src', 'fig', 'raw', 'html', 'latex', 'bf', 'img', 'div', 'math', 'png',
        'alt', 'align', 'green', 'Ding', 'link', 'nbsp', 'cdot', 'nabla', 'frac',
        'partial', 'eta', 'style', 'width', 'right', 'left', 'center', 'Result',
        'drawing'}
    stopwords = set(STOPWORDS).union(blacklist)

    wordcloud = WordCloud(background_color="white", stopwords=stopwords)
    wordcloud.generate(body)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout()
    if args.output is None:
        plt.show()
    else:
        output = path.splitext(path.basename(notebook))[0] + '_wordcloud.png'
        output = path.join(args.output, output)
        print('Saving to', output)
        plt.savefig(output)


if __name__ == '__main__':
    main()
