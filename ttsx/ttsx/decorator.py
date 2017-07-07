from django.shortcuts import redirect

def islogin(fun1):
    def fun2(request, *args,**kwargs):
        if request.session.get('id'):
            return fun1(request)
        else:
            return redirect('/user/login/')
    return fun2