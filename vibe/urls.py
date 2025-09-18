from django.urls import path
from . import views

# from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.vibe_list, name="vibe_list"),
    path('create/', views.vibe_create, name="vibe_create"),
    path('<int:vibe_id>/edit/', views.vibe_edit, name="vibe_edit"),
    path('<int:vibe_id>/delete/', views.vibe_delete, name="vibe_delete"),
    
    path('register/', views.register,  name="register"),

]
