# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration import StorageManagementClientConfiguration
from .operations import Operations
from .operations import SkusOperations
from .operations import StorageAccountsOperations
from .operations import UsageOperations
from .operations import BlobContainersOperations
from . import models


class StorageManagementClient(object):
    """The Azure Storage Management API.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.storage.v2018_02_01.operations.Operations
    :ivar skus: SkusOperations operations
    :vartype skus: azure.mgmt.storage.v2018_02_01.operations.SkusOperations
    :ivar storage_accounts: StorageAccountsOperations operations
    :vartype storage_accounts: azure.mgmt.storage.v2018_02_01.operations.StorageAccountsOperations
    :ivar usage: UsageOperations operations
    :vartype usage: azure.mgmt.storage.v2018_02_01.operations.UsageOperations
    :ivar blob_containers: BlobContainersOperations operations
    :vartype blob_containers: azure.mgmt.storage.v2018_02_01.operations.BlobContainersOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = StorageManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.skus = SkusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.storage_accounts = StorageAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usage = UsageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.blob_containers = BlobContainersOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> StorageManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
