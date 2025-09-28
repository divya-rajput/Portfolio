"""Rename certificates table
Revision ID: aeff25f89db0
Revises: 
Create Date: 2025-09-27 19:59:25.616334
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'aeff25f89db0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.drop_table('certification') 
# def downgrade():
    # op.rename_table('certificates', 'certification')
