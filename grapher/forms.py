from django import forms


class chartForm(forms.Form):
    location = forms.CharField(widget=forms.TextInput(attrs={ 'id': 'location', 'name': 'location', 'class': 'chartInput'}), label='Location', max_length=100, required=False)
    
    day = forms.ChoiceField(widget=forms.Select(attrs={ 'id': 'day', 'name': 'day', 'class': 'chartInput'}), label='Day', choices=[(
        'M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('Th', 'Thursday'), ('F', 'Friday')])
    
    quarter = forms.ChoiceField(widget=forms.Select(attrs={ 'id': 'Quarter', 'name': 'Quarter', 'class': 'chartInput'}), label='Quarter', choices=[
                                ('Current', 'Current'), ('Past', 'Past')])
    
    sort = forms.ChoiceField(widget=forms.Select(attrs={ 'id': 'Sort Order', 'name': 'Sort Order', 'class': 'chartInput'}), label='Sort', choices=[('location', 'Location 🔼'), (
        '-location', 'Location 🔽'), ('starttime', 'Start Time 🔼'), ('-starttime', 'Start Time 🔽')])
