vim-xsnippet
============

**vim-xsnippet** is a simple Vim_ plugin which enables one to post code
snippets to the xsnippet.org_ pastebin service directly from Vim.


Requirements
------------

* Python 2.x
* Vim 7.x built with ``+python`` option


Installation
------------

Copy all files to your ``$VIMRUNTIME`` dir (usually ``~/.vim``).

    **Note:** if you use pathogen, copy all files to some
    dir in your bundles path.

Using
-----

``:call PostToXsnippet()``
    posts the content of the current buffer to xsnippet.org_
    and puts the snippet's url to the clipboard

Info
----

* Author:   Roman Podolyaka (roman.podolyaka@gmail.com)
* License:  GNU GPL v3
* Homepage: https://github.com/xsnippet/vim-xsnippet


.. _xsnippet.org: http://www.xsnippet.org/
.. _Vim: http://www.vim.org/
