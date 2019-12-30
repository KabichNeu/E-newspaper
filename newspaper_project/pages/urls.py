from	django.urls	import	path
from	.	import	views

installed_apps = 'pages'
urlpatterns	=	[ 
    path('',	views.HomePageView.as_view(),	name='home'),
     ]
