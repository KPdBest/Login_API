from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from Test.models import Sudo,User

def run(request):
	if request.method == 'POST' :
		data = json.loads(request.body)
		obj=User.objects.all()
		for x in obj :
			if(x.Email==data['Email'] and x.Password==data['Password']):
				query=User.objects.filter(Email=data['Email']).values('link__Fname','link__Fa_Name','link__Mobile_no','link__Email','link__Fa_Mobile_no','link__Gender')
				return JsonResponse(list(query),safe=False)
			elif(x.Email==data['Email'] and x.Password!=data['Password']):
				data1={"Status":"Wrongpass"}
				return JsonResponse(data1)
			
			
		try:
			query2= Sudo.objects.create(Fname=data['Fname'],Fa_Name=data['Fa_name'],Mobile_no=data['Mobile_no'],Email=data['Email'],Gender=data['Gender'],Fa_Mobile_no=data['Fa_Mobile_no'])
			query3=User.objects.create(Email=data['Email'],Password=data['Password'], link=query2)
			data2={"Status":"YES"}
			return JsonResponse(data2)

		except:
			q={"Status":"Invalid"}
			return JsonResponse(q)
