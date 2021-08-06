"""empty message

Revision ID: 7cabb38a511d
Revises: cf9872fe2cf9
Create Date: 2021-08-06 12:36:01.162508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cabb38a511d'
down_revision = 'cf9872fe2cf9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('historial_generado')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('historial_generado',
    sa.Column('ci_e', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('id_hist', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['ci_e'], ['empleado.ci'], name='historial_generado_ci_e_fkey'),
    sa.ForeignKeyConstraint(['id_hist'], ['historial.id'], name='historial_generado_id_hist_fkey'),
    sa.PrimaryKeyConstraint('ci_e', 'id_hist', name='historial_generado_pkey')
    )
    # ### end Alembic commands ###
