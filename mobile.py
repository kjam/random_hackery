class MobileMiddleware(object):
    '''This is a simple mobile middleware wrapper for Django that uses separate caching environments for mobile vs. standard browser interactions'''
    def process_request(self,request):
        if 'HTTP_USER_AGENT' in request.META:
            touch = (lambda x:'iPad' in x or 'iPhone' in x or 'Android' in x or False)(request.META['HTTP_USER_AGENT'])
            ipad = (lambda x:'iPad' in x or False)(request.META['HTTP_USER_AGENT'])
            if ipad:
                CACHE_MIDDLEWARE_KEY_PREFIX = '542378909#$'
            elif touch:
                CACHE_MIDDLEWARE_KEY_PREFIX = '5589043cjkowio'
        return None

    def process_response(self, request, response):
        return response
