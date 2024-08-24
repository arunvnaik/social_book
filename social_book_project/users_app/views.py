from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.shortcuts import render ,redirect
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
# from rest_framework.permissions import IsAuthenticated
# from .serializers import UploadedFileSerializer
from .models import UploadedFile
from .forms import UploadFileForm
from django.contrib.auth.decorators import login_required
User = get_user_model()
from rest_framework.permissions import IsAuthenticated
from .serializers import UploadedFileSerializer
from .decorators import check_uploaded_files
from django.core.mail import send_mail 

# class RegisterView(APIView):
#     def get(self, request):
#         return render(request, 'register.html') 

#     def post(self, request):
#         # import pdb;pdb.set_trace()
#         # permission_classes = []
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Send registration success email
            subject = 'Registration Successful'
            message = f'Hi {user.username},\n\nYou have successfully registered on our platform.'
            from_email = 'arunvnaik2002@gmail.com'
            recipient_list = [user.email]

            try:
                send_mail(subject, message, from_email, recipient_list)
            except Exception as e:
                return Response({"message": "User registered successfully, but failed to send email.", "error": str(e)}, status=status.HTTP_201_CREATED)

            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "message": "Login successful."})

# from django.http import HttpResponse

# def send_test_email(request):
#     subject = 'Test Email'
#     message = 'This is a test email sent from Django.'
#     from_email = 'arunvnaik2002@gmail.com'  # Your Gmail address
#     recipient_list = ['recipient-email@example.com']   # Recipient's email address

#     send_mail(subject, message, from_email, recipient_list)

#     return HttpResponse('Email sent successfully!')

# from django.core.mail import send_mail

# class LoginView(ObtainAuthToken):
#     serializer_class = LoginSerializer

#     def get(self, request):
#         return render(request, 'login.html')

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
        
#         # Send a login success email
#         subject = 'Login Successful'
#         message = f'Hi {user.username}, you have successfully logged in.'

#         from_email = 'arunvnaik2002@gmail.com'
#         recipient_list = [user.email]

#         send_mail(subject, message, from_email, recipient_list)

#         return Response({"token": token.key, "message": "Login successful."}) 


class AuthorsSellersView(APIView):
    def get(self, request):
        # Filter users with public_visibility set to True
        users = User.objects.filter(public_visibility=True)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data) 
    
class UserListView(APIView):
    def get(self, request):
        # Filter users with public_visibility set to True and username starting with 'a' or 'A'
        users = User.objects.filter(public_visibility=True, username__istartswith='a')
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

# class UploadFileView(APIView):
#     # permission_classes = [IsAuthenticated]

#     def post(self, request):
#         serializer = UploadedFileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response({"message": "File uploaded successfully."}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UploadedFilesListView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         files = UploadedFile.objects.filter(user=request.user)
#         serializer = UploadedFileSerializer(files, many=True)
#         return Response(serializer.data)


@login_required
def upload_books(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            uploaded_file.save()
            return redirect('upload_books')
    else:
        form = UploadFileForm()

    uploaded_files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'uplode_book.html', {'form': form, 'uploaded_files': uploaded_files})




from django.http import JsonResponse
from sqlalchemy import text
from .sql import engine, Session

def fetch_data_view(request):
    # SQL query to fetch data from your table
    sql_query = "SELECT * FROM test;"

    # Create a session and execute the query
    with Session() as session:
        result = session.execute(text(sql_query))
        rows = result.fetchall()

    # Convert each row to a dictionary
    data = [dict(row._mapping) for row in rows]

    # Return data as JSON for simplicity
    return JsonResponse({'data': data})

class UserFilesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Fetch files uploaded by the authenticated user
        uploaded_files = UploadedFile.objects.filter(user=request.user)
        serializer = UploadedFileSerializer(uploaded_files, many=True)
        return Response(serializer.data) 
    
    
    
@check_uploaded_files
def my_books_view(request):
    files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'my_books.html', {'files': files})  


