
from django.contrib import admin
from django.urls import path
from baseapp.views import registration_view, home, logout_view, login_view, account_view
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
# from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('account/', account_view, name="account"),
    # path('api-token-auth/', views.obtain_auth_token),
    # path('api/baseapp', include('baseapp.urls'))
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
