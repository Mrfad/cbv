from django.forms import ModelForm
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        # exclude = ['owner_comment']
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
        error_messages = {
            "user_name":{
                "requred": "Your name must not be empty",
                "max_length": "please enter a shorter name"
            }
        }
