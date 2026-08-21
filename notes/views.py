from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Note
from .serializers import RegisterSerializer, NoteSerializer


# REGISTER API
class RegisterView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "message": "User registered successfully"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# GET NOTES + CREATE NOTE
class NotesView(APIView):

    permission_classes = [IsAuthenticated]

    # GET ALL NOTES
    def get(self, request):

        notes = Note.objects.filter(user=request.user)

        serializer = NoteSerializer(
            notes,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


    # CREATE NOTE
    def post(self, request):
        print(request.data)
        serializer = NoteSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(user=request.user)

            return Response(
                {
                    "message": "Note created successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# UPDATE NOTE
class UpdateNoteView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, id):

        try:
            note = Note.objects.get(
                id=id,
                user=request.user
            )

        except Note.DoesNotExist:

            return Response(
                {
                    "error": "Note not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = NoteSerializer(
            note,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "message": "Note updated successfully",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# DELETE NOTE
class DeleteNoteView(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, id):

        try:

            note = Note.objects.get(
                id=id,
                user=request.user
            )

        except Note.DoesNotExist:

            return Response(
                {
                    "error": "Note not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        note.delete()

        return Response(
            {
                "message": "Note deleted successfully"
            },
            status=status.HTTP_200_OK
        )