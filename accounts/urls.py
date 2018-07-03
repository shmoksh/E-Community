from django.conf.urls import url
from django.contrib.auth import views as auth_views
from accounts import views

aap_name = 'accounts'

urlpatterns=[
	url(r'^login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
	url(r'^signup/$',views.Signup.as_view(template_name='accounts/signup.html'),name='signup'),
	url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),
	
]