"""empty message

Revision ID: 72d1f38c573a
Revises: 
Create Date: 2022-11-30 14:14:43.902336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72d1f38c573a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('provider',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nama', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('password', sa.String(length=250), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('provider_id', sa.Integer(), nullable=True),
    sa.Column('nomer', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['provider_id'], ['provider.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contact')
    op.drop_table('user')
    op.drop_table('provider')
    # ### end Alembic commands ###
