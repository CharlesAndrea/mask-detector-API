"""empty message

Revision ID: 76d4d7155997
Revises: 726c20d87793
Create Date: 2021-08-05 18:46:01.472378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76d4d7155997'
down_revision = '726c20d87793'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('departamento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_dept', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('historial',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ci_e', sa.Integer(), nullable=False),
    sa.Column('modo_uso', sa.String(), nullable=True),
    sa.Column('fecha', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'ci_e'),
    sa.UniqueConstraint('id')
    )
    op.create_table('rol',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_rol', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('empleado',
    sa.Column('ci', sa.Integer(), nullable=False),
    sa.Column('nombre_completo', sa.String(), nullable=False),
    sa.Column('correo', sa.String(), nullable=False),
    sa.Column('contrasena', sa.String(), nullable=False),
    sa.Column('tlf', sa.String(), nullable=True),
    sa.Column('direccion', sa.String(length=120), nullable=True),
    sa.Column('fecha_nacimiento', sa.String(), nullable=True),
    sa.Column('sexo', sa.String(), nullable=True),
    sa.Column('estado', sa.Boolean(), nullable=False),
    sa.Column('dept_id', sa.Integer(), nullable=False),
    sa.Column('rol_id', sa.Integer(), nullable=False),
    sa.Column('ci_s', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ci_s'], ['empleado.ci'], ),
    sa.ForeignKeyConstraint(['dept_id'], ['departamento.id'], ),
    sa.ForeignKeyConstraint(['rol_id'], ['rol.id'], ),
    sa.PrimaryKeyConstraint('ci'),
    sa.UniqueConstraint('ci')
    )
    op.create_table('historial_generado',
    sa.Column('ci_e', sa.Integer(), nullable=False),
    sa.Column('id_hist', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ci_e'], ['empleado.ci'], ),
    sa.ForeignKeyConstraint(['id_hist'], ['historial.id'], ),
    sa.PrimaryKeyConstraint('ci_e', 'id_hist')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('historial_generado')
    op.drop_table('empleado')
    op.drop_table('rol')
    op.drop_table('historial')
    op.drop_table('departamento')
    # ### end Alembic commands ###
