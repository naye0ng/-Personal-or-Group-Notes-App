from django import forms 
from .models import Memo 

class MemoForm(forms.ModelForm):
    class Meta :
        model = Memo
        fields = ["title","content",]
        widgets={
            "title" : forms.TextInput(
                attrs={
                    "class" : "form-control",
                    "placeholder" : "제목을 입력하세요."
                }),
            "content" : forms.Textarea(
                attrs={
                    "class" : "form-control",
                    "placeholder" : "내용을 입력하세요."
                })
        }