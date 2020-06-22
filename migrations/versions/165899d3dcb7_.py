"""empty message

Revision ID: 165899d3dcb7
Revises: 
Create Date: 2020-06-22 17:59:35.381908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '165899d3dcb7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sensor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=30), nullable=False),
    sa.Column('type', sa.String(length=20), nullable=False),
    sa.Column('inside', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sensor_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('type', sa.String(length=20), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('sensor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sensor_id'], ['sensor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sensor_data')
    op.drop_table('sensor')
    # ### end Alembic commands ###
