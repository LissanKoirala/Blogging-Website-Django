from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('your_name', 'comment')

		widgets = {
			'your_name': forms.TextInput(attrs={'class':'form-control'}),
			'comment': forms.Textarea(attrs={'class':'form-control'}),
		}