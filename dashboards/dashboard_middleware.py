# yourapp/dashboard_middleware.py
from django.shortcuts import redirect,render

class DashboardPermissionMiddleware:
    """
    Restrict all URLs starting with /dashboard to managers or editors.
    """
    allowed_groups = ['Manager', 'Editor']  

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info

        if path.startswith('/dashboard'):
            # redirect if user is not logged in
            if not request.user.is_authenticated:
                return redirect('login')  # adjust to your login URL

            # check if user is in allowed groups
            if not request.user.groups.filter(name__in=self.allowed_groups).exists():
                return render(request,'403.html')

        response = self.get_response(request)
        return response
