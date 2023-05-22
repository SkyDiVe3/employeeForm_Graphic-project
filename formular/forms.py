from django import forms
from .models import Employee

class CustomTextInput(forms.TextInput):
    def __init__(self, placeholder, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs['class'] = 'form-control my-2'  # Add 'form-control' class for styling
        self.attrs['placeholder'] = placeholder  # Set the placeholder attribute
        self.attrs['required'] = True  # Set the field as required

class CustomSelect(forms.Select):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs['class'] = 'form-select my-1'  # Add 'form-select' class for styling
        self.attrs['required'] = True  # Set the field as required

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        """
        Create an option for the select field.

        This method overrides the base create_option method to add custom
        functionality. In this case, it sets the 'selected' attribute to
        the default option, represented by an empty value.

        Args:
            name (str): The name of the field.
            value (str): The value of the option.
            label (str): The display label for the option.
            selected (bool): Whether the option is selected.
            index (int): The index of the option.
            subindex (int): The subindex of the option.
            attrs (dict): Additional attributes for the option.

        Returns:
            dict: The option with custom attributes.

        """
        option = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
        if value == '':
            option['attrs']['selected'] = 'selected'  # Set the default option as selected
        return option

class EmployeeForm(forms.Form):
    jobTitles = list(Employee.JOB_CHOICES)
    default_choice = ('', "Choose..")
    full_job_choices = [default_choice] + jobTitles

    firstname = forms.CharField(label='First Name', max_length=30, widget=CustomTextInput(placeholder='Name'))
    lastname = forms.CharField(label='Last Name', max_length=30, widget=CustomTextInput(placeholder='Lastname'))

    gender = forms.ChoiceField(
        label='Gender:',
        choices=[('other', 'Other'), ('male', 'Male'), ('female', 'Female')],
        widget=CustomSelect()
    )


    jobCategories = forms.ChoiceField(
        label='Job Title:',
        choices=full_job_choices,
        widget=CustomSelect()
    )
