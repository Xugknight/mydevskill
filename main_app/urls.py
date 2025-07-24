from django.urls import path
from .views import HomeView, signup_view, login_view, logout_view, SkillListView, SkillDetailView, SkillCreateView, SkillDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='landing'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('skills/', SkillListView.as_view(), name='my_skills'),
    path('skills/create/', SkillCreateView.as_view(), name='add_skill'),
    path('skills/<int:pk>/', SkillDetailView.as_view(), name='skill_detail'),
    path('skills/<int:pk>/delete/', SkillDeleteView.as_view(), name='delete_skill'),
]