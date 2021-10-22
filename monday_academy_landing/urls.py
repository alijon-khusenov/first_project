from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('landing.urls', 'monday_academy_landing'), namespace='landing'))
]

urlpatterns += staticfiles_urlpatterns()