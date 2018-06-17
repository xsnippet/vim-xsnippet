vim-xsnippet
============

**vim-xsnippet** is a simple Vim_ plugin that enables one to post code
snippets to xsnippet.org_ pastebin service directly from Vim.


Requirements
------------

* Python 2.7+
* Vim 7.x+ built with ``+python``


Installation
------------

Copy all files to your ``$VIMRUNTIME`` dir (usually ``~/.vim``).

Alternatively, if you are using Vundle_ plug-in manager for Vim_, add the
following line to your ``.vimrc``::

    Bundle 'xsnippet/vim-xsnippet'


Usage
-----

``:call PostToXsnippet()``
    posts the content of the current buffer to xsnippet.org_ and puts the
    snippet url to the clipboard

Info
----

* Authors:  The XSnippet Team (dev@xsnippet.org)
* License:  MIT
* Homepage: https://github.com/xsnippet/vim-xsnippet


.. _xsnippet.org: https://xsnippet.org/
.. _Vim: http://www.vim.org/
.. _Vundle: https://github.com/VundleVim/Vundle.vim
