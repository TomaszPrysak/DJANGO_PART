from django import forms
from django.contrib.auth.models import User
from .models import Post, Category, Subcategory
from django.core import validators

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = '__all__'

    def clean(self):
        subcategory = self.cleaned_data['subcategory']
        if subcategory is None:
            return self.cleaned_data
        try:
            category = self.cleaned_data['category']
            subcategory_category = Subcategory.objects.get(pk=subcategory.pk).main_category
            if subcategory_category == category:
                return self.cleaned_data
            else:
                raise forms.ValidationError()
        except:
            msg = "Podkategoria '{0}' nie należy do kategorii '{1}'. Sprawdź w powyższej hierarchii przynależności podkategorii postów do kategorii głównych".format(subcategory.name_subcategory, category.name_category)
            raise forms.ValidationError(msg)

class CategoryForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = '__all__'

class SubcategoryForm(forms.ModelForm):
    class Meta():
        model = Subcategory
        fields= '__all__'
