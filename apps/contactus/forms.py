from django import forms
from apps.contactus.tasks import send_contact_email_task



class ContactForm(forms.Form):
    email = forms.EmailField(label="Email", required=True)
    full_name = forms.CharField(label="Full name", required=True)
    subject = forms.CharField(label="Subject", required=True)
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={"row":5}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({"class":"form-control mb-2"})
        self.fields["full_name"].widget.attrs.update({"class":"form-control mb-2"})
        self.fields["subject"].widget.attrs.update({"class":"form-control mb-2"})
        self.fields["message"].widget.attrs.update({"class":"form-control mb-2"})
    
    def send_contact_mail(self):
        send_contact_email_task.delay(
            self.cleaned_data["email"],
            self.cleaned_data["full_name"],
            self.cleaned_data["subject"],
            self.cleaned_data["message"]
        )

        # send_contact_email_task.apply_async(
        #     args=[
        #         self.cleaned_data["email"],
        #         self.cleaned_data["full_name"],
        #         self.cleaned_data["subject"],
        #         self.cleaned_data["message"]
        #     ]
        # )
