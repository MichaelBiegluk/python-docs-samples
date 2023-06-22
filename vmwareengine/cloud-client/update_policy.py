# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.api_core import operation
from google.cloud import vmwareengine_v1


def update_network_policy(project_id: str, region: str) -> operation.Operation:
    """
    Creates a new network policy in a given network.

    Args:
        project_id: name of the project you want to use.
        region: name of the region you want to use. I.e. "us-central1"

    Returns:
        An operation object representing the started operation. You can call its .result() method to wait for
        it to finish.
    """

    client = vmwareengine_v1.VmwareEngineClient()
    request = vmwareengine_v1.UpdateNetworkPolicyRequest()
    request.update_mask = "internetAccess.enabled,externalIp.enabled"
    network_policy = vmwareengine_v1.NetworkPolicy()
    network_policy.name = f"projects/{project_id}/locations/{region}/networkPolicies/{region}-default"
    network_policy.vmware_engine_network = f"projects/{project_id}/locations/{region}/vmwareEngineNetworks/{region}-default"
    network_policy.internet_access.enabled = False
    network_policy.external_ip.enabled = False

    request.network_policy = network_policy

    return client.update_network_policy(request)
