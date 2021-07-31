"""create manga table

Revision ID: 20cf40bcc490
Revises: 
Create Date: 2021-07-31 21:06:20.636481

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '20cf40bcc490'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stuff')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stuff',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('author', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('artist', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('year', sa.NUMERIC(precision=4, scale=0), autoincrement=False, nullable=True),
    sa.Column('status', postgresql.ENUM('ongoing', 'completed', 'hiatus', 'cancelled', name='status'), autoincrement=False, nullable=False),
    sa.Column('version', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='stuff_pkey')
    )
    # ### end Alembic commands ###
