from django .urls import re_path
from Login.views import LoginAuth

urlpatterns = [
    re_path(r'^', LoginAuth.as_view()),
]