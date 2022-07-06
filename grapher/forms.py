from django import forms

class chartForm(forms.Form):
    location = forms.CharField(label='Location', max_length=100, required = False)
    day = forms.ChoiceField(label='Day', choices=[('M','Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('Th', 'Thursday'), ('F', 'Friday')])
    quarter = forms.ChoiceField(label='Quarter', choices=[('Current', 'Current'), ('Past', 'Past')])
    sort = forms.ChoiceField(label='Sort', choices=[('location', 'Location 🔼'), ('-location', 'Location 🔽'), ('starttime', 'Start Time 🔼'), ('-starttime', 'Start Time 🔽')])