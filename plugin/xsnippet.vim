let s:plugin_path = escape(expand('<sfile>:p:h'), '\')

function! PostToXsnippet()

python import sys
exe 'python sys.path.insert(0, "' . s:plugin_path . '")'

python << EOF
import os

import getpass

import vim
import xsnippet

FT_TO_LANGUAGE = {
    "c": "C",
    "cpp": "C++",
    "cs": "C#",
    "java": "Java",
    "python": "Python",
    "sh": "Bash",
    "html": "HTML",
    "xml": "XML",
    "css": "CSS",
    "javascript": "JavaScript",
    "php": "PHP",
    "sql": "SQL",
    "ruby": "Ruby",
    "apache": "Apache",
    "cmake": "CMake",
    "diff": "diff",
    "django": "Django",
    "dosbatch": "DOS",
    "erlang": "Erlang",
    "haskell": "Haskell",
    "dosini": "ini",
    "lisp": "Lisp",
    "lua": "Lua",
    "objc": "Objective-C",
    "perl": "Perl",
    "tex": "TeX",
    "vhdl": "VHDL",
    "verilog": "Verilog",
    "nasm": "Nasm",
    "asm": "Gas",
}

url = xsnippet.post_snippet(content='\n'.join(vim.current.buffer[:]),
                            title=vim.eval("expand('%:t')"),
                            language=FT_TO_LANGUAGE.get(vim.eval("&ft"), "Autodetection"),
                            author=getpass.getuser())

vim.command("let @+ = '%s'" % url)

EOF
endfunction
