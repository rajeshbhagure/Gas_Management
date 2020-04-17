from django import forms

from .models import CustomerModel, PriceModel

from .models import Stockdetails



class DateInput(forms.DateInput):
    input_type = 'date'

class CustomerForm(forms.ModelForm):
    ch = (
        ('Commercial', 'Commercial'),
        ('Dommestic', 'Dommestic'),
    )
    Cy_type = forms.ChoiceField(choices=ch)
    class Meta:
        model=CustomerModel
        fields='__all__'
        widgets={'date_conn':DateInput}



class PriceForm(forms.ModelForm):
    ch=(
        ('Commercial','Commercial'),
        ('Dommestic','Dommestic'),
)
    c_type = forms.ChoiceField(choices=ch)
    class Meta:
        model=PriceModel
        fields='__all__'
        widgets={"date":DateInput}

class DateTimeInput (forms.DateTimeInput):
    input_type = 'date'

class StockForm(forms.ModelForm):
    class Meta:
        model=Stockdetails
        fields='__all__'
        widgets={'s_date':DateTimeInput}

# class BillsForm(forms.ModelForm):
#     class Meta:
#         model=BillingModel
#         fields='__all__'
#         widgets={'bk_date':DateTimeInput,'del_date':DateTimeInput}
#
#

