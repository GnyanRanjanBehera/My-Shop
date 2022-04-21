from django.contrib import admin
from django.urls import path,include
admin.site.site_header="My Shops Admin"
admin.site.site_title="My Shops Admin Panel"
admin.site.index_title="Welcome To My Shops Admin"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
]
