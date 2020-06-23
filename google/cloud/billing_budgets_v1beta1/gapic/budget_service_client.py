# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Accesses the google.cloud.billing.budgets.v1beta1 BudgetService API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.page_iterator
import google.api_core.path_template
import grpc

from google.cloud.billing_budgets_v1beta1.gapic import budget_service_client_config
from google.cloud.billing_budgets_v1beta1.gapic import enums
from google.cloud.billing_budgets_v1beta1.gapic.transports import (
    budget_service_grpc_transport,
)
from google.cloud.billing_budgets_v1beta1.proto import budget_model_pb2
from google.cloud.billing_budgets_v1beta1.proto import budget_service_pb2
from google.cloud.billing_budgets_v1beta1.proto import budget_service_pb2_grpc
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    "google-cloud-billing-budgets"
).version


class BudgetServiceClient(object):
    """
    BudgetService stores Cloud Billing budgets, which define a
    budget plan and rules to execute as we track spend against that plan.
    """

    SERVICE_ADDRESS = "billingbudgets.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.cloud.billing.budgets.v1beta1.BudgetService"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            BudgetServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def billing_account_path(cls, billing_account):
        """Return a fully-qualified billing_account string."""
        return google.api_core.path_template.expand(
            "billingAccounts/{billing_account}", billing_account=billing_account
        )

    @classmethod
    def budget_path(cls, billing_account, budget):
        """Return a fully-qualified budget string."""
        return google.api_core.path_template.expand(
            "billingAccounts/{billing_account}/budgets/{budget}",
            billing_account=billing_account,
            budget=budget,
        )

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.BudgetServiceGrpcTransport,
                    Callable[[~.Credentials, type], ~.BudgetServiceGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = budget_service_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=budget_service_grpc_transport.BudgetServiceGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = budget_service_grpc_transport.BudgetServiceGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME]
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def create_budget(
        self,
        parent,
        budget,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates a new budget. See
        <a href="https://cloud.google.com/billing/quotas">Quotas and limits</a>
        for more information on the limits of the number of budgets you can create.

        Example:
            >>> from google.cloud import billing_budgets_v1beta1
            >>>
            >>> client = billing_budgets_v1beta1.BudgetServiceClient()
            >>>
            >>> parent = client.billing_account_path('[BILLING_ACCOUNT]')
            >>>
            >>> # TODO: Initialize `budget`:
            >>> budget = {}
            >>>
            >>> response = client.create_budget(parent, budget)

        Args:
            parent (str): Required. The name of the billing account to create the budget in.
                Values are of the form ``billingAccounts/{billingAccountId}``.
            budget (Union[dict, ~google.cloud.billing_budgets_v1beta1.types.Budget]): Required. Budget to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.billing_budgets_v1beta1.types.Budget`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.billing_budgets_v1beta1.types.Budget` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_budget" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_budget"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_budget,
                default_retry=self._method_configs["CreateBudget"].retry,
                default_timeout=self._method_configs["CreateBudget"].timeout,
                client_info=self._client_info,
            )

        request = budget_service_pb2.CreateBudgetRequest(parent=parent, budget=budget)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_budget"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_budget(
        self,
        budget,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates a budget and returns the updated budget.

        WARNING: There are some fields exposed on the Google Cloud Console that
        aren't available on this API. Budget fields that are not exposed in
        this API will not be changed by this method.

        Example:
            >>> from google.cloud import billing_budgets_v1beta1
            >>>
            >>> client = billing_budgets_v1beta1.BudgetServiceClient()
            >>>
            >>> # TODO: Initialize `budget`:
            >>> budget = {}
            >>>
            >>> response = client.update_budget(budget)

        Args:
            budget (Union[dict, ~google.cloud.billing_budgets_v1beta1.types.Budget]): Required. The updated budget object.
                The budget to update is specified by the budget name in the budget.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.billing_budgets_v1beta1.types.Budget`
            update_mask (Union[dict, ~google.cloud.billing_budgets_v1beta1.types.FieldMask]): Optional. Indicates which fields in the provided budget to update.
                Read-only fields (such as ``name``) cannot be changed. If this is not
                provided, then only fields with non-default values from the request are
                updated. See
                https://developers.google.com/protocol-buffers/docs/proto3#default for
                more details about default values.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.billing_budgets_v1beta1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.billing_budgets_v1beta1.types.Budget` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_budget" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_budget"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_budget,
                default_retry=self._method_configs["UpdateBudget"].retry,
                default_timeout=self._method_configs["UpdateBudget"].timeout,
                client_info=self._client_info,
            )

        request = budget_service_pb2.UpdateBudgetRequest(
            budget=budget, update_mask=update_mask
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("budget.name", budget.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_budget"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_budget(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Returns a budget.

        WARNING: There are some fields exposed on the Google Cloud Console that
        aren't available on this API. When reading from the API, you will not
        see these fields in the return value, though they may have been set
        in the Cloud Console.

        Example:
            >>> from google.cloud import billing_budgets_v1beta1
            >>>
            >>> client = billing_budgets_v1beta1.BudgetServiceClient()
            >>>
            >>> name = client.budget_path('[BILLING_ACCOUNT]', '[BUDGET]')
            >>>
            >>> response = client.get_budget(name)

        Args:
            name (str): Required. Name of budget to get. Values are of the form
                ``billingAccounts/{billingAccountId}/budgets/{budgetId}``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.billing_budgets_v1beta1.types.Budget` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_budget" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_budget"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_budget,
                default_retry=self._method_configs["GetBudget"].retry,
                default_timeout=self._method_configs["GetBudget"].timeout,
                client_info=self._client_info,
            )

        request = budget_service_pb2.GetBudgetRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_budget"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_budgets(
        self,
        parent,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Returns a list of budgets for a billing account.

        WARNING: There are some fields exposed on the Google Cloud Console that
        aren't available on this API. When reading from the API, you will not
        see these fields in the return value, though they may have been set
        in the Cloud Console.

        Example:
            >>> from google.cloud import billing_budgets_v1beta1
            >>>
            >>> client = billing_budgets_v1beta1.BudgetServiceClient()
            >>>
            >>> parent = client.billing_account_path('[BILLING_ACCOUNT]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_budgets(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_budgets(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. Name of billing account to list budgets under. Values are
                of the form ``billingAccounts/{billingAccountId}``.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.billing_budgets_v1beta1.types.Budget` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_budgets" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_budgets"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_budgets,
                default_retry=self._method_configs["ListBudgets"].retry,
                default_timeout=self._method_configs["ListBudgets"].timeout,
                client_info=self._client_info,
            )

        request = budget_service_pb2.ListBudgetsRequest(
            parent=parent, page_size=page_size
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_budgets"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="budgets",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def delete_budget(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes a budget. Returns successfully if already deleted.

        Example:
            >>> from google.cloud import billing_budgets_v1beta1
            >>>
            >>> client = billing_budgets_v1beta1.BudgetServiceClient()
            >>>
            >>> name = client.budget_path('[BILLING_ACCOUNT]', '[BUDGET]')
            >>>
            >>> client.delete_budget(name)

        Args:
            name (str): Required. Name of the budget to delete. Values are of the form
                ``billingAccounts/{billingAccountId}/budgets/{budgetId}``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_budget" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_budget"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_budget,
                default_retry=self._method_configs["DeleteBudget"].retry,
                default_timeout=self._method_configs["DeleteBudget"].timeout,
                client_info=self._client_info,
            )

        request = budget_service_pb2.DeleteBudgetRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_budget"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
