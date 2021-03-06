from django.conf.urls import patterns, url
from mainapp import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^restricted/', views.restricted, name='restricted'),
	url(r'^about/$', views.about, name='about'),
	url(r'^which_expenses/$',views.which_expenses, name='which_expenses'),
	url(r'^(?P<user_name_url>\w+)/$', views.dashboard, name='dashboard'),
	url(r'^(?P<user_name_url>\w+)/macro$', views.edit_macros, name='macros'),
	url(r'^(?P<user_name_url>\w+)/budget$', views.edit_budget, name='budget'),
	url(r'^(?P<user_name_url>\w+)/all_expenses$', views.all_expenses, name='all_expenses'),
	url(r'^(?P<user_name_url>\w+)/which_expenses$', views.which_expenses, name='which_expenses'),
	url(r'^(?P<user_name_url>\w+)/all_expenses/(?P<month_url>\w+)$', views.all_expenses, name='all_expenses'),
	url(r'^(?P<user_name_url>\w+)/(?P<expense_id_url>\w+)$', views.edit_expense, name='expense')
	)