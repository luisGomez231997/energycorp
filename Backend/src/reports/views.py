from django.shortcuts import render
from rest_framework.views import View

from users.models import Client
from energytransfers.models import Counter
from contract.models import Contract
from rest_framework.response import Response

import json
from django.db.models import F

from django.http import HttpResponse

from .serializers import (
    MoraSerializer,
    ServiceSuspendedSerializer,
   
)

from django.db.models import Count
# Create your views here.

class MoraAndSuspended(View):
    def get(self, request):
        queryset1 =  Contract.objects.exclude(
            interes_mora__iexact=0.0).filter(
                client__user__is_active=True).annotate(
                        id=F( 'client__id'),
                        name= F('client__user__name')
                    
                ).values('id','interes_mora', 'name')
       
        queryset = Contract.objects.exclude(counter__is_active=True)
       
        query = ServiceSuspendedSerializer(
            queryset,many=True
        ).data
       

       
        dicc= []
        for i in range(len(query)):
            datos = {

                "id": "",
                "name":"",
                "codeCounter": "",
                "is_active":""
            }
            datos['id']= query[i]['client']['id']
            datos['name']= query[i]['client']['user']['name']
            datos['codeCounter']= query[i]['counter']['codeCounter']
            datos['is_active']= query[i]['counter']['is_active']
           
            dicc.append(datos)
        
        response={
            "mora":"",
            "suspended":""
        }
        response['mora']=list(queryset1)
        response['suspended']=dicc


        return HttpResponse(json.dumps(response))   

class TopFiveCounters(View):
     def get(self, request):
        queryset1 =   Counter.objects.all(

        ).order_by('-value')[:5].values('codeCounter',
            'latitudeCounter',
            'lengthCounter',
            'value',
            'addressCounter',
            'stratum',
            'transformatorCounter')
        queryset2 =   Counter.objects.all(
        ).order_by('value')[:5].values('codeCounter',
            'latitudeCounter',
            'lengthCounter',
            'value',
            'addressCounter',
            'stratum',
            'transformatorCounter')
        
        response={
            "topfive+":"" ,
            "topfive-":""
        }
        response['topfive+']=list(queryset1)
        response['topfive-']=list(queryset2)
   

        return HttpResponse(json.dumps(response))  

class QuantityCounterTransformator(View):
    def get(self, request):
        queryset=Counter.objects.values(
            'transformatorCounter').annotate(
                total=Count('codeCounter')).filter(
                    transformatorCounter__is_active=True
                )



        return HttpResponse(json.dumps(list(queryset)))     