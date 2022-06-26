
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from user.serializers import  RegisterSerializer
from user.services import create_user


class RegisterView(GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            user = create_user(serializer.validated_data)
            return Response({"status": 0, "message": "Success"})
        return Response({"status": -1, "message": "Failed"})
