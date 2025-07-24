from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, TemplateView, DeleteView, UpdateView
from .forms import SignUpForm, LoginForm, SkillForm
from .models import Skill

class HomeView(TemplateView):
    template_name = 'home.html'

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('my_skills')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(
            request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user:
            login(request, user)
            return redirect('my_skills')
        form.add_error(None, 'Invalid Username or Password.')
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('landing')

class SkillListView(LoginRequiredMixin, ListView):
    model = Skill
    template_name = 'skills/list.html'
    context_object_name = 'skills'

    def get_queryset(self):
        return Skill.objects.filter(user=self.request.user)

class SkillDetailView(LoginRequiredMixin, DetailView):
    model = Skill
    template_name = 'skills/detail.html'


class SkillCreateView(LoginRequiredMixin, CreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skills/form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class SkillDeleteView(LoginRequiredMixin, DeleteView):
    model = Skill
    template_name = 'skills/confirm_delete.html'
    success_url = reverse_lazy('my_skills')

    def get_queryset(self):
        return Skill.objects.filter(user=self.request.user)

class SkillUpdateView(LoginRequiredMixin, UpdateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skills/edit_form.html'

    def get_queryset(self):
        return Skill.objects.filter(user=self.request.user)