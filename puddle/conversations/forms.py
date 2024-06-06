from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-md",
                "rows": 4,  # Adjust the number of rows as needed
                "placeholder": "Enter your message here...",
            }),
        }
