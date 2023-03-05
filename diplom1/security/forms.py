from django import forms
class Fio(forms.Form):
    fio_client = forms.CharField()
    gender = forms.CharField()
    passport_number_client=forms.CharField()
    date_of_birthday_client=forms.DateField()
    phone_number_client=forms.CharField()
    client_type=forms.CharField()
    #link_photo1_client = forms.ImageField()

    def getfio(self):
        values=self.data['fio_client']
        return values

    def getgender(self):
        values=self.data['gender']
        return values

    def getpassport(self):
        values=self.data['passport_number_client']
        return values

    def getdate(self):
        values=self.data['date_of_birthday_client']
        return values
    
    def getphone(self):
        values=self.data['phone_number_client']
        return values

    def gettype(self):
        values=self.data['client_type']
        return values

    # def getphoto(self):
    #     values=self.data['link_photo1_client']
    #     return values

class Search_client(forms.Form):
    fio_client = forms.CharField()
    gender = forms.CharField()
    passport_number_client=forms.CharField()
    age=forms.CharField()
    phone_number_client=forms.CharField()
    
    def getfio(self):
        values=self.data['fio_client']
        return values

    def getgender(self):
        values=self.data['gender']
        return values

    def getpassport(self):
        values=self.data['passport_number_client']
        return values

    def getage(self):
        values=self.data['age']
        return values
    
    def getphone(self):
        values=self.data['phone_number_client']
        return values
    

