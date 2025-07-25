from django.urls import path
from .views import HomeView, signup_view, login_view, logout_view, SkillListView, SkillDetailView, SkillCreateView, SkillDeleteView, SkillUpdateView, add_note, delete_note

urlpatterns = [
    path('', HomeView.as_view(), name='landing'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('skills/', SkillListView.as_view(), name='my_skills'),
    path('skills/create/', SkillCreateView.as_view(), name='add_skill'),
    path('skills/<int:pk>/', SkillDetailView.as_view(), name='skill_detail'),
    path('skills/<int:pk>/delete/', SkillDeleteView.as_view(), name='delete_skill'),
    path('skills/<int:pk>/edit/', SkillUpdateView.as_view(), name='edit_skill'),
    path('skills/<int:pk>/notes/add/', add_note, name='add_note'),
    path('skills/<int:pk>/notes/<int:note_pk>/delete/', delete_note, name='delete_note'),
]