"""learning_log/urls.py"""

# Django modules
from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include(('users.urls','users'), namespace='users')),
    url(r'', include(('learning_logs.urls','learning_logs'), namespace='learning_logs')),
    ]
