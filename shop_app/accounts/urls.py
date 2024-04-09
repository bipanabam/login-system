from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),

    path("home/", views.home, name="home"),
    path("customer-dashboard/", views.customerDashboard, name="customer_dashboard"),
    path("admin-dashboard/", views.adminDashboard, name="admin_dashboard"),
    path("supplier-dashboard/", views.supplierDashboard, name="supplier_dashboard"),
]
