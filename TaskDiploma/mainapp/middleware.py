import time
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse


class SessionIdleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.user.is_superuser:

            if 'last_request' in request.session:
                elapsed = time.time() - request.session['last_request']

                if elapsed > 60:
                    del request.session['last_request'] 
                    logout(request)
                    if "api" in request.path:
                        return HttpResponseRedirect(request.path)
                    else:
                        url = reverse('index')
                        return redirect(url)

            request.session['last_request'] = time.time()
        else:
            if 'last_request' in request.session:
                del request.session['last_request']

        response = self.get_response(request)

        return response

