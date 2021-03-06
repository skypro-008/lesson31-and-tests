from rest_framework import viewsets
from choco.models import Chocolate
from choco.serializers import ChocoSerializer
from rest_framework.response import Response


class ChocoViewSet(viewsets.ModelViewSet):
    queryset = Chocolate.objects.all()
    serializer_class = ChocoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"items": serializer.data[:5]})
