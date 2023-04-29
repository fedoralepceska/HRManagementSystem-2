from django import forms
from HRManagementSystemApp.models import Department, CustomUser, Request


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']


class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'department', 'date_employment', 'usedVacDays', 'usedSickLeave', 'usedFreeDays']


class RequestForm(forms.ModelForm):
    num_days = forms.IntegerField()
    request_type = forms.ChoiceField(choices=[('free', 'Free Days'), ('sick', 'Sick Leave'), ('vacation', 'Vacation Days')])

    class Meta:
        model = Request
        fields = ('num_days', 'request_type',)

    def save(self, commit=True, user=None):
        request = super().save(commit=False)
        request.user = user
        request.save()

        if self.cleaned_data['request_type'] == 'free':
            user.usedFreeDays += self.cleaned_data['num_days']
        elif self.cleaned_data['request_type'] == 'sick':
            user.usedSickLeave += self.cleaned_data['num_days']
        elif self.cleaned_data['request_type'] == 'vacation':
            user.usedVacDays += self.cleaned_data['num_days']
        user.save()

        return request
