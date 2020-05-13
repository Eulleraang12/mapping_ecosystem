from django import forms

class RegistroForm(forms.Form):

    Empresa = forms.CharField(max_length=30,
                              widget=forms.TextInput(attrs={'class':'form-control',
                                                            'placeholder':'Empresa/Startup'
                                                            }
                            ))


    Email = forms.EmailField(max_length=30,
                              widget=forms.TextInput(attrs={'class':'form-control',
                                                            'placeholder':'Email'
                                                            }
                            ))
    Site = forms.CharField(max_length=30,
                              widget=forms.TextInput(attrs={'class':'form-control',
                                                            'placeholder':'Site'
                                                            }
                            ))

    Rua = forms.CharField(max_length=30,
                              widget=forms.TextInput(attrs={'class':'form-control',
                                                            'placeholder':'Rua'
                                                            }
                            ))
    Bairro = forms.CharField(max_length=30,
                              widget=forms.TextInput(attrs={'class':'form-control',
                                                            'placeholder':'Bairro'
                                                            }
                            ))
    Cidade = forms.CharField(max_length=30,
                              widget=forms.TextInput(attrs={'class':'form-control',
                                                            'placeholder':'Cidade'
                                                            }
                            ))
    Estado = forms.CharField(max_length=30,
                              widget=forms.TextInput(attrs={'class':'form-control',
                                                            'placeholder':'Estado'
                                                            }
                            ))


    CEP = forms.CharField(max_length=30,
                              widget=forms.TextInput(attrs={'class':'form-control',
                                                            'placeholder':'CEP'
                                                            }
                            ))
    CNPJ = forms.CharField(max_length=30,
                              widget=forms.TextInput(attrs={'class':'form-control',
                                                            'placeholder':'CNPJ'
                                                            }
                            ))