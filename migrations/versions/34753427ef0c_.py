"""empty message

Revision ID: 34753427ef0c
Revises: 8ba65a77e39f
Create Date: 2022-03-16 15:17:31.392411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34753427ef0c'
down_revision = '8ba65a77e39f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('advertisement_model_text_key', 'advertisement_model', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('advertisement_model_text_key', 'advertisement_model', ['text'])
    # ### end Alembic commands ###
