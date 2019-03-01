# Copyright (c) 2019 China Telecom Corporation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""add-amphora-num-to-loadbalancer

Revision ID: 102baabb847e
Revises: d081d6a6ddc1
Create Date: 2019-02-28 14:29:34.753208

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '102baabb847e'
down_revision = 'd081d6a6ddc1'


def upgrade():
    op.add_column(
        u'load_balancer',
        sa.Column(u'expected_amphora_number', sa.Integer(), nullable=True))
