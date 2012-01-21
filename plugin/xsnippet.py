import urllib
import urllib2

APIURL = "http://www.xsnippet.org/new"

def post_snippet(content,
                 title="Untitled",
                 author="Anonymous",
                 language="Autodetection",
                 tags=[]):
    """
    Post a text snippet to the www.xsnippet.org pastebin service

    Arguments:
        content  --- text content of the snippet (string)
        title    --- a title of the snippet (string)
        author   --- an author of the snippet (string)
        language --- a programming language the snippet is written in (string)
        tags     --- tags associated with the snippet (list of strings)

    (note: all strings should be UTF-8 encoded)

    Returns:
        a string containing the url of the posted snippet
    """

    params = {
                 'title': title
               , 'content': content
               , 'author': author
               , 'language': language
               , 'tags': ','.join(tags)
             }

    request = urllib2.urlopen(APIURL, data=urllib.urlencode(params))
    return request.geturl()
