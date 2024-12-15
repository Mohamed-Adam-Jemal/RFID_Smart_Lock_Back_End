from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import RFIDUser, AccessLog
from .serializers import RFIDUserSerializer, AccessLogSerializer
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'message': 'Invalid username or password'}, status=400)
    return JsonResponse({'message': 'Invalid method'}, status=405)

@api_view(['GET'])
def get_users(request):
    users = RFIDUser.objects.all()
    serializer = RFIDUserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_user(request):
    serializer = RFIDUserSerializer(data=request.data)
    print(request.data)  # Log the incoming data to check its format
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user(request):
    try:
        user = RFIDUser.objects.get(user_id=request.data['user_id'])
        serializer = RFIDUserSerializer(user, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except RFIDUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_access_log(request):
    serializer = AccessLogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_access_log(request):
    access_log = AccessLog.objects.all()
    serializer = AccessLogSerializer(access_log, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_user(request, user_id):
    try:
        # Try to get the user object
        user = RFIDUser.objects.get(user_id=user_id)
        # Delete the user
        user.delete()
        # Return a success response with status 200
        return Response({"message": "User deleted successfully!"}, status=status.HTTP_200_OK)
    
    except RFIDUser.DoesNotExist:
        # If the user doesn't exist, return a 404 response
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)