from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash, REDIRECT_FIELD_NAME, logout
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.views import PasswordResetConfirmView
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from django.utils.http import urlsafe_base64_decode
from django.utils.translation import ugettext as _, ugettext_lazy as _l
from django.views import generic
from django.shortcuts import redirect, render




class LoginView(InvalidFormMixin, BaseLoginView):
    """
    Login view
    """
    # http_method_names = ['post']
    form_class = AuthenticationForm
    template_name = 'account/login.html'
    allow_authenticated = False

    def get_form_kwargs(self):
        kw = super(LoginView, self).get_form_kwargs()
        kw.update({'request': self.request})
        return kw

    def form_valid(self, form):

        login(self.request, form.get_user())
        message = _("Welcome back, %s! Redirecting ...") % form.get_user().name
        url = self.get_success_url()
        if self.request.GET.get('amount') and self.request.GET.get('gateway'):
            amount = self.request.GET.get('amount')
            gateway = self.request.GET.get('gateway')
            project = self.request.GET.get('project')
            url = url + '?amount=' + amount + '&gateway=' + gateway + '&project=' + project
        data = {
            'message': message,
            'redirect_url': url
        }

        if not form.cleaned_data.get('remember_me'):
            self.request.session.set_expiry(0)

        return JsonResponse(data, status=200)
