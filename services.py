from models import db, Conversation, Message, MessageType, ModelFamily
import logging

class ConversationService:
    @staticmethod
    def save_conversation(prompt, response, model_family=ModelFamily.GEMINI):
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
            model_family=model_family
        )
        db.session.add(response_msg)
        
        
        db.session.commit()
        return conversation.id