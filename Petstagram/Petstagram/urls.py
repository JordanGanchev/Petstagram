from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Petstagram.common.urls')),
    path('accounts/', include('Petstagram.accounts.urls')),
    path('pets/', include('Petstagram.pets.urls')),
    path('photos/', include('Petstagram.photos.urls')),
]

'''
After 'startAPP-NAME'

1. Create APP_NAME/urls.py with empty 'urlpatterns'
2. Include 'APP_NAME/urls.py into project's urls.py'
3. Add 'APP_NAME' to 'INSTALLED_APPS' in settings.py

'''