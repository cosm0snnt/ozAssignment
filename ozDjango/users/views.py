from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError
from django.contrib.auth.password_validation import validate_password
from .serializers import MyInfoUserSerializer


# api/v1/users/myinfo [GET,PUT]
class Users(APIView):
    def post(self, request):
        password = request.data.get("password")
        serializer = MyInfoUserSerializer(data=request.data)

        try:
            validate_password(password)
        except:
            raise ParseError("Invaild password")


        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()

            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        
        else:
            raise ParseError(serializer.errors)