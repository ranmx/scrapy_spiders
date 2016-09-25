from scrapy.downloadermiddlewares.redirect import RedirectMiddleware as ReM
from urlparse import urljoin
from config import *
from scrapy.http import HtmlResponse
from scrapy.utils.response import get_meta_refresh
from scrapy.utils.python import to_native_str
from scrapy.exceptions import IgnoreRequest, NotConfigured


class RedirctMW(ReM):


    def process_response(self, request, response, spider):
        if (request.meta.get('dont_redirect', False) or
                response.status in getattr(spider, 'handle_httpstatus_list', []) or
                response.status in request.meta.get('handle_httpstatus_list', []) or
                request.meta.get('handle_httpstatus_all', False)):
            return response

        allowed_status = (301, 302, 303, 307)
        if 'Location' not in response.headers or response.status not in allowed_status:
            return response

        # HTTP header is ascii or latin1, redirected url will be percent-encoded utf-8
        location = to_native_str(response.headers['location'].decode('latin1'))

        redirected_url = urljoin(request.url, location)

        if '?ticket=' in redirected_url:
            redirected = request.replace(url=redirected_url, headers=HEADER_TICKET_302, cookies=None)
            return self._redirect(redirected, request, spider, response.status)

        if response.status in (301, 307) or request.method == 'HEAD':
            redirected = request.replace(url=redirected_url)
            return self._redirect(redirected, request, spider, response.status)

        redirected = self._redirect_request_using_get(request, redirected_url)
        return self._redirect(redirected, request, spider, response.status)
