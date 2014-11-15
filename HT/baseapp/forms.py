from django import forms
from django.forms.extras.widgets import SelectDateWidget

class EventForm(forms.form):
    TYPES_OF_EVENTS = (('Art'),('Art'),('Tech','Tech'),('Food','Food'),('Seminars','Seminars'), ('Park','Park'))
    _type = forms.CharField(label='Type' widget=forms.CheckboxSelectMultiple, choices = TYPES_OF_EVENTS, max_length = 200)
    date = forms.DateTimeField(widget=SplitDateTimeWidget)
    details = forms.CharField(widget=forms.Textarea)
    link = forms.CharField(max_length = 2083)

class UserForm(forms.form):
    username = forms.CharField(max_length = 30)
    password = forms.CharField(max_length = 500)

