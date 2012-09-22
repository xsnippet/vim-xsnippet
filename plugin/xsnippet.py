import urllib
import urllib2
import json


def post_snippet(title, language, content):
    """
        Send file to xsnippet.org and return link to last one.
        Return "None" if error occured.
    """

    POST_SNIPPET_URL = "http://xsnippet.org/api/v1/snippets/"
    SHOW_SNIPPET_URL = "http://xsnippet.org/{id}/"

    if not content:
        return None

    data = {"content": content}

    if title is not None:
        data["title"] = title
    if language is not None:
        data["language"] = language

    request = urllib2.Request(POST_SNIPPET_URL, urllib.urlencode(data))
    response = urllib2.urlopen(request)

    if response.getcode() == 201:
        id = json.loads(response.read()).get("id")
        return SHOW_SNIPPET_URL.format(id=id)

    return None
