"""Models for conversation and message

Revision ID: ad4b013fb7c0
Revises: 
Create Date: 2025-11-01 16:11:11.420026

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision: str = 'ad4b013fb7c0'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    
    if 'conversation' not in tables:
        op.create_table('conversation',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('created_at', sa.DateTime(), nullable=True),
            sa.PrimaryKeyConstraint('id')
        )
    
    if 'provider' not in tables:
        op.create_table('provider',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('key', sa.String(length=50), nullable=False),
            sa.Column('name', sa.String(length=100), nullable=False),
            sa.Column('model_family', sa.String(length=100), nullable=False),
            sa.Column('is_active', sa.Boolean(), nullable=True),
            sa.PrimaryKeyConstraint('id'),
            sa.UniqueConstraint('key')
        )
    
    if 'model' not in tables:
        op.create_table('model',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('provider_id', sa.Integer(), nullable=False),
            sa.Column('name', sa.String(length=100), nullable=False),
            sa.Column('model_id', sa.String(length=100), nullable=False),
            sa.Column('is_default', sa.Boolean(), nullable=True),
            sa.Column('is_active', sa.Boolean(), nullable=True),
            sa.ForeignKeyConstraint(['provider_id'], ['provider.id'], ),
            sa.PrimaryKeyConstraint('id')
        )
    
    if 'message' not in tables:
        op.create_table('message',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('conversation_id', sa.Integer(), nullable=False),
            sa.Column('type', sa.Enum('PROMPT', 'RESPONSE', name='messagetype'), nullable=False),
            sa.Column('content', sa.Text(), nullable=False),
            sa.Column('model_id', sa.Integer(), nullable=True),
            sa.Column('created_at', sa.DateTime(), nullable=True),
            sa.ForeignKeyConstraint(['conversation_id'], ['conversation.id'], ),
            sa.ForeignKeyConstraint(['model_id'], ['model.id'], ),
            sa.PrimaryKeyConstraint('id')
        )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('message')
    op.drop_table('model')
    op.drop_table('provider')
    op.drop_table('conversation')