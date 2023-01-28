"""Initial migration

Revision ID: 3d98af01da1d
Revises: 
Create Date: 2023-01-26 19:47:40.719258

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import sqlalchemy_utils

from models.models import EventSeatStatus, SeatType

# revision identifiers, used by Alembic.
revision = '3d98af01da1d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('place',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('location', sa.String(length=30), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.Column('host_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('open', sa.Time(), nullable=False),
    sa.Column('close', sa.Time(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_place_name'), 'place', ['name'], unique=True)
    op.create_table('purchased_film',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('film_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('place_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('start', sa.DateTime(), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('host_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('film_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('participants', sa.Integer(), nullable=False),
    sa.Column('comments', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['place_id'], ['place.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_event_name'), 'event', ['name'], unique=True)
    op.create_table('seat',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('row', sa.Integer(), nullable=True),
    sa.Column('seat', sa.Integer(), nullable=True),
    sa.Column('type', sqlalchemy_utils.types.choice.ChoiceType(choices=SeatType, impl=sa.Integer()), nullable=False),
    sa.Column('place_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['place_id'], ['place.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_seat',
    sa.Column('seat_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('event_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('status', sqlalchemy_utils.types.choice.ChoiceType(choices=EventSeatStatus, impl=sa.Integer()), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['seat_id'], ['seat.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('seat_id', 'event_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event_seat')
    op.drop_table('seat')
    op.drop_index(op.f('ix_event_name'), table_name='event')
    op.drop_table('event')
    op.drop_table('purchased_film')
    op.drop_index(op.f('ix_place_name'), table_name='place')
    op.drop_table('place')
    # ### end Alembic commands ###
