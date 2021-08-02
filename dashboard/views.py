from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, 'dashboard/base_dashboard.html')
