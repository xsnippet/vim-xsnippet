let s:plugin_path = escape(expand('<sfile>:p:h'), '\')

function! PostToXsnippet()

python import sys
exe 'python sys.path.insert(0, "' . s:plugin_path . '")'

python << EOF
import vim
import xsnippet

FT_TO_LANGUAGE = {
    "c": "c_cpp",
    "cpp": "c_cpp",
    "cs": "csharp",
    "java": "java",
    "python": "python",
    "sh": "sh",
    "html": "html",
    "xml": "xml",
    "css": "css",
    "javascript": "javascript",
    "php": "php",
    "sql": "sql",
    "ruby": "ruby",
    "apache": "apache_conf",
    "diff": "diff",
    "django": "django",
    "dosbatch": "batchfile",
    "erlang": "erlang",
    "haskell": "haskell",
    "dosini": "ini",
    "lisp": "lisp",
    "lua": "lua",
    "objc": "objectivec",
    "perl": "perl",
    "tex": "latex",
    "vhdl": "vhdl",
    "verilog": "verilog",
    "asm": "assembly_x86",
    "yaml": "yaml",
    "dockerfile": "dockerfile"
}

url = xsnippet.post_snippet(
    content='\n'.join(vim.current.buffer[:]),
    title=vim.eval("expand('%:t')"),
    syntax=FT_TO_LANGUAGE.get(vim.eval("&ft"), "text")
)

vim.command("let @+ = '%s'" % url)

EOF
endfunction
