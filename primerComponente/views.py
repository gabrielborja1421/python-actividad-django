from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# importación de modelos
from primerComponente.models import PrimerModelo

# importación de serializadores
from primerComponente.serializers import PrimerTablaSerializer

class CustomedResponse():

    def response_custom(self, validate_data, responseCustomed,opcion, status):
        response = {
            "messages":responseCustomed
        }
        if opcion==1:
            response["pay_load"]={"data":validate_data}
        else :
            response["pay_load"]={"description":validate_data}
        response["status"]=status
        return response

class PrimerViewList(APIView):
    
    def get(self, request, format=None):
        querySet = PrimerModelo.objects.all()
        serializer=PrimerTablaSerializer(querySet,many=True ,context={'request':request})
        responseC = CustomedResponse()
        return Response(responseC.response_custom(serializer.data, 'Success',1, status = status.HTTP_200_OK))

    def post(self, request, format=None):
        serializer=PrimerTablaSerializer(data=request.data, context={'request':request})
        responseC = CustomedResponse()
        if serializer.is_valid():
            serializer.save()
            return Response(responseC.response_custom(serializer.data, 'Success',1, status.HTTP_201_CREATED))
        else:
            return Response(responseC.response_custom(serializer.errors, 'Error',2, status.HTTP_400_BAD_REQUEST))


class PrimerViewDetail(APIView):

    def get_object(self, pk):
        try:
            return PrimerModelo.objects.get(pk=pk)
        except PrimerModelo.DoesNotExist:
            return 404
    
    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        responseC = CustomedResponse()
        if idResponse != 404:
            serializer = PrimerTablaSerializer(idResponse, context={'request':request})
            return Response(responseC.response_custom(serializer.data, 'Success',1, status.HTTP_200_OK))
        else:
            return Response(responseC.response_custom('Not Found','Error',2, status=status.HTTP_400_BAD_REQUEST))
    
    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        responseC = CustomedResponse()
        if idResponse != 404:
            serializer = PrimerTablaSerializer(idResponse, data=request.data, context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(responseC.response_custom(serializer.data,'Success' ,1,status = status.HTTP_200_OK))
            else:
                return Response(responseC.response_custom(serializer.errors,'Error' ,2,status = status.HTTP_400_BAD_REQUEST))
        else:
             return Response(responseC.response_custom('Id no encontrado','Error' ,2,status = status.HTTP_400_BAD_REQUEST))
             
    def delete(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        responseC = CustomedResponse()
        if idResponse != 404:
            serializer = PrimerTablaSerializer(idResponse, context={'request':request})
            idResponse.delete()
            return Response(responseC.response_custom(serializer.data, 'Success',1,status = status.HTTP_200_OK))
        else:
            return Response(responseC.response_custom('Id no encontrado','Error',2, status = status.HTTP_400_BAD_REQUEST))

    