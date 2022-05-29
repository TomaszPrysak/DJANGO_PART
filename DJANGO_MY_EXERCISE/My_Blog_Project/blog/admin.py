from django.contrib import admin
from .models import Post, Category, Subcategory
from django import forms
from django.core.exceptions import ValidationError

# Register your models here.

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def clean(self):
        subcategory = self.cleaned_data['subcategory']
        if subcategory is None:
            return self.cleaned_data
        else:
            try:
                category = self.cleaned_data['category']
                subcategory_category = Subcategory.objects.get(pk=subcategory.pk).main_category
                if subcategory_category == category:
                    return self.cleaned_data
                else:
                    raise ValidationError()
            except:
                msg = "Podkategoria '{0}' nie należy do kategorii '{1}'. Sprawdź w 'Subcategorys' przynależność podkategorii do głównej kategorii.".format(subcategory.name_subcategory, category.name_category)
                raise ValidationError(msg)

class PostAdmin(admin.ModelAdmin):
    form = PostForm

    def save_model(self, request, obj, form, change):
        if obj.author == request.user or request.user.is_superuser:
            try:
                super().save_model(request, obj, form, change)
            except:
                pass

    list_filter = ['category', 'subcategory']
    list_display = ['title', 'date', 'category', 'subcategory']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Subcategory)
