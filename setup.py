from setuptools import setup
import os


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    long_description = f.read()

lines = long_description.splitlines(True)
long_description = ''.join(lines)


setup(
    name = "jupyter-wordcloud",
    description=('Generate wordclouds from Jupyter notebooks'),
    long_description=long_description,
    version = "0.0.0",
    install_requires=[
        "wordcloud", "nbconvert", "matplotlib", "numpy"],
    entry_points={
        'console_scripts':
        ['jupyter-wordcloud=jupyter_wordcloud:main',
         ]},
    license="BSD",
    author='Ashwin Vishnu Mohanan',
    author_email='avmo@kth.se',
    test_suite='test.TestJupyterWordcloud',
)
