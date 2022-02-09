
from blog import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


# to change the names of admin panel 
admin.site.site_header = 'Al-Quran Academy Administration'
admin.site.site_title = 'Al-Quran Academy Admin Panel'
admin.site.index_title = 'Welcome to Al-Quran Academy Admin Panel'


urlpatterns = [
   path('', views.home, name='home'),
   path('courses', views.courses, name='courses'),
   path('admission', views.admission, name='admission'),
   path('about', views.about, name='about'),
]

# For working media 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
