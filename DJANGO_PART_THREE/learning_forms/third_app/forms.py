from django import forms
from django.core import validators

# Budowa własnego walidatora opierającego się o nasze własne wytyczne do walidacji.
# W poniższym wypadku dla zobrazowania przykładu sprawdzamy czy pierwsza litera pola formularza "name" rozpoczyna się od literki "z"
# def check_for_z(value):
#     if value[0].lower() != "z":
#         raise forms.ValidationError('Name needs to start with Z')

class FormName(forms.Form):
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verifay_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)

    # w poniższej linii jest walidacja poprzez wbudowany w django moduł validators. Który też sprawdza to pole które zostało stworzone tylko na botów.
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    # Poniżej jest własnoręcznie napisana walidacja formularza.
    # Zabezpieczenie przed botami.
    # Tworzymy niewidoczne dla użytkownika pole formularza które może zostać uzupełnione tylko przez bota, bo on nie wie co wyświetla się  na ekranie. On widzi co jest w kodzie html.
    # Tworzymy zatem specjalną funkcję która musi się zaczynać od clean i po podkreślniku musi być nazwa pola którego będzie dotyczyć walidacja
    # Czyli clean_botcatcher
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('Bot złapał się w sidła')
    #     return botcatcher

    # Poniższa funkcja pozwala sprawdzać wszystkie pola formularza.
    # W niej możemy zapisać wszystkie wymagania co do danych wpisywanych do formularza.
    # W naszym przypadku sprawdzamy czy dwa pole email są sobie równe.
    # Jak się domyślacie można to użyć również w polach do haseł.
    # Aby to sprawdzić tworzymy funkcję o nazwie clean.
    # I tak też ta funkcja musi się nazywać.
    # Oczywiście w tej funkcji możemy też umieścić walidacje sprawdzającą inne pola formularza.
    # Na przykład taką którą już wcześniejs zapisaliśmy która sprawdza czy wartość wpisana pole 'name' zaczyna się od literki 'z'.
    # Lepiej chyba takie warunki walidacji pisać w tej funkcji bo bedziemy mieć każdy rodzaj walidacji w jednym miejscu.
    # Nawet tuaj zapisaliśmy ochronę przed botami.
    # Super ta funkcja
    def clean(self):
        all_clean_data = super().clean()
        name = all_clean_data['name']
        email = all_clean_data['email']
        vmail = all_clean_data['verifay_email']
        bcatcher = all_clean_data['botcatcher']
        if email != vmail:
            raise forms.ValidationError('Upewnij się że email został dwa razy podany taki sam')
        if name[0].lower() != "z":
            raise forms.ValidationError('Name needs to start with Z')
        if len(bcatcher) > 0 :
            raise forms.ValidationError('Bot złapał się w sidła')
