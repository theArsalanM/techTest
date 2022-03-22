from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from molecule.models import Molecule, Activity
from molecule.serializers import MoleculeSerializer, ActivitySerializer


class MoleculeViewSet(ReadOnlyModelViewSet):
    """
    Provides detail view of a single molecule
    Lists all molecules using Standard Pagination Class
    """
    queryset = Molecule.objects.all()
    serializer_class = MoleculeSerializer

    @action(detail=True)
    def activity(self, request, pk=None):
        """"
        Returns a list of activities for the provided Molecule ID, using Standard Pagination Class
        """
        queryset = Activity.objects.filter(molecule_id=pk)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ActivitySerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
