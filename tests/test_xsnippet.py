import json

import mock
import pytest

try:
    # python 3
    import http.client as http
except ImportError:
    # python 2
    import httplib as http

import xsnippet


@pytest.fixture
def mocked_http():
    with mock.patch.object(http, 'HTTPConnection') as mock_http:
        with mock.patch.object(http, 'HTTPSConnection') as mock_https:
            yield mock_http, mock_https


TEST_SNIPPET = {
    'id': 42,
    'title': 'snippet #1',
    'content': 'def foo(): pass',
    'syntax': 'python',
    'tags': [],
    'created_at': '2018-06-17 22:00:00',
    'updated_at': '2018-06-17 22:00:00',
}


def test_post_snippet(mocked_http):
    _, mock_https = mocked_http

    conn = mock_https.return_value
    response = conn.getresponse.return_value

    response.status = http.CREATED
    response.read.return_value = json.dumps(TEST_SNIPPET)

    rv = xsnippet.post_snippet(
        title='snippet #1',
        syntax='python',
        content='def foo(): pass'
    )
    assert rv == 'https://xsnippet.org/42'

    conn.request.assert_called_once_with(
        'POST', '/v1/snippets',
        body=json.dumps({
            'content': 'def foo(): pass',
            'title': 'snippet #1',
            'syntax': 'python'
        }),
        headers={
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    )
    conn.close.assert_called_once_with()
    mock_https.assert_called_once_with('api.xsnippet.org', 443, timeout=10)


def test_post_snippet_overriden_settings(mocked_http, monkeypatch):
    monkeypatch.setattr(xsnippet, 'API_URL', 'http://staging.xsnippet.org')
    monkeypatch.setattr(xsnippet, 'WEB_URL', 'http://beta.xsnippet.org')
    monkeypatch.setattr(xsnippet, 'TIMEOUT', 42)

    mock_http, _ = mocked_http

    conn = mock_http.return_value
    response = conn.getresponse.return_value

    response.status = http.CREATED
    response.read.return_value = json.dumps(TEST_SNIPPET)

    rv = xsnippet.post_snippet(
        title='snippet #1',
        syntax='python',
        content='def foo(): pass'
    )
    assert rv == 'http://beta.xsnippet.org/42'

    conn.request.assert_called_once_with(
        'POST', '/v1/snippets',
        body=json.dumps({
            'content': 'def foo(): pass',
            'title': 'snippet #1',
            'syntax': 'python'
        }),
        headers={
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    )
    conn.close.assert_called_once_with()
    mock_http.assert_called_once_with('staging.xsnippet.org', 80,
                                      timeout=42)


def test_post_snippet_error_response(mocked_http):
    _, mock_https = mocked_http

    conn = mock_https.return_value
    response = conn.getresponse.return_value
    response.status = 502  # simulate xsnippet api outage

    with pytest.raises(ValueError, message='Failed to post a snippet'):
        xsnippet.post_snippet(
            title='snippet #1',
            syntax='python',
            content='def foo(): pass'
        )
    conn.close.assert_called_once_with()


def test_post_snippet_empty_content(mocked_http):
    with pytest.raises(ValueError, message='Can not post an empty snippet'):
        xsnippet.post_snippet(
            title='snippet #1',
            syntax='python',
            content=''
        )
