from registration.views import RegistrationView


class NewRegistrationView(RegistrationView):
    success_url = 'home'
