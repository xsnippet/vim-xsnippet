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
    "c": "c",
    "cpp": "cpp",
    "cs": "csharp",
    "java": "java",
    "python": "python",
    "sh": "bash",
    "html": "html+php",
    "xml": "xml",
    "css": "css",
    "javascript": "javascript",
    "php": "php",
    "sql": "sql",
    "ruby": "ruby",
    "apache": "apache",
    "cmake": "cmake",
    "diff": "diff",
    "django": "django",
    "dosbatch": "bat",
    "erlang": "erlang",
    "haskell": "haskell",
    "dosini": "ini",
    "lisp": "cl",
    "lua": "lua",
    "objc": "objc",
    "perl": "perl",
    "tex": "tex",
    "vhdl": "vhdl",
    "verilog": "v",
    "nasm": "nasm",
    "asm": "gas",
    "yaml": "yaml",
    "vim": "vim"
}

url = xsnippet.post_snippet(
    content='\n'.join(vim.current.buffer[:]),
    title=vim.eval("expand('%:t')"),
    language=FT_TO_LANGUAGE.get(vim.eval("&ft"), "text")
)

vim.command("let @+ = '%s'" % url)

EOF
endfunction
