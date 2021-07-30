from django.http.response import HttpResponse
from .models import Review
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from .forms import ReviewForm
from .models import Review


#####################################################
# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()

#         return render(request, "app1/review.html", {
#             "form": form
#         })

#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")

#         return render(request, 'review.html', {
#             'form':form
#         })



# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "app1/review.html"
#     success_url = "thank-you"


#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)




class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "app1/review.html"
    success_url = "thank-you"

######################################################

class ThankYouView(TemplateView):
    template_name = "app1/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This works"
        return context


##############################################
# class ReviewsListView(TemplateView):
#     template_name = "app1/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context

class ReviewsListView(ListView):
    template_name = "app1/review_list.html"
    model = Review
    context_object_name = "reviews"

    """ 
            #optional if you ned some filtering
    def get_queryset(self):
        base_query =  super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data

    """
################################################   

        
# class SingleReviewView(TemplateView):
#     template_name = "app1/single_review.html"

#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
#         context["review"] = selected_review
#         return context


# in DetailView url should be pk not id
# in template the data variable is the modelname lowercasehere is "review" or "objct"

class SingleReviewView(DetailView):
    template_name = "app1/single_review.html"
    model = Review




#################################################




