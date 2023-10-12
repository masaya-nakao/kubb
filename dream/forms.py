from django import forms
from .models import Preference_GroupMessage, Agenda_GroupMessage

class Preference_GroupMessageForm(forms.Form):
    class Meta:
        model = Preference_GroupMessage
        fields = ('body')
        labels = {'body':'body',}
        
class Agenda_GroupMessageForm(forms.Form):
    class Meta:
        model = Agenda_GroupMessage
        fields = ('body')
        labels = {'body':'body',}
    