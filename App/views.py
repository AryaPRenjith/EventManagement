from django.shortcuts import render
from django .http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Events
from .serializer import EventSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.                               #Function Based CRUD Operations using csrf_exempt and api_view 

#@csrf_exempt
@api_view(['GET','POST'])

def Event_list(request):
    if request.method == 'GET':
        events=Events.objects.all()
        serializer=EventSerializer(events, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        # data=JSONParser().parse(request)
        # serializer=EventSerializer(data=data)
        serializer=EventSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data,status=201)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        # return JsonResponse(serializer.errors,status=400)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
@api_view(['GET','PUt','DELETE'])
def Event_Details(request,pk):
    try:
        eve=Events.objects.get(pk=pk)
    except Events.DoesNotExist:
        # return HttpResponse(status=404)
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        
        serializer=EventSerializer(eve)
        # return JsonResponse(serializer.data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # data=JSONParser().parse(request)
        # serializer=EventSerializer(eve,data=data)
        serializer=EventSerializer(eve,data=request.data)

        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data)
            return Response(serializer.data)
        # return JsonResponse(serializer.errors,status=400)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        eve.delete()
        # return HttpResponse(status=204)
        return Response(status=status.HTTP_204_NO_CONTENT)



