from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status, permissions

class DetailsMixin(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @property
    def model(self):
        raise NotImplementedError('Specify a model to use DetailsMixin')

    @property
    def serializer(self):
        raise NotImplementedError('Specify a serializer to use DetailsMixin')

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        instance = self.get_object(pk)
        return Response(self.serializer(instance).data)
    
    def put(self, request, pk):
        instance = self.get_object(pk)
        updated_instance = self.serializer(instance, data=request.data)
        if updated_instance.is_valid():
            updated_instance.save()
            return Response(updated_instance.data)
        return Response(updated_instance.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
