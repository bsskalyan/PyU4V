# Copyright (c) 2022 Dell Inc. or its subsidiaries.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""clone.py."""

import logging

from PyU4V.common import CommonFunctions
from PyU4V.provisioning import ProvisioningFunctions
from PyU4V.utils import constants
from PyU4V.utils import exception

LOG = logging.getLogger(__name__)

# Resource constants
ASYNC_UPDATE = constants.ASYNC_UPDATE
REPLICATION = constants.REPLICATION
SYMMETRIX = constants.SYMMETRIX
CAPABILITIES = constants.CAPABILITIES
STORAGEGROUP = constants.STORAGEGROUP
RDFG = constants.RDFG
RDF_GROUP = constants.RDF_GROUP
METRO_DR = constants.METRO_DR
ASYNCHRONOUS = constants.ASYNCHRONOUS_CC
ADAPTIVE_COPY = constants.ADAPTIVE_COPY


class CloneFunctions(object):
    """Clone Functions."""

    def __init__(self, array_id, rest_client):
        """__init__."""
        self.provisioning = ProvisioningFunctions(array_id, rest_client)
        self.common = CommonFunctions(rest_client)
        self.get_resource = self.common.get_resource
        self.create_resource = self.common.create_resource
        self.modify_resource = self.common.modify_resource
        self.delete_resource = self.common.delete_resource
        self.array_id = array_id

    def clone_target_storage_group_list(
            self, array_id, storage_group_id, target_storage_group=None,
            target_storage_group_volume_count=None, volume_pair_count=None,
            state=None, modified_tracks=None, src_protected_tracks=None,
            src_modified_tracks=None, background_copy=None,
            differential=None, precopy=None, vse=None):
        """Clone target storage group list.
        param: array_id The storage array ID -- string
        param: storage_group_id The Storage Group ID -- string
        param: target_storage_group Value that filters returned list to include
               target storage groups equal to or like the provided
               name -- string
        param: target_storage_group_volume_count Value that filters returned
               list to include target storage groups with the specified
               number of volumes -- string
        param: volume_pair_count Value that filters returned list to include
               target storage groups with the specified number of volume
               pairs -- string
        param: state Value that filters returned list to include target storage
               groups with pairs in the specified states -- array
        param: modified_tracks Value that filters returned list to include
               target storage groups with the specified modified
               tracks -- string
        param: src_protected_tracks Value that filters returned list to include
               target storage groups with the specified src protected tracks
               -- string
        param: src_modified_tracks Value that filters returned list to
               include target storage groups with the specified src modified
               tracks -- string
        param: background_copy Value that filters returned list to include
               target storage groups with background copy flag -- boolean
        param: differential Value that filters returned list to include target
               storage groups with differential flag -- boolean
        param: precopy Value that filters returned list to include target
               storage groups with the precopy flag -- boolean
        param: vse Value that filters returned list to include target storage
               groups with the vse -- boolean
        """
        query_params = {
            'target_storage_group': target_storage_group,
            'target_storage_group_volume_count':
                target_storage_group_volume_count,
            'volume_pair_count': volume_pair_count, 'state': state,
            'modified_tracks': modified_tracks,
            'src_protected_tracks': src_protected_tracks,
            'src_modified_tracks': src_modified_tracks,
            'background_copy': background_copy, 'differential': differential,
            'precopy': precopy,
            'vse': vse, }
        return api.common.get_request(
            target_uri=f"/100/replication/symmetrix/{array_id}/storagegroup/"
                       f"{storage_group_id}/clone/storagegroup",
            resource_type=None, params=query_params)

    def clone_Pairs_List(self, array_id, storage_group_id):
        """Clone Pairs List.
        param: array_id The storage array ID -- string
        param: storage_group_id The Storage Group ID -- string
        """
        query_params = {}
        return api.common.get_request(
            target_uri=f"/100/replication/symmetrix"
                        f"/{array_id}/storagegroup/{storage_group_id}"
                        f"/clone/volume",
            resource_type=None, params=query_params)

    def clone_storage_group_pair_details(
            self, array_id, storage_group_id, target_storage_group_id):
        """Clone storage group pair details.
        param: array_id The storage array ID -- string
        param: storage_group_id The Storage Group ID -- string
        param: target_storage_group_id The Target Storage Group ID -- string
        """
        query_params = {}
        return api.common.get_request(
            target_uri=f"/100/replication/symmetrix/{array_id}/storagegroup/"
                       f"{storage_group_id}/clone/storagegroup/"
                       f"{target_storage_group_id}",
            resource_type=None, params=query_params)
