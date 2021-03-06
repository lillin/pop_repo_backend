from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import RepoPopularitySearchSerializer, RepoPopularityByOwnerSerializer


class RepoPopularitySearchView(APIView):
    def post(self, request):
        context = {'page': request.query_params.get('page')}
        serializer = RepoPopularitySearchSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)


class RepoPopularityByOwnerView(APIView):
    def post(self, request):
        serializer = RepoPopularityByOwnerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)
