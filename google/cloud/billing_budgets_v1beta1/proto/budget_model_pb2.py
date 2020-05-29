# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/billing_budgets_v1beta1/proto/budget_model.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.type import money_pb2 as google_dot_type_dot_money__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/billing_budgets_v1beta1/proto/budget_model.proto",
    package="google.cloud.billing.budgets.v1beta1",
    syntax="proto3",
    serialized_options=b"\n(com.google.cloud.billing.budgets.v1beta1P\001ZKgoogle.golang.org/genproto/googleapis/cloud/billing/budgets/v1beta1;budgets",
    serialized_pb=b'\n=google/cloud/billing_budgets_v1beta1/proto/budget_model.proto\x12$google.cloud.billing.budgets.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/type/money.proto"\xde\x03\n\x06\x42udget\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x03\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12H\n\rbudget_filter\x18\x03 \x01(\x0b\x32,.google.cloud.billing.budgets.v1beta1.FilterB\x03\xe0\x41\x01\x12G\n\x06\x61mount\x18\x04 \x01(\x0b\x32\x32.google.cloud.billing.budgets.v1beta1.BudgetAmountB\x03\xe0\x41\x02\x12Q\n\x0fthreshold_rules\x18\x05 \x03(\x0b\x32\x33.google.cloud.billing.budgets.v1beta1.ThresholdRuleB\x03\xe0\x41\x01\x12S\n\x10\x61ll_updates_rule\x18\x06 \x01(\x0b\x32\x34.google.cloud.billing.budgets.v1beta1.AllUpdatesRuleB\x03\xe0\x41\x01\x12\x11\n\x04\x65tag\x18\x07 \x01(\tB\x03\xe0\x41\x01:]\xea\x41Z\n$billingbudgets.googleapis.com/Budget\x12\x32\x62illingAccounts/{billing_account}/budgets/{budget}"\xa5\x01\n\x0c\x42udgetAmount\x12.\n\x10specified_amount\x18\x01 \x01(\x0b\x32\x12.google.type.MoneyH\x00\x12T\n\x12last_period_amount\x18\x02 \x01(\x0b\x32\x36.google.cloud.billing.budgets.v1beta1.LastPeriodAmountH\x00\x42\x0f\n\rbudget_amount"\x12\n\x10LastPeriodAmount"\xcd\x01\n\rThresholdRule\x12\x1e\n\x11threshold_percent\x18\x01 \x01(\x01\x42\x03\xe0\x41\x02\x12S\n\x0bspend_basis\x18\x02 \x01(\x0e\x32\x39.google.cloud.billing.budgets.v1beta1.ThresholdRule.BasisB\x03\xe0\x41\x01"G\n\x05\x42\x61sis\x12\x15\n\x11\x42\x41SIS_UNSPECIFIED\x10\x00\x12\x11\n\rCURRENT_SPEND\x10\x01\x12\x14\n\x10\x46ORECASTED_SPEND\x10\x02"H\n\x0e\x41llUpdatesRule\x12\x19\n\x0cpubsub_topic\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x1b\n\x0eschema_version\x18\x02 \x01(\tB\x03\xe0\x41\x02"\x90\x02\n\x06\x46ilter\x12\x15\n\x08projects\x18\x01 \x03(\tB\x03\xe0\x41\x01\x12\x66\n\x16\x63redit_types_treatment\x18\x04 \x01(\x0e\x32\x41.google.cloud.billing.budgets.v1beta1.Filter.CreditTypesTreatmentB\x03\xe0\x41\x01\x12\x15\n\x08services\x18\x03 \x03(\tB\x03\xe0\x41\x01"p\n\x14\x43reditTypesTreatment\x12&\n"CREDIT_TYPES_TREATMENT_UNSPECIFIED\x10\x00\x12\x17\n\x13INCLUDE_ALL_CREDITS\x10\x01\x12\x17\n\x13\x45XCLUDE_ALL_CREDITS\x10\x02\x42y\n(com.google.cloud.billing.budgets.v1beta1P\x01ZKgoogle.golang.org/genproto/googleapis/cloud/billing/budgets/v1beta1;budgetsb\x06proto3',
    dependencies=[
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_type_dot_money__pb2.DESCRIPTOR,
    ],
)


_THRESHOLDRULE_BASIS = _descriptor.EnumDescriptor(
    name="Basis",
    full_name="google.cloud.billing.budgets.v1beta1.ThresholdRule.Basis",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="BASIS_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="CURRENT_SPEND", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="FORECASTED_SPEND",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=992,
    serialized_end=1063,
)
_sym_db.RegisterEnumDescriptor(_THRESHOLDRULE_BASIS)

_FILTER_CREDITTYPESTREATMENT = _descriptor.EnumDescriptor(
    name="CreditTypesTreatment",
    full_name="google.cloud.billing.budgets.v1beta1.Filter.CreditTypesTreatment",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="CREDIT_TYPES_TREATMENT_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="INCLUDE_ALL_CREDITS",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="EXCLUDE_ALL_CREDITS",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1300,
    serialized_end=1412,
)
_sym_db.RegisterEnumDescriptor(_FILTER_CREDITTYPESTREATMENT)


_BUDGET = _descriptor.Descriptor(
    name="Budget",
    full_name="google.cloud.billing.budgets.v1beta1.Budget",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.billing.budgets.v1beta1.Budget.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\003",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="google.cloud.billing.budgets.v1beta1.Budget.display_name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="budget_filter",
            full_name="google.cloud.billing.budgets.v1beta1.Budget.budget_filter",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="amount",
            full_name="google.cloud.billing.budgets.v1beta1.Budget.amount",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="threshold_rules",
            full_name="google.cloud.billing.budgets.v1beta1.Budget.threshold_rules",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="all_updates_rule",
            full_name="google.cloud.billing.budgets.v1beta1.Budget.all_updates_rule",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="etag",
            full_name="google.cloud.billing.budgets.v1beta1.Budget.etag",
            index=6,
            number=7,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\352AZ\n$billingbudgets.googleapis.com/Budget\0222billingAccounts/{billing_account}/budgets/{budget}",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=189,
    serialized_end=667,
)


_BUDGETAMOUNT = _descriptor.Descriptor(
    name="BudgetAmount",
    full_name="google.cloud.billing.budgets.v1beta1.BudgetAmount",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="specified_amount",
            full_name="google.cloud.billing.budgets.v1beta1.BudgetAmount.specified_amount",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="last_period_amount",
            full_name="google.cloud.billing.budgets.v1beta1.BudgetAmount.last_period_amount",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="budget_amount",
            full_name="google.cloud.billing.budgets.v1beta1.BudgetAmount.budget_amount",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=670,
    serialized_end=835,
)


_LASTPERIODAMOUNT = _descriptor.Descriptor(
    name="LastPeriodAmount",
    full_name="google.cloud.billing.budgets.v1beta1.LastPeriodAmount",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=837,
    serialized_end=855,
)


_THRESHOLDRULE = _descriptor.Descriptor(
    name="ThresholdRule",
    full_name="google.cloud.billing.budgets.v1beta1.ThresholdRule",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="threshold_percent",
            full_name="google.cloud.billing.budgets.v1beta1.ThresholdRule.threshold_percent",
            index=0,
            number=1,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="spend_basis",
            full_name="google.cloud.billing.budgets.v1beta1.ThresholdRule.spend_basis",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_THRESHOLDRULE_BASIS],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=858,
    serialized_end=1063,
)


_ALLUPDATESRULE = _descriptor.Descriptor(
    name="AllUpdatesRule",
    full_name="google.cloud.billing.budgets.v1beta1.AllUpdatesRule",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="pubsub_topic",
            full_name="google.cloud.billing.budgets.v1beta1.AllUpdatesRule.pubsub_topic",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="schema_version",
            full_name="google.cloud.billing.budgets.v1beta1.AllUpdatesRule.schema_version",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1065,
    serialized_end=1137,
)


_FILTER = _descriptor.Descriptor(
    name="Filter",
    full_name="google.cloud.billing.budgets.v1beta1.Filter",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="projects",
            full_name="google.cloud.billing.budgets.v1beta1.Filter.projects",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="credit_types_treatment",
            full_name="google.cloud.billing.budgets.v1beta1.Filter.credit_types_treatment",
            index=1,
            number=4,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="services",
            full_name="google.cloud.billing.budgets.v1beta1.Filter.services",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_FILTER_CREDITTYPESTREATMENT],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1140,
    serialized_end=1412,
)

_BUDGET.fields_by_name["budget_filter"].message_type = _FILTER
_BUDGET.fields_by_name["amount"].message_type = _BUDGETAMOUNT
_BUDGET.fields_by_name["threshold_rules"].message_type = _THRESHOLDRULE
_BUDGET.fields_by_name["all_updates_rule"].message_type = _ALLUPDATESRULE
_BUDGETAMOUNT.fields_by_name[
    "specified_amount"
].message_type = google_dot_type_dot_money__pb2._MONEY
_BUDGETAMOUNT.fields_by_name["last_period_amount"].message_type = _LASTPERIODAMOUNT
_BUDGETAMOUNT.oneofs_by_name["budget_amount"].fields.append(
    _BUDGETAMOUNT.fields_by_name["specified_amount"]
)
_BUDGETAMOUNT.fields_by_name[
    "specified_amount"
].containing_oneof = _BUDGETAMOUNT.oneofs_by_name["budget_amount"]
_BUDGETAMOUNT.oneofs_by_name["budget_amount"].fields.append(
    _BUDGETAMOUNT.fields_by_name["last_period_amount"]
)
_BUDGETAMOUNT.fields_by_name[
    "last_period_amount"
].containing_oneof = _BUDGETAMOUNT.oneofs_by_name["budget_amount"]
_THRESHOLDRULE.fields_by_name["spend_basis"].enum_type = _THRESHOLDRULE_BASIS
_THRESHOLDRULE_BASIS.containing_type = _THRESHOLDRULE
_FILTER.fields_by_name[
    "credit_types_treatment"
].enum_type = _FILTER_CREDITTYPESTREATMENT
_FILTER_CREDITTYPESTREATMENT.containing_type = _FILTER
DESCRIPTOR.message_types_by_name["Budget"] = _BUDGET
DESCRIPTOR.message_types_by_name["BudgetAmount"] = _BUDGETAMOUNT
DESCRIPTOR.message_types_by_name["LastPeriodAmount"] = _LASTPERIODAMOUNT
DESCRIPTOR.message_types_by_name["ThresholdRule"] = _THRESHOLDRULE
DESCRIPTOR.message_types_by_name["AllUpdatesRule"] = _ALLUPDATESRULE
DESCRIPTOR.message_types_by_name["Filter"] = _FILTER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Budget = _reflection.GeneratedProtocolMessageType(
    "Budget",
    (_message.Message,),
    {
        "DESCRIPTOR": _BUDGET,
        "__module__": "google.cloud.billing_budgets_v1beta1.proto.budget_model_pb2",
        "__doc__": """A budget is a plan that describes what you expect to spend
  on Cloud projects, plus the rules to execute as spend is tracked against
  that plan, (for example, send an alert when 90% of the target spend is
  met). Currently all plans are monthly budgets so the usage period(s)
  tracked are implied (calendar months of usage back-to-back).
  
  
  Attributes:
      name:
          Output only. Resource name of the budget. The resource name
          implies the scope of a budget. Values are of the form
          ``billingAccounts/{billingAccountId}/budgets/{budgetId}``.
      display_name:
          User data for display name in UI. Validation: <= 60 chars.
      budget_filter:
          Optional. Filters that define which resources are used to
          compute the actual spend against the budget.
      amount:
          Required. Budgeted amount.
      threshold_rules:
          Optional. Rules that trigger alerts (notifications of
          thresholds being crossed) when spend exceeds the specified
          percentages of the budget.
      all_updates_rule:
          Optional. Rules to apply to all updates to the actual spend,
          regardless of the thresholds set in ``threshold_rules``.
      etag:
          Optional. Etag to validate that the object is unchanged for a
          read-modify-write operation. An empty etag will cause an
          update to overwrite other changes.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.billing.budgets.v1beta1.Budget)
    },
)
_sym_db.RegisterMessage(Budget)

BudgetAmount = _reflection.GeneratedProtocolMessageType(
    "BudgetAmount",
    (_message.Message,),
    {
        "DESCRIPTOR": _BUDGETAMOUNT,
        "__module__": "google.cloud.billing_budgets_v1beta1.proto.budget_model_pb2",
        "__doc__": """The budgeted amount for each usage period.
  
  
  Attributes:
      budget_amount:
          Specification for what amount to use as the budget.
      specified_amount:
          A specified amount to use as the budget. ``currency_code`` is
          optional. If specified, it must match the currency of the
          billing account. The ``currency_code`` is provided on output.
      last_period_amount:
          Use the last period’s actual spend as the budget for the
          present period.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.billing.budgets.v1beta1.BudgetAmount)
    },
)
_sym_db.RegisterMessage(BudgetAmount)

LastPeriodAmount = _reflection.GeneratedProtocolMessageType(
    "LastPeriodAmount",
    (_message.Message,),
    {
        "DESCRIPTOR": _LASTPERIODAMOUNT,
        "__module__": "google.cloud.billing_budgets_v1beta1.proto.budget_model_pb2",
        "__doc__": """Describes a budget amount targeted to last period’s spend.
  At this time, the amount is automatically 100% of last period’s spend;
  that is, there are no other options yet. Future configuration will be
  described here (for example, configuring a percentage of last period’s
  spend).
  
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.billing.budgets.v1beta1.LastPeriodAmount)
    },
)
_sym_db.RegisterMessage(LastPeriodAmount)

ThresholdRule = _reflection.GeneratedProtocolMessageType(
    "ThresholdRule",
    (_message.Message,),
    {
        "DESCRIPTOR": _THRESHOLDRULE,
        "__module__": "google.cloud.billing_budgets_v1beta1.proto.budget_model_pb2",
        "__doc__": """ThresholdRule contains a definition of a threshold which triggers an
  alert (a notification of a threshold being crossed) to be sent when
  spend goes above the specified amount. Alerts are automatically e-mailed
  to users with the Billing Account Administrator role or the Billing
  Account User role. The thresholds here have no effect on notifications
  sent to anything configured under ``Budget.all_updates_rule``.
  
  
  Attributes:
      threshold_percent:
          Required. Send an alert when this threshold is exceeded. This
          is a 1.0-based percentage, so 0.5 = 50%. Validation: non-
          negative number.
      spend_basis:
          Optional. The type of basis used to determine if spend has
          passed the threshold. Behavior defaults to CURRENT_SPEND if
          not set.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.billing.budgets.v1beta1.ThresholdRule)
    },
)
_sym_db.RegisterMessage(ThresholdRule)

AllUpdatesRule = _reflection.GeneratedProtocolMessageType(
    "AllUpdatesRule",
    (_message.Message,),
    {
        "DESCRIPTOR": _ALLUPDATESRULE,
        "__module__": "google.cloud.billing_budgets_v1beta1.proto.budget_model_pb2",
        "__doc__": """AllUpdatesRule defines notifications that are sent on
  every update to the billing account’s spend, regardless of the
  thresholds defined using threshold rules.
  
  
  Attributes:
      pubsub_topic:
          Required. The name of the Cloud Pub/Sub topic where budget
          related messages will be published, in the form
          ``projects/{project_id}/topics/{topic_id}``. Updates are sent
          at regular intervals to the topic. The topic needs to be
          created before the budget is created; see
          https://cloud.google.com/billing/docs/how-to/budgets#manage-
          notifications for more details. Caller is expected to have
          ``pubsub.topics.setIamPolicy`` permission on the topic when
          it’s set for a budget, otherwise, the API call will fail with
          PERMISSION_DENIED. See
          https://cloud.google.com/pubsub/docs/access-control for more
          details on Pub/Sub roles and permissions.
      schema_version:
          Required. The schema version of the notification. Only “1.0”
          is accepted. It represents the JSON schema as defined in
          https://cloud.google.com/billing/docs/how-
          to/budgets#notification_format
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.billing.budgets.v1beta1.AllUpdatesRule)
    },
)
_sym_db.RegisterMessage(AllUpdatesRule)

Filter = _reflection.GeneratedProtocolMessageType(
    "Filter",
    (_message.Message,),
    {
        "DESCRIPTOR": _FILTER,
        "__module__": "google.cloud.billing_budgets_v1beta1.proto.budget_model_pb2",
        "__doc__": """A filter for a budget, limiting the scope of the cost to
  calculate.
  
  
  Attributes:
      projects:
          Optional. A set of projects of the form
          ``projects/{project}``, specifying that usage from only this
          set of projects should be included in the budget. If omitted,
          the report will include all usage for the billing account,
          regardless of which project the usage occurred on. Only zero
          or one project can be specified currently.
      credit_types_treatment:
          Optional. If not set, default behavior is
          ``INCLUDE_ALL_CREDITS``.
      services:
          Optional. A set of services of the form
          ``services/{service_id}``, specifying that usage from only
          this set of services should be included in the budget. If
          omitted, the report will include usage for all the services.
          The service names are available through the Catalog API:
          https://cloud.google.com/billing/v1/how-tos/catalog-api.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.billing.budgets.v1beta1.Filter)
    },
)
_sym_db.RegisterMessage(Filter)


DESCRIPTOR._options = None
_BUDGET.fields_by_name["name"]._options = None
_BUDGET.fields_by_name["budget_filter"]._options = None
_BUDGET.fields_by_name["amount"]._options = None
_BUDGET.fields_by_name["threshold_rules"]._options = None
_BUDGET.fields_by_name["all_updates_rule"]._options = None
_BUDGET.fields_by_name["etag"]._options = None
_BUDGET._options = None
_THRESHOLDRULE.fields_by_name["threshold_percent"]._options = None
_THRESHOLDRULE.fields_by_name["spend_basis"]._options = None
_ALLUPDATESRULE.fields_by_name["pubsub_topic"]._options = None
_ALLUPDATESRULE.fields_by_name["schema_version"]._options = None
_FILTER.fields_by_name["projects"]._options = None
_FILTER.fields_by_name["credit_types_treatment"]._options = None
_FILTER.fields_by_name["services"]._options = None
# @@protoc_insertion_point(module_scope)
