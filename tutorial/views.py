from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.urls import reverse
import psycopg2
from django.templatetags.static import static
from django.conf import settings as django_settings
import os


from .models import person

# Create your views here.

def index(request):
    return render(request, "tutorial/index.html", {})

def dock(request):
    return render(request, "tutorial/dock.html", {})


def nana(request):

    name = request.POST['Name']
    email = request.POST['Email']
    city = request.POST['City']
    d = {'Email': email, 'City': city}

    obj, created = person.objects.update_or_create( Name=name, defaults=d,)

    if created:
        messages.info(request, 'New User {} has been created'.format(name))
        #return render(request, "tutorial/index.html", {})
        #return redirect(dock)
        return HttpResponseRedirect('/tutorial/dock')

    else:
        messages.info(request, 'Existing user has been modified')
        #return render(request, "tutorial/index.html", {})
        return HttpResponseRedirect('/tutorial/dock')

def postgres(request):
    return render(request, "tutorial/postgres.html", {})
    #return HttpResponseRedirect('/tutorial/postgres')

def postgresquery(request):
    
    output = ''
    query = request.POST['query']
    try:
        conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="dvdrental",
        user="postgres",
        password="Admin@123")
        cursor = conn.cursor()
        cursor.execute(query)
        output = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description]
    except Exception as e:
        return render(request, "tutorial/postgres.html", {'emessages':e})
    
    finally:
        cursor.close()
        conn.close()
    
    return render(request, "tutorial/postgres.html", {'messages':output,'cname':colnames})

def mysql(request):
    return render(request, "tutorial/mysql.html", {})

def dataframe(request):
    import pandas as pd
    query = request.POST.get('query', False)
    df = pd.read_csv('student.csv')
    #result = exec("{}".format(query))
    code = "result =" + query
    glo = {'df':df}
    loc= {}
    exec(code, glo, loc)
    print(df.size)
    return render(request, "tutorial/dataframe.html", {'message':loc['result']})

def timer(request):
    return render(request, "tutorial/timer.html" )


