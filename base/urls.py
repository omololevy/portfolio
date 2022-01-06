from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('posts/', views.posts, name= "posts"),
	path('post/<slug:slug>/', views.post, name="post"),
	path('profile/', views.profile, name="profile"),

	#CRUD PATHS

	path('create_post/', views.createPost, name="create_post"),
	path('update_post/<slug:slug>/', views.updatePost, name="update_post"),
	path('delete_post/<slug:slug>/', views.deletePost, name="delete_post"),


	path('send_email/', views.sendEmail, name="send_email"),

	path('login/', views.loginPage, name="login"),
	path('register/', views.registerPage, name="register"),
	path('logout/', views.logoutUser, name="logout"),

	path('about/', views.myAbout, name="about"),
	path('skills/', views.mySkills, name="skills"),
	path('contact/', views.myContact, name="contact"),
	path('account/', views.userAccount, name="account"),
	path('education/', views.myEducation, name="education"),
	path('experience/', views.myExperience, name="experience"),
	path('achievements/', views.myAchievements, name="achievements"),
	path('update_profile/', views.updateProfile, name="update_profile"),
]