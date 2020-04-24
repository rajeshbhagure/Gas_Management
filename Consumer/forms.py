
from django import forms



from .models import TransactionModel


class DateInput(forms.DateInput):
    input_type = 'date'


class TransactionForm(forms.ModelForm):
    class Meta:
        model=TransactionModel
        fields='__all__'
        widgets={"datetime":DateInput}
