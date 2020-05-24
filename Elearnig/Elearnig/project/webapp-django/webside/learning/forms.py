from django import forms
from .models import Contact, CourseReview, BillDetail


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["user_id", "contact_name", "contact_mail", "contact_content"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = CourseReview
        fields = ["user_id", "course_id", "review_content", "review_star"]

class CheckOutForm(forms.ModelForm):
    class Meta:
        model = BillDetail
        fields = ["user_id", "course_id", "bill_fn", "bill_ln", "bill_mail", "bill_address", "bill_country", "bill_city", "bill_zip"]

