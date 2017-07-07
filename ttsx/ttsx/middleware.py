
class UrlPathMiddleware():
    def process_request(self,request):
        if request.path not in [
            '/user/register/',
            '/user/register_check/',
            '/user/register_check2/',
            '/user/login/',
            '/user/logout/',
            '/user/login_check/',
            '/user/login_check2/',
        ]:
            request.session['url_path']=request.get_full_path()