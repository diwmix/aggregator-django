from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes 
from .serializers import UserSerializer, PatchUserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
import cloudinary.uploader

@api_view(['POST'])
def user_register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Both username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if not user:
            if '@' in username:
                username = username.lower()
                try:
                    user = CustomUser.objects.get(email=username)
                    if not user.check_password(password):
                        user = None 
                except ObjectDoesNotExist:
                    pass 

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'imageUrl': user.imageUrl.url,
        'isCreator': user.isCreator,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def users_id(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    serializer = UserSerializer(user)
    response = Response(serializer.data)
    return response

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def user_update_profile(request):
    user = request.user
    serializer = PatchUserSerializer(user, data=request.data, partial=True)

    if serializer.is_valid():
        image = request.FILES.get('imageUrl')  # Access the uploaded image
        if image:
            uploaded_image = cloudinary.uploader.upload(image)  # Upload to Cloudinary
            serializer.validated_data['imageUrl'] = uploaded_image['secure_url'][37:]  # Update URL
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def users(request):
    if request.method == 'GET':
        queryset = CustomUser.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
# accounts/views.py

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

@api_view(['POST'])
def forgot_password(request):
    email = request.data.get('email')
    if email:
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({'error': 'No user found with this email address.'}, status=status.HTTP_404_NOT_FOUND)

        # Generate token
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        # Create reset password link
        reset_password_link = f'http://localhost:4000/reset-password/{uid}/{token}/'

        # Send reset password email
        subject = 'Password Reset Request'
        message = render_to_string('email/reset_password_email.html', {
            'user': user,
            'reset_password_link': reset_password_link,
        })
        send_mail(subject, message, 'sanuaburdun15@gmail.com', [email])

        return Response({'success': 'Reset password instructions have been sent to your email.'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)
