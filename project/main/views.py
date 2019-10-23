from django.shortcuts import render
from django.views import View

from .models import SampleData

# Create your views here.


class Home(View):
    template_name = 'main/home.html'
    context = {
        'page_title': 'Home Page',
        'data': {
            'name': "Home Page",
        }
    }

    def get(self, request):
        user_is_logged = request.user.is_authenticated

        self.context['user_is_logged'] = user_is_logged

        content = SampleData.objects.all()

        if user_is_logged:
            # Stuff exclusive to people we already know
            pass

        self.context['content'] = content

        return render(request, self.template_name, self.context)
