from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import FormView, UpdateView

from baskets.models import Basket
from geekshop.mixin import BaseClassContextMixin
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib.auth.decorators import user_passes_test

from users.models import User


class LoginListView(LoginView, BaseClassContextMixin):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'geekshop | авторизация'
    success_url = reverse_lazy('index')


class RegisterListView(FormView, BaseClassContextMixin):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    title = 'geekshop | регистрация'
    success_url = reverse_lazy('users:login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect(self.success_url)
        else:
            print(form.errors)
            return redirect('users:register')


class ProfileFormView(UpdateView, BaseClassContextMixin):
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    title = 'geekshop | профиль'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES, instance=self.get_object())
        if form.is_valid():
            form.save()
            messages.success(request, 'Успешно изменено!')
            return redirect(self.success_url)
        else:
            return redirect(self.success_url)


class Logout(LogoutView):
    template_name = 'mainapp/index.html'
    title = 'geekshop | main page'
