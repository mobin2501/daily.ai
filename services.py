from models import db, Conversation, Message, MessageType
import logging

class ConversationService:
    @staticmethod
    def save_conversation(prompt, response, model_id=None):
        conversation = Conversation()
        db.session.add(conversation)
        db.session.flush()
        
        prompt_msg = Message(
            conversation_id=conversation.id,
            type=MessageType.PROMPT,
            content=prompt
        )
        db.session.add(prompt_msg)
        
        response_msg = Message(
            conversation_id=conversation.id,
            type=MessageType.RESPONSE,
            content=response,
            model_id=model_id
        )
        db.session.add(response_msg)
        
        db.session.commit()
        return conversation.id