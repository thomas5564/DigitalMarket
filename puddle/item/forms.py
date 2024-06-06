from django import forms
from .models import Item

class createItemForm(forms.ModelForm):
    class Meta:
            model=Item
            InputClasses = "font-bold appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
            fields=["Category","image","name","description","price"]
            widgets={"Category":forms.Select(attrs={"class":InputClasses}),
                     "image":forms.FileInput(attrs={"class":InputClasses}),
                    "name":forms.TextInput(attrs={"class":InputClasses}),
                    "description":forms.TextInput(attrs={"class":InputClasses}),
                    "price":forms.TextInput(attrs={"class":InputClasses}),}

class editItemForm(forms.ModelForm):
    class Meta:
            model=Item
            InputClasses = "font-bold appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
            fields=["image","name","description","price","is_sold"]
            widgets={"image":forms.FileInput(attrs={"class":InputClasses}),
                    "name":forms.TextInput(attrs={"class":InputClasses}),
                    "description":forms.TextInput(attrs={"class":InputClasses}),
                    "price":forms.TextInput(attrs={"class":InputClasses}),
                    "sold":forms.Select(attrs={"class":InputClasses})}
