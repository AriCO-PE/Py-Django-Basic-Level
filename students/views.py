from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from django.contrib.auth.views import LogoutView


class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return 'dashboard.html'  

class logout_view(LogoutView):
    next_page = 'login.html'  