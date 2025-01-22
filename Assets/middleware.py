from django.conf import settings
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

ALLOWED_IPS = ['127.0.0.1', '::1', '*', 'pythonanywhere.com']

class RestrictIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip not in ALLOWED_IPS:
            return HttpResponseForbidden("IP not acceptable")
        return self.get_response(request)

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in ['/login/', '/register/']:
            return redirect('login')
        return self.get_response(request)

class RedirectAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path in ['/login/', '/register/']:
            if request.user.groups.filter(name="Administrator").exists():
                return redirect("adminDashboard")
            elif request.user.groups.filter(name="Asset Manager").exists():
                return redirect("assetmanagerDashboard")
            elif request.user.groups.filter(name="Technician").exists():
                return redirect("technicianDashboard")
            elif request.user.groups.filter(name="Auditor").exists():
                return redirect("auditorDashboard")
            elif request.user.groups.filter(name="Reporter").exists():
                return redirect("reporterDashboard")
            else:
                return redirect("userDashboard")
        return self.get_response(request)

