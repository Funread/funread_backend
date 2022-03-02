from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from whatthefuck.models import WhatTheFuck as Snippet
from whatthefuck.serializers import WhatTheFuckSerializer as SnippetSerializer

"""
    The following code is almost identical to the one in 
        https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
    Why? Because I'm lazy... In addition, if you walk through the tutorial of django-rest-framework,
    you can trim your code even more. Here is the final code:
  
    ```
        from snippets.models import Snippet
        from snippets.serializers import SnippetSerializer
        from rest_framework import generics

        class SnippetList(generics.ListCreateAPIView):
            queryset = Snippet.objects.all()
            serializer_class = SnippetSerializer


        class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
            queryset = Snippet.objects.all()
            serializer_class = SnippetSerializer
    ```

    You could see the example in 
        https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-generic-class-based-views

    Yes. The code above can achieve the same task as the code below -- but remember to change 
    your code in urls.py.

"""

@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)