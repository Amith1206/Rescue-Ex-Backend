"""initial migration

Revision ID: 68b40ae4d0fc
Revises: 
Create Date: 2020-09-13 01:34:48.944899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68b40ae4d0fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rescuee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=64), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('long', sa.Float(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('rescuee')
    # ### end Alembic commands ###