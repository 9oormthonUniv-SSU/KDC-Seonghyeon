from django import forms
from .models import ImageUploadModel
class SimpleUploadForm(forms.Form):
    title = forms.CharField(max_length=50)

    image = forms.ImageField()

class ImageUploadForm(forms.ModelForm):

    # Form을 통해 받아들여야 할 데이터가 명시되어 있는 메타 데이터 (DB 테이블을 연결)
    class Meta:
        model = ImageUploadModel
    # Form을 통해 사용자로부터 입력 받으려는 Model Clas
        fields = ('description', 'document',)  # uploaded_at