from django.contrib import admin
from django.urls import include, path

from pages.views import home_view, contact_view, about_view, social_view
from products.views import (
    dynamic_lookup_view,

)

urlpatterns = [
    path('blog/', include('Blog.urls')),
    path('products/', include('products.urls')),
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('social/', social_view, name='social'),
    path('admin/', admin.site.urls),

    path('products/<int:id>/', dynamic_lookup_view, name='product-detail'),

]
