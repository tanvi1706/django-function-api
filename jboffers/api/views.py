from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view

from jboffers.models import JobOffers
from jboffers.api.serializer import JobOffersSerializer


# Function-based views
@api_view(["GET", "POST"])
def JobBoardListView(request):

    if request.method == "GET":
        job = JobOffers.objects.filter(available=True)
        serializer = JobOffersSerializer(job, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = JobOffersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def JobBoardDetailView(request, pk):

    try:
        job = JobOffers.objects.get(pk=pk)
    except job.DoesNotExist:
        return Response(
            {
                "error": {
                    "code": 404,
                    "message": "This job Does not exist"
                }
            }, status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "GET":
        serializer = JobOffersSerializer(job)
        return Response(serializer.data)
   
    elif request.method == "PUT":
        serializer = JobOffersSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


