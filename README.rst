jupyter-wordcloud
=================
Generate wordcloud from Jupyter notebooks.

Example
-------
Command::

    jupyter-wordcloud test.ipynb -o .

Output:

.. figure:: test_wordcloud.png
   :alt: Demo
   :align: right

Installation
------------
Simply do::

    pip install -e git+https://github.com/ashwinvis/jupyter-wordcloud

Or manually::

    git clone https://github.com/ashwinvis/jupyter-wordcloud
    pip install -e .

Test
----
To test::

    python setup.py test
