"""base init

Revision ID: 354222c0ab70
Revises: 4fa974bedec1
Create Date: 2025-03-24 14:37:29.986414

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '354222c0ab70'
down_revision: Union[str, None] = '4fa974bedec1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_companies_id'), 'companies', ['id'], unique=False)
    op.create_table('resumes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('position', sa.String(length=200), nullable=True),
    sa.Column('skills', sa.Text(), nullable=True),
    sa.Column('experience', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_resumes_id'), 'resumes', ['id'], unique=False)
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_favorites_id'), 'favorites', ['id'], unique=False)
    op.create_table('responses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_responses_id'), 'responses', ['id'], unique=False)
    op.add_column('jobs', sa.Column('user_id', sa.Integer(), nullable=False))
    op.add_column('jobs', sa.Column('type', sa.String(length=20), nullable=False))
    op.add_column('jobs', sa.Column('price', sa.Numeric(), nullable=True))
    op.add_column('jobs', sa.Column('status', sa.String(length=20), nullable=False))
    op.alter_column('jobs', 'title',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=200),
               existing_nullable=False)
    op.alter_column('jobs', 'description',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.Text(),
               existing_nullable=True)
    op.create_foreign_key(None, 'jobs', 'users', ['user_id'], ['id'])
    op.drop_column('jobs', 'owner_id')
    op.add_column('users', sa.Column('name', sa.String(length=100), nullable=True))
    op.add_column('users', sa.Column('role', sa.String(length=20), nullable=False))
    op.add_column('users', sa.Column('intent', sa.String(length=20), nullable=False))
    op.add_column('users', sa.Column('telegram_id', sa.String(length=50), nullable=True))
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.drop_constraint('users_username_key', 'users', type_='unique')
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.drop_column('users', 'hashed_password')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('hashed_password', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.create_unique_constraint('users_username_key', 'users', ['username'])
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    op.drop_column('users', 'telegram_id')
    op.drop_column('users', 'intent')
    op.drop_column('users', 'role')
    op.drop_column('users', 'name')
    op.add_column('jobs', sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'jobs', type_='foreignkey')
    op.alter_column('jobs', 'description',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=500),
               existing_nullable=True)
    op.alter_column('jobs', 'title',
               existing_type=sa.String(length=200),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
    op.drop_column('jobs', 'status')
    op.drop_column('jobs', 'price')
    op.drop_column('jobs', 'type')
    op.drop_column('jobs', 'user_id')
    op.drop_index(op.f('ix_responses_id'), table_name='responses')
    op.drop_table('responses')
    op.drop_index(op.f('ix_favorites_id'), table_name='favorites')
    op.drop_table('favorites')
    op.drop_index(op.f('ix_resumes_id'), table_name='resumes')
    op.drop_table('resumes')
    op.drop_index(op.f('ix_companies_id'), table_name='companies')
    op.drop_table('companies')
    # ### end Alembic commands ###
