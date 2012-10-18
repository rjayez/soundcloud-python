from contextlib import contextmanager

import fudge
import soundcloud

from nose.tools import raises, assert_raises
from requests.exceptions import HTTPError, TooManyRedirects

from soundcloud.tests.utils import MockResponse


@contextmanager
def response_status(fake_http_request, status):
    response = MockResponse('{}', status_code=status)
    fake_http_request.expects_call().returns(response)
    yield

@fudge.patch('requests.get')
def test_ok_response(fake):
    """A 200 range response should be fine."""
    client = soundcloud.Client(client_id='foo', client_secret='foo')
    for status in (200, 201, 202, 203, 204, 205, 206):
        with response_status(fake, status):
            user = client.get('/me')

