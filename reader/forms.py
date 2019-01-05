from django import forms
from django.forms import ModelForm, TextInput
from django.utils.translation import gettext_lazy as _

from . import models, fields


class SubscriptionTagsForm(ModelForm):

    class Meta:
        model = models.Subscription
        fields = ['tags']


class BoardForm(ModelForm):

    class Meta:
        model = models.Board
        fields = ['name', 'tags']
        widgets = {
            'tags': TextInput(attrs={'type': 'tags',
                                     'placeholder': _('Add tags')}),
        }


class UploadOPMLFileForm(forms.Form):
    opml_uris = fields.OPMLField(max_length=1024 * 1024)
