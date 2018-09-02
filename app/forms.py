from django.forms import models

from app.models import Level, Problem


class LevelForm(models.ModelForm):

    class Meta:
        model = Level
        fields = ['title', 'content']
        widgets = {

        }

    def __init__(self, *args, **kwargs):
        super(LevelForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '제목을 입력해주세요'
        })
        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '받아쓰기에 대한 설명을 써주세요'
        })

    def save(self, commit=True):
        self.instance.made_by_user = True
        return super(LevelForm, self).save()
