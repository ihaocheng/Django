
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

class UrlPathMiddleware(MiddlewareMixin):
    def process_view(self, request, *args):
        if request.path not in [
            '/user/register/',
            '/user/register_check/',
            '/user/register_check2/',
            '/user/login/',
            '/user/logout/',
            '/user/login_check/',
            '/user/login_check2/',
            '/goods/list_tag/',
            '/user/site_set/',
        ]:
            url = request.get_full_path()
            request.session['url_path'] = url
            print(url)