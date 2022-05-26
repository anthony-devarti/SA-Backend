from django.urls import path, include
from rest_framework import routers
from . import views
from strange.views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView

router = routers.DefaultRouter()
router.register(r'orders', views.OrderViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.index, name='index'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
