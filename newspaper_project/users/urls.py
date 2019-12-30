from	django.urls	import	path 
from	.	import	views 

installed_apps ='users'
urlpatterns	=	[ 
    path('signup/',	views.SignUp.as_view(),	name='signup'), 
    ]
