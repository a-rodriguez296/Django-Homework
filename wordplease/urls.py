from django.conf.urls import include, url
from django.contrib import admin
from posts import urls as posts_urls, api_urls as posts_api_urls
from users import urls as users_urls, api_urls as users_api_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #Users Urls
    url(r'', include(users_urls)),
    url(r'api/', include(users_api_urls)),

    #Posts urls
    url(r'', include(posts_urls)),
    url(r'api/', include(posts_api_urls)),
]