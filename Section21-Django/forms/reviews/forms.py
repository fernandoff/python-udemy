from django import forms

class ReviewForm(forms.Form):
    name = forms.CharField(label="Nome:", max_length=100, 
                           error_messages={
                               "required": "O campo não pode estar vazio",
                               "max_lenght": "Defina um nome menor que 100 caracteres"
                           })
    username = forms.CharField(label="Username:", max_length=50, 
                           error_messages={
                               "required": "O campo não pode estar vazio",
                               "max_lenght": "Defina um username menor que 100 caracteres"
                           })
    review = forms.CharField(label="Feedback", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)