"""empty message

Revision ID: e27809f3b95d
Revises: 52ee964ec5f0
Create Date: 2024-08-12 11:44:53.285618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e27809f3b95d'
down_revision = '52ee964ec5f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('lastname', sa.String(length=80), nullable=False))
        batch_op.drop_constraint('user_username_key', type_='unique')
        batch_op.create_unique_constraint(None, ['lastname'])
        batch_op.drop_column('username')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_unique_constraint('user_username_key', ['username'])
        batch_op.drop_column('lastname')

    # ### end Alembic commands ###