from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import Project, Message

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        # fields = '__all__'
        fields = ['title', 'thumbnail', 'body']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'})

        self.fields['body'].widget.attrs.update(
            {'class': 'form-control'})

    # def __init__(self, *args, **kwargs):
    #     super(ProjectForm, self).__init__(*args, **kwargs)
    #     self.fields['title'].widget.attrs.update(
    #         {'class': 'form-control'})

    #     self.fields['body'].widget.attrs.update(
    #         {'class': 'form-control', })

class MessageForm(ModelForm):
    
    class Meta:
        model = Message
        fields = '__all__'
        exclude = ['is_read']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'})
        
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control'})
        
        self.fields['subject'].widget.attrs.update(
            {'class': 'form-control'})

        self.fields['body'].widget.attrs.update(
            {'class': 'form-control'})

    # def __init__(self, *args, **kwargs):
    #     super(MessageForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs.update(
    #         {'class': 'form-control'})
    #     self.fields['email'].widget.attrs.update(
    #         {'class': 'form-control', })

    #     self.fields['subject'].widget.attrs.update(
    #         {'class': 'form-control', })
    #     self.fields['body'].widget.attrs.update(
    #         {'class': 'form-control', })





