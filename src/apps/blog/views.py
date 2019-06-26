from django.contrib.auth import get_user_model
from django.views.generic import ListView


User = get_user_model()


class AuthorList(ListView):
    model = User
    template_name = 'blog/author_list.html'
