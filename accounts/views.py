
import environ
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

from accounts.models import User, StudentProfile
from core.models import Classroom
from student_core.models import Enroll


env = environ.Env(
    DEBUG=(bool, False)
)
# OUTDATED
class StudentRegister(viewsets.ViewSet):
    '''
    Allows a student to sign themselves up as a new student in the classroom
    '''
    permission_classes = [AllowAny]

    def create(self, request):
        # Obtains the classroom code, sets up the index number of the student and updates the classroom
        classroom = Classroom.objects.get(code=request.data['code'])
        new_index = max(classroom.student_indexes) + 1
        classroom.student_indexes = classroom.student_indexes + [new_index]
        classroom.save()

        # Creates a new user profile
        student = User(
            username=request.data['code']+'_'+str(new_index), user_type=1)
        student.set_password(str(new_index))
        student.save()

        # Sets up the student profile and saves it
        student_profile = StudentProfile(
            student=student, assigned_class_code=request.data['code'], index=new_index,
            created_by_student=True,
            name=request.data['name']
        )
        student_profile.save()

        enroll = Enroll(
            studentUserID=request.data['user_id'],classroom=request.data['code'], studentIndex=new_index, score=0
        )
        enroll.save()

        return Response({'code': request.data['code'], 'index': new_index})

class TeacherSignUp(viewsets.ViewSet):
    permission_classes = [AllowAny]
    def create(self, request):
        passcode = request.data.get('passcode')
        if passcode != env('PASSCODE'):
            return Response({'error': 'Invalid passcode.'}, status=status.HTTP_400_BAD_REQUEST)

        teacher = User(username=request.data['username'], user_type=2, email=request.data['email'], first_name=request.data['first_name'])
        teacher.set_password(request.data['password'])
        teacher.save()

        return Response({'Account': 'Teacher','Username': request.data['username'], 'First Name': request.data['first_name']})


class StudentSignUp(viewsets.ViewSet):
    permission_classes = [AllowAny]
    
    def create(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        password = request.data.get('password')
        
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        
        student = User(username=username, user_type=3, email=email, first_name=first_name)
        student.set_password(password)
        student.save()

        return Response({'Account': 'Student', 'Username': username, 'First Name': first_name})

# OUTDATED
class StudentJoinClass(viewsets.ViewSet):
    permission_classes = [AllowAny]
    def create(self, request):
        enroll = Enroll(
            studentUserID=request.data['user_id'],classroom=request.data['code'], studentIndex=request.data['index'], score=0
        )
        enroll.save()

        return Response({'Student Account': 'studentUserId', 'Classroom': 'classroom', 'Index': 'studentIndex'})

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        inputUserType = request.data.get('userType')
        inputUserCode = 0
        if inputUserType == "teacher":
            inputUserCode = 2
        elif inputUserType == "student":
            inputUserCode = 3
        if user.user_type != inputUserCode:
            raise AuthenticationFailed('Invalid user type.')

        tokens = serializer.validated_data
        response_data = {
            'access': str(tokens['access']),
            'refresh': str(tokens['refresh']),
            'userType': user.user_type,
        }

        print(response_data)

        return Response(response_data)

class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
      

        tokens = serializer.validated_data
        response_data = {
            'access': str(tokens['access']),
            # 'refresh': str(tokens['refresh']),
        }

        print(response_data)

        return Response(response_data)

class CustomTokenVerifyView(TokenVerifyView):
    pass
