"""
URL configuration for tienda_ceramica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from products import views as product_views
from cart import views as cart_views

urlpatterns = [
    path("", product_views.HomepageView.as_view(), name="homepage"),
    path("<int:pk>", product_views.DetailView.as_view(), name="detail"),
    path("carrito", cart_views.LocalStorageCartView.as_view(), name="carritolocal"),
    path("add/<int:pieza_id>/", cart_views.AddToCart.as_view(), name="AddToCart"),
    path(
        "remove/<int:pieza_id>/",
        cart_views.RemoveFromCart.as_view(),
        name="RemoveFromCart",
    ),
    path(
        "micarrito",
        cart_views.DatabaseCartView.as_view(),
        name="micarrito",
    ),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("cuenta/", include("users.urls")),
    path("api/stock/<int:product_id>", product_views.stock_view, name="stock_view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
