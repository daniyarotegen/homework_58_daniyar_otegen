from django import forms
from django.core.exceptions import ValidationError
from .models import Issue, Type, Status


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'type']
        labels = {
            'summary': 'Summary',
            'description': 'Description',
            'status': 'Status',
            'type': 'Type'
        }

    status = forms.ModelChoiceField(queryset=Status.objects.all())
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all())

    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        if len(summary) < 2:
            raise ValidationError('Summary must be longer than 2 symbols')
        return summary
