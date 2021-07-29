from django.http.response import HttpResponse
from .models import Review
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from .forms import ReviewForm


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "app1/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, 'review.html', {
            'form':form
        })

class ThankYouView(TemplateView):
    template_name = "app1/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This works"
        return context

        


