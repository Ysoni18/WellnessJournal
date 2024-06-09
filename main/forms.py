from django import forms
	
class text(forms.Form):
	title = forms.CharField(max_length=30, label='', widget=forms.Textarea(attrs={'class':'title','cols':75,'rows':1,'placeholder':'title'}))
	class_id = forms.CharField(max_length=5,label='', widget=forms.Textarea(attrs={'class':'class_id', 'cols':75,'rows':1,'placeholder':'class id'}))
	text = forms.CharField(max_length=450,label='', widget=forms.Textarea(attrs={'class':'text','cols':75, 'rows':10,
	 'placeholder':'Write your thoughts here...'}))
	

