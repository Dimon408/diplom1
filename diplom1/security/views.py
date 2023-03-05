from django.http import HttpResponse
from django.shortcuts import render 
from .forms import Fio, Search_client
from .models import Client_Time, Worker
import datetime, timedelta
from PIL import Image
import face_recognition

import matplotlib.pyplot as plt

def index(request):
    return HttpResponse("Привет мир!!!!!!")

def main(request):
    return render(request, "security/main.html")
    

def client_enter(request):
    print('start')
    if request.method=="POST":
        print('post1')
        Client_Time1=Client_Time()
        print('post2')
        form = Fio(request.POST)
        print('post3')
        if form.is_valid():
            print('post4')
            print('Форма правильная')
            print(form.cleaned_data['fio_client'])
            Client_Time1.fio_client=form.cleaned_data['fio_client']

            print(form.cleaned_data['gender'])
            if(form.cleaned_data['gender']=='Женский'):
                Client_Time1.gender=1
            else:
                Client_Time1.gender=0
            

            print(form.cleaned_data['passport_number_client'])
            Client_Time1.passport_number_client=form.cleaned_data['passport_number_client']

            print(form.cleaned_data['date_of_birthday_client'])
            Client_Time1.date_of_birthday_client=form.cleaned_data['date_of_birthday_client']

            print(form.cleaned_data['phone_number_client'])
            Client_Time1.phone_number_client=form.cleaned_data['phone_number_client']

            print(form.cleaned_data['client_type'])
            if form.cleaned_data['client_type']=='Постоянный':
                Client_Time1.client_type=0
            elif form.cleaned_data['client_type']=='Временный':
                Client_Time1.client_type=1
            elif form.cleaned_data['client_type']=='Одноразовый':
                Client_Time1.client_type=2
            Client_Time1.link_photo1_client = request.FILES.get('myfile1')#request.getFILES['myfile1'] 
            print(Client_Time1.link_photo1_client)
            all_clients=Client_Time.objects.all()   
            Client_Time1.id_client=len(all_clients)+1
            Client_Time1.save()

            print(Client_Time1)

            return render(request, "security/client_enter.html", {'form':form})

    else:
        print('get')
        form=Fio()
        return render(request, "security/client_enter.html", {'form':form})


    return render(request, "security/client_enter.html")

def search_client(request):
    print('1')
    if request.method=="POST":
        print('post')
        form=Search_client(request.POST)
        # if form.is_valid():
        #     print('2')
        #     all_clients=list(Client_Time.objects.all())

        #     if form.cleaned_data['fio_client']!=None:
        #         fio_filter=form.cleaned_data['fio_client']
        #         fio_filtered_clients=list(Client_Time.objects.filter(fio_client = fio_filter))
        #         all_clients.intersection_update(fio_filtered_clients)
            
        #     if form.cleaned_data['gender']!=None:
        #         gender_filter=form.cleaned_data['gender']
        #         gender_filtered_clients=list(Client_Time.objects.filter(gender = gender_filter))
        #         all_clients.intersection_update(gender_filtered_clients)

        #     if form.cleaned_data['passport_number_client']!=None:
        #         passport_number_filter=form.cleaned_data['passport_number_client']
        #         passport_number_filtered_clients=list(Client_Time.objects.filter(passport_number_client = passport_number_filter))
        #         all_clients.intersection_update(passport_number_filtered_clients)

        #     if form.cleaned_data['age']!=None:
        #         gender_filter=form.cleaned_data['age']
        #         age_min=gender_filter.split('-')[0]
        #         age_max=gender_filter.split('-')[1]
        #         age_min_date=datetime.now() - timedelta(years=age_min)
        #         age_max_date=datetime.now() - timedelta(years=age_max)
        #         age_min_filtered_clients=list(Client_Time.objects.filter(date_of_birthday_client__gte = age_min_date))
        #         age_max_filtered_clients=list(Client_Time.objects.filter(date_of_birthday_client__lte = age_min_date))
        #         all_clients.intersection_update(age_min_filtered_clients)
        #         all_clients.intersection_update(age_max_filtered_clients)
            
        #     if form.cleaned_data['phone_number_client']!=None:
        #         phone_filter=form.cleaned_data['phone_number_client']
        #         phone_filtered_clients=list(Client_Time.objects.filter(phone_number_client = phone_filter))
        #         all_clients.intersection_update(phone_filtered_clients)

        print('2')
        all_clients=set(Client_Time.objects.all())

        if request.POST.get("fio_client")!='':
            fio_filter=request.POST.get("fio_client")
            fio_filtered_clients=set(Client_Time.objects.filter(fio_client = fio_filter))
            all_clients.intersection_update(fio_filtered_clients)
          
        if request.POST.get('gender')!='':
            gender_filter=request.POST.get('gender')
            if ( gender_filter=="Мужской"):
                 gender_filter=0
            else:
                 gender_filter=1
            gender_filtered_clients=set(Client_Time.objects.filter(gender = gender_filter))
            print(gender_filtered_clients)
            print(all_clients)
            all_clients.intersection_update(gender_filtered_clients)

        if request.POST.get('passport_number_client')!='':
            passport_number_filter=request.POST.get('passport_number_client')
            passport_number_filtered_clients=set(Client_Time.objects.filter(passport_number_client = passport_number_filter))
            all_clients.intersection_update(passport_number_filtered_clients)

        if request.POST.get('age')!='':
            age_filter=request.POST.get('age')
            age_min=age_filter.split('-')[0]
            age_max=age_filter.split('-')[1]
            age_min_date=datetime.now() - timedelta(years=age_min)
            age_max_date=datetime.now() - timedelta(years=age_max)
            age_min_filtered_clients=set(Client_Time.objects.filter(date_of_birthday_client__gte = age_min_date))
            age_max_filtered_clients=set(Client_Time.objects.filter(date_of_birthday_client__lte = age_max_date))
            all_clients.intersection_update(age_min_filtered_clients)
            all_clients.intersection_update(age_max_filtered_clients)
            
        if request.POST.get('phone_number_client')!='':
            phone_filter=request.POST.get('phone_number_client')
            phone_filtered_clients=list(Client_Time.objects.filter(phone_number_client = phone_filter))
            all_clients.intersection_update(phone_filtered_clients)

        output=[]

        if all_clients=={}:
            output={}
        else:
            if request.FILES.get('myfile1')!=None:
                app_client=Client_Time()
                print(request.FILES.get('myfile1'))
                print(request.FILES.get('myfile1'))
                app_client.link_photo1_client = request.FILES.get('myfile1')
                known_image = face_recognition.load_image_file(app_client.link_photo1_client)
                print(known_image)
                for client in all_clients:
                    unknown_image = face_recognition.load_image_file(client.link_photo1_client)
                    print(unknown_image)
                    baixiaona_encoding = face_recognition.face_encodings(known_image)[0]
                    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
                    results = face_recognition.compare_faces([baixiaona_encoding], unknown_encoding)
            
                    if results[0] == True:
                        output.append(client)
            else:
                output=all_clients

        
        context={
                'result_rearch' : output
                }

        return render(request, "security/search_client.html", context=context)
    else:
        print('get')
        return render(request, "security/search_client.html")
    

    
def search_worker(request):
    print('1')
    if request.method=="POST":
        print('post')
        form=Search_client(request.POST)
        # if form.is_valid():
        #     print('2')
        #     all_clients=list(Client_Time.objects.all())

        #     if form.cleaned_data['fio_client']!=None:
        #         fio_filter=form.cleaned_data['fio_client']
        #         fio_filtered_clients=list(Client_Time.objects.filter(fio_client = fio_filter))
        #         all_clients.intersection_update(fio_filtered_clients)
            
        #     if form.cleaned_data['gender']!=None:
        #         gender_filter=form.cleaned_data['gender']
        #         gender_filtered_clients=list(Client_Time.objects.filter(gender = gender_filter))
        #         all_clients.intersection_update(gender_filtered_clients)

        #     if form.cleaned_data['passport_number_client']!=None:
        #         passport_number_filter=form.cleaned_data['passport_number_client']
        #         passport_number_filtered_clients=list(Client_Time.objects.filter(passport_number_client = passport_number_filter))
        #         all_clients.intersection_update(passport_number_filtered_clients)

        #     if form.cleaned_data['age']!=None:
        #         gender_filter=form.cleaned_data['age']
        #         age_min=gender_filter.split('-')[0]
        #         age_max=gender_filter.split('-')[1]
        #         age_min_date=datetime.now() - timedelta(years=age_min)
        #         age_max_date=datetime.now() - timedelta(years=age_max)
        #         age_min_filtered_clients=list(Client_Time.objects.filter(date_of_birthday_client__gte = age_min_date))
        #         age_max_filtered_clients=list(Client_Time.objects.filter(date_of_birthday_client__lte = age_min_date))
        #         all_clients.intersection_update(age_min_filtered_clients)
        #         all_clients.intersection_update(age_max_filtered_clients)
            
        #     if form.cleaned_data['phone_number_client']!=None:
        #         phone_filter=form.cleaned_data['phone_number_client']
        #         phone_filtered_clients=list(Client_Time.objects.filter(phone_number_client = phone_filter))
        #         all_clients.intersection_update(phone_filtered_clients)

        print('2')
        all_clients=set(Worker.objects.all())

        if request.POST.get("fio_client")!='':
            fio_filter=request.POST.get("fio_client")
            fio_filtered_clients=set(Worker.objects.filter(fio_client = fio_filter))
            all_clients.intersection_update(fio_filtered_clients)
          
        if request.POST.get('gender')!='':
            gender_filter=request.POST.get('gender')
            if ( gender_filter=="Мужской"):
                 gender_filter=0
            else:
                 gender_filter=1
            gender_filtered_clients=set(Worker.objects.filter(gender = gender_filter))
            print(gender_filtered_clients)
            print(all_clients)
            all_clients.intersection_update(gender_filtered_clients)

        if request.POST.get('passport_number_client')!='':
            passport_number_filter=request.POST.get('passport_number_client')
            passport_number_filtered_clients=set(Worker.objects.filter(passport_number_client = passport_number_filter))
            all_clients.intersection_update(passport_number_filtered_clients)

        if request.POST.get('age')!='':
            age_filter=request.POST.get('age')
            age_min=age_filter.split('-')[0]
            age_max=age_filter.split('-')[1]
            age_min_date=datetime.now() - timedelta(years=age_min)
            age_max_date=datetime.now() - timedelta(years=age_max)
            age_min_filtered_clients=set(Worker.objects.filter(date_of_birthday_client__gte = age_min_date))
            age_max_filtered_clients=set(Worker.objects.filter(date_of_birthday_client__lte = age_max_date))
            all_clients.intersection_update(age_min_filtered_clients)
            all_clients.intersection_update(age_max_filtered_clients)
            
        if request.POST.get('phone_number_client')!='':
            phone_filter=request.POST.get('phone_number_client')
            phone_filtered_clients=list(Worker.objects.filter(phone_number_client = phone_filter))
            all_clients.intersection_update(phone_filtered_clients)

        output=[]

        if all_clients=={}:
            output={}
        else:
            if request.FILES.get('myfile1')!=None:
                app_client=Worker()
                print(request.FILES.get('myfile1'))
                print(request.FILES.get('myfile1'))
                app_client.link_photo1_client = request.FILES.get('myfile1')
                known_image = face_recognition.load_image_file(app_client.link_photo1_client)
                print(known_image)
                for client in all_clients:
                    unknown_image = face_recognition.load_image_file(client.link_photo1_client)
                    print(unknown_image)
                    baixiaona_encoding = face_recognition.face_encodings(known_image)[0]
                    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
                    results = face_recognition.compare_faces([baixiaona_encoding], unknown_encoding)
            
                    if results[0] == True:
                        output.append(client)
            else:
                output=all_clients

        
        context={
                'result_rearch' : output
                }

        return render(request, "security/search_worker.html", context=context)
    else:
        print('get')
        return render(request, "security/search_worker.html")

def error(request):
    return render(request, "security/error.html")

def search_worker(request):
    return render(request, "security/search_worker.html")

def worker_enter(request):
    return render(request, "security/worker_enter.html")