from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from translator.models import Translation
from translator.serializers import TranslationSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

class FrenchSpanishTranslationViewSet(APIView):

    def get(self, request):
        data = Translation.objects.filter(source_language__in=['FR', 'ES'], target_language__in=['FR', 'ES'])
        serializer = TranslationSerializer(data, many=True)
        return Response(data=serializer.data, status=None)
    
    def post(self, request):
        serializer = TranslationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=None)
        return Response(data=serializer.errors, status=None)
    
    def put(self, request, pk):
        translation = get_object_or_404(Translation, pk=pk)
        serializer = TranslationSerializer(translation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=None)
        return Response(data=serializer.errors, status=None)
    
    def delete(self, request, pk):
        translation = get_object_or_404(Translation, pk=pk)
        translation.delete()
        return Response(data={}, status=None)
    
class FrenchEnglishTranslationViewSet(APIView):

    def get(self, request):

        import google.generativeai as genai

        api_key="AIzaSyCmYrzD3f23p7p_QUvWk06G67-5i4O27UY"

        genai.configure(api_key=[api_key])
        
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)
    
class FrenchItalianTranslationViewSet(APIView):

    def get(self, request):
        data = Translation.objects.filter(source_language__in=['FR', 'IT'], target_language__in=['FR', 'IT'])
        serializer = TranslationSerializer(data, many=True)
        return Response(data=serializer.data, status=None)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)

class AllTranslation(APIView):
    
        def get(self, request):

            data = Translation.objects.all()
            serializer = TranslationSerializer(data, many=True)
            return Response(data=serializer.data, status=None)
        
def index(request):
    return render(request, 'index.html', context={})

def contact(request):
    return render(request, 'contact.html', context={})