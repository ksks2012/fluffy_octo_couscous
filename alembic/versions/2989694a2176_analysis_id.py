"""analysis_id

Revision ID: 2989694a2176
Revises: 1893d330da4c
Create Date: 2024-11-24 22:13:52.399486

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2989694a2176'
down_revision: Union[str, None] = '1893d330da4c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Use batch mode to add the foreign key
    with op.batch_alter_table("comments", schema=None) as batch_op:
        batch_op.add_column(sa.Column('analysis_id', sa.String(length=36), nullable=True))
        batch_op.create_foreign_key(
            "fk_comments_analysis_id", "analysis_result", ["analysis_id"], ["analysis_id"]
        )

def downgrade() -> None:
    # Use batch mode to remove the foreign key
    with op.batch_alter_table("comments", schema=None) as batch_op:
        batch_op.drop_constraint("fk_comments_analysis_id", type_="foreignkey")
        batch_op.drop_column("analysis_id")
