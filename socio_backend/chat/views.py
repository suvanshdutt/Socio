from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import db  # Assuming you have imported and connected MongoDB here

class ChatList(APIView):

    def get(self, request):
        # Fetch all chats from MongoDB
        chats = list(db.chats.find())
        
        # Convert MongoDB documents to a list of dictionaries
        for chat in chats:
            chat['_id'] = str(chat['_id'])  # Convert ObjectId to string
        
        return Response({"chats": chats}, status=status.HTTP_200_OK)

    def post(self, request):
        # Get the data from the request
        participants = request.data.get('participants')
        messages = request.data.get('messages')

        # Check if the chat already exists
        chat = db.chats.find_one({"participants": participants})
        if chat:
            # Update the chat with the new message
            db.chats.update_one(
                {"_id": chat["_id"]},
                {"$push": {"messages": {"$each": messages}}}
            )
        else:
            # Create a new chat document
            db.chats.insert_one({
                "participants": participants,
                "messages": messages,
            })

        return Response({"message": "Message saved"}, status=status.HTTP_201_CREATED)
