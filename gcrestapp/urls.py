from django.urls import path
from .views import RestaurantList, RestaurantDetail,DeliveryList,DeliveryDetail,CreateDelivery,UserList,UserCreate, LoginView
from rest_framework.authtoken import views
from django.conf.urls import url

urlpatterns = [
    path("restaurants/", RestaurantList.as_view(), name="restaurants_list"),
    path("restaurants/<int:pk>/", RestaurantDetail.as_view(), name="restaurants_detail"),
    path("deliveries/", DeliveryList.as_view(), name="delivery_list"),
    path("deliveries/<int:pk>/", DeliveryDetail.as_view(), name="delivery_detail"),
    path("delivery/", CreateDelivery.as_view(), name="create_delivery"),
    path("users/", UserList.as_view(), name="user_list"),
    path("user/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    url(r'^api-token-auth/', views.obtain_auth_token),
]