from django.contrib import admin
from django.urls import path
from list import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('shoppinglist/admin/', admin.site.urls),
    path('shoppinglist/', views.ShoppingListView.as_view()),
    path('shoppinglist/<int:pk>', views.ShoppingDetailView.as_view()),
    path('shoppinglist/<int:pk>/update/', views.ShoppingUpdateView.as_view()),
    path('shoppinglist/<int:pk>/delete/', views.ShoppingDeleteView.as_view()),
    path('shoppinglist/new/', views.ShoppingCreateView.as_view()),

    #AUTH
    path('accounts/login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view(next_page="/shoppinglist/")),
]
