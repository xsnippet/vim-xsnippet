import contextlib
import json
import os

try:
    # python 3
    import http.client as http
except ImportError:
    # python 2
    import httplib as http


API_URL = os.environ.get('XSNIPPET_API_URL', 'https://api.xsnippet.org')
WEB_URL = os.environ.get('XSNIPPET_WEB_URL', 'https://xsnippet.org')
TIMEOUT = int(os.environ.get('XSNIPPET_CONN_TIMEOUT', 10))


def post_snippet(title, syntax, content):
    if not content:
        raise ValueError('Can not post an empty snippet')

    if API_URL.startswith('https'):
        conn = http.HTTPSConnection(API_URL.split('https://', 1)[-1], 443,
                                    timeout=TIMEOUT)
    else:
        conn = http.HTTPConnection(API_URL.split('http://', 1)[-1], 80,
                                   timeout=TIMEOUT)

    with contextlib.closing(conn):
        conn.request(
            'POST', '/v1/snippets',
            body=json.dumps({
                'content': content,
                'title': title,
                'syntax': syntax
            }),
            headers={
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        )

        response = conn.getresponse()
        if response.status != http.CREATED:
            raise ValueError('Failed to post a snippet')

        snippet_id = json.loads(response.read())['id']
        return '%s/%s' % (WEB_URL, snippet_id)
