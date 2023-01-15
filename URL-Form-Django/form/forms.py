from django import forms
from django import forms
from form.models import Form


class Form(forms.ModelForm):
    class Meta:
        model = Form
        fields = "__all__"

class classform(forms.Form):
    namac = forms.CharField(
        label = 'Nama Lengkap',
        widget = forms.TextInput(
            attrs={
                'class':'field padding-bottom--24',
                'type':'nama',
                'placeholder':'Masukkan Nama',
            }
        )
    )
    alamatc = forms.CharField(
        label = 'Alamat',
        widget = forms.TextInput(
            attrs={
                'class':'field padding-bottom--24',
                'type':'alamat',
                'placeholder':'Masukkan Alamat',
            }
        )
    )
    tgl_lahirc = forms.CharField(
        label = 'Tanggal Lahir',
        widget = forms.TextInput(
            attrs={
                'class':'field padding-bottom--24',
                'type':'tgl_lahir',
                'placeholder':'Masukkan Tanggal Lahir',
            }
        )
    )
    emailc = forms.EmailField(
        label = 'Email',
        widget = forms.TextInput(
            attrs={
                'class':'field padding-bottom--24',
                'type':'email',
                'placeholder':'Masukkan Email',
            }
        )
    )
    # komentar = forms.CharField(widget = forms.Textarea, max_length = 100, required = False)