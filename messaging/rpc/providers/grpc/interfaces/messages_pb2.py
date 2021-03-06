# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='messaging.rpc.providers.grpc.proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0emessages.proto\x12\"messaging.rpc.providers.grpc.proto\"\x19\n\nNodeHeader\x12\x0b\n\x03uri\x18\x01 \x01(\t\"\x94\x01\n\x08Schedule\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0ctrigger_type\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\x05\x12J\n\x10schedule_details\x18\x05 \x01(\x0b\x32\x30.messaging.rpc.providers.grpc.proto.CronSchedule\"\x99\x01\n\x0c\x43ronSchedule\x12\x0e\n\x06second\x18\x01 \x01(\t\x12\x0e\n\x06minute\x18\x02 \x01(\t\x12\x0c\n\x04hour\x18\x03 \x01(\t\x12\x0b\n\x03\x64\x61y\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x61y_of_week\x18\x05 \x01(\t\x12\x0c\n\x04week\x18\x06 \x01(\t\x12\r\n\x05month\x18\x07 \x01(\t\x12\x0c\n\x04year\x18\x08 \x01(\t\x12\x0e\n\x06jitter\x18\t \x01(\x05\"R\n\tClockNode\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\x0e\n\x06minute\x18\x03 \x01(\x05\x12\x1a\n\x12max_schedule_count\x18\x04 \x01(\x05\"\x13\n\x11HealthPingRequest\"\x14\n\x12HealthPingResponse\"T\n\x12\x41\x64\x64ScheduleRequest\x12>\n\x08schedule\x18\x02 \x01(\x0b\x32,.messaging.rpc.providers.grpc.proto.Schedule\"\x15\n\x13\x41\x64\x64ScheduleResponse\"%\n\x15RemoveScheduleRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"\x18\n\x16RemoveScheduleResponse\"Z\n\x17ReplaceSchedulesRequest\x12?\n\tschedules\x18\x01 \x03(\x0b\x32,.messaging.rpc.providers.grpc.proto.Schedule\"\x1a\n\x18ReplaceSchedulesResponse\"{\n\x18RegisterClockNodeRequest\x12;\n\x04node\x18\x01 \x01(\x0b\x32-.messaging.rpc.providers.grpc.proto.ClockNode\x12\"\n\x1areschedule_on_registration\x18\x02 \x01(\x08\"\x1b\n\x19RegisterClockNodeResponseb\x06proto3'
)




_NODEHEADER = _descriptor.Descriptor(
  name='NodeHeader',
  full_name='messaging.rpc.providers.grpc.proto.NodeHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='messaging.rpc.providers.grpc.proto.NodeHeader.uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=79,
)


_SCHEDULE = _descriptor.Descriptor(
  name='Schedule',
  full_name='messaging.rpc.providers.grpc.proto.Schedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='messaging.rpc.providers.grpc.proto.Schedule.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='messaging.rpc.providers.grpc.proto.Schedule.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trigger_type', full_name='messaging.rpc.providers.grpc.proto.Schedule.trigger_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='messaging.rpc.providers.grpc.proto.Schedule.type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schedule_details', full_name='messaging.rpc.providers.grpc.proto.Schedule.schedule_details', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=230,
)


_CRONSCHEDULE = _descriptor.Descriptor(
  name='CronSchedule',
  full_name='messaging.rpc.providers.grpc.proto.CronSchedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='second', full_name='messaging.rpc.providers.grpc.proto.CronSchedule.second', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minute', full_name='messaging.rpc.providers.grpc.proto.CronSchedule.minute', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hour', full_name='messaging.rpc.providers.grpc.proto.CronSchedule.hour', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day', full_name='messaging.rpc.providers.grpc.proto.CronSchedule.day', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day_of_week', full_name='messaging.rpc.providers.grpc.proto.CronSchedule.day_of_week', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='week', full_name='messaging.rpc.providers.grpc.proto.CronSchedule.week', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='messaging.rpc.providers.grpc.proto.CronSchedule.month', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='year', full_name='messaging.rpc.providers.grpc.proto.CronSchedule.year', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jitter', full_name='messaging.rpc.providers.grpc.proto.CronSchedule.jitter', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=386,
)


_CLOCKNODE = _descriptor.Descriptor(
  name='ClockNode',
  full_name='messaging.rpc.providers.grpc.proto.ClockNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='messaging.rpc.providers.grpc.proto.ClockNode.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uri', full_name='messaging.rpc.providers.grpc.proto.ClockNode.uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minute', full_name='messaging.rpc.providers.grpc.proto.ClockNode.minute', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_schedule_count', full_name='messaging.rpc.providers.grpc.proto.ClockNode.max_schedule_count', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=388,
  serialized_end=470,
)


_HEALTHPINGREQUEST = _descriptor.Descriptor(
  name='HealthPingRequest',
  full_name='messaging.rpc.providers.grpc.proto.HealthPingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=472,
  serialized_end=491,
)


_HEALTHPINGRESPONSE = _descriptor.Descriptor(
  name='HealthPingResponse',
  full_name='messaging.rpc.providers.grpc.proto.HealthPingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=493,
  serialized_end=513,
)


_ADDSCHEDULEREQUEST = _descriptor.Descriptor(
  name='AddScheduleRequest',
  full_name='messaging.rpc.providers.grpc.proto.AddScheduleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schedule', full_name='messaging.rpc.providers.grpc.proto.AddScheduleRequest.schedule', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=515,
  serialized_end=599,
)


_ADDSCHEDULERESPONSE = _descriptor.Descriptor(
  name='AddScheduleResponse',
  full_name='messaging.rpc.providers.grpc.proto.AddScheduleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=601,
  serialized_end=622,
)


_REMOVESCHEDULEREQUEST = _descriptor.Descriptor(
  name='RemoveScheduleRequest',
  full_name='messaging.rpc.providers.grpc.proto.RemoveScheduleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='messaging.rpc.providers.grpc.proto.RemoveScheduleRequest.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=624,
  serialized_end=661,
)


_REMOVESCHEDULERESPONSE = _descriptor.Descriptor(
  name='RemoveScheduleResponse',
  full_name='messaging.rpc.providers.grpc.proto.RemoveScheduleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=663,
  serialized_end=687,
)


_REPLACESCHEDULESREQUEST = _descriptor.Descriptor(
  name='ReplaceSchedulesRequest',
  full_name='messaging.rpc.providers.grpc.proto.ReplaceSchedulesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schedules', full_name='messaging.rpc.providers.grpc.proto.ReplaceSchedulesRequest.schedules', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=689,
  serialized_end=779,
)


_REPLACESCHEDULESRESPONSE = _descriptor.Descriptor(
  name='ReplaceSchedulesResponse',
  full_name='messaging.rpc.providers.grpc.proto.ReplaceSchedulesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=781,
  serialized_end=807,
)


_REGISTERCLOCKNODEREQUEST = _descriptor.Descriptor(
  name='RegisterClockNodeRequest',
  full_name='messaging.rpc.providers.grpc.proto.RegisterClockNodeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='messaging.rpc.providers.grpc.proto.RegisterClockNodeRequest.node', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reschedule_on_registration', full_name='messaging.rpc.providers.grpc.proto.RegisterClockNodeRequest.reschedule_on_registration', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=809,
  serialized_end=932,
)


_REGISTERCLOCKNODERESPONSE = _descriptor.Descriptor(
  name='RegisterClockNodeResponse',
  full_name='messaging.rpc.providers.grpc.proto.RegisterClockNodeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=934,
  serialized_end=961,
)

_SCHEDULE.fields_by_name['schedule_details'].message_type = _CRONSCHEDULE
_ADDSCHEDULEREQUEST.fields_by_name['schedule'].message_type = _SCHEDULE
_REPLACESCHEDULESREQUEST.fields_by_name['schedules'].message_type = _SCHEDULE
_REGISTERCLOCKNODEREQUEST.fields_by_name['node'].message_type = _CLOCKNODE
DESCRIPTOR.message_types_by_name['NodeHeader'] = _NODEHEADER
DESCRIPTOR.message_types_by_name['Schedule'] = _SCHEDULE
DESCRIPTOR.message_types_by_name['CronSchedule'] = _CRONSCHEDULE
DESCRIPTOR.message_types_by_name['ClockNode'] = _CLOCKNODE
DESCRIPTOR.message_types_by_name['HealthPingRequest'] = _HEALTHPINGREQUEST
DESCRIPTOR.message_types_by_name['HealthPingResponse'] = _HEALTHPINGRESPONSE
DESCRIPTOR.message_types_by_name['AddScheduleRequest'] = _ADDSCHEDULEREQUEST
DESCRIPTOR.message_types_by_name['AddScheduleResponse'] = _ADDSCHEDULERESPONSE
DESCRIPTOR.message_types_by_name['RemoveScheduleRequest'] = _REMOVESCHEDULEREQUEST
DESCRIPTOR.message_types_by_name['RemoveScheduleResponse'] = _REMOVESCHEDULERESPONSE
DESCRIPTOR.message_types_by_name['ReplaceSchedulesRequest'] = _REPLACESCHEDULESREQUEST
DESCRIPTOR.message_types_by_name['ReplaceSchedulesResponse'] = _REPLACESCHEDULESRESPONSE
DESCRIPTOR.message_types_by_name['RegisterClockNodeRequest'] = _REGISTERCLOCKNODEREQUEST
DESCRIPTOR.message_types_by_name['RegisterClockNodeResponse'] = _REGISTERCLOCKNODERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeHeader = _reflection.GeneratedProtocolMessageType('NodeHeader', (_message.Message,), {
  'DESCRIPTOR' : _NODEHEADER,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:messaging.rpc.providers.grpc.proto.NodeHeader)
  })
_sym_db.RegisterMessage(NodeHeader)

Schedule = _reflection.GeneratedProtocolMessageType('Schedule', (_message.Message,), {
  'DESCRIPTOR' : _SCHEDULE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:messaging.rpc.providers.grpc.proto.Schedule)
  })
_sym_db.RegisterMessage(Schedule)

CronSchedule = _reflection.GeneratedProtocolMessageType('CronSchedule', (_message.Message,), {
  'DESCRIPTOR' : _CRONSCHEDULE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:messaging.rpc.providers.grpc.proto.CronSchedule)
  })
_sym_db.RegisterMessage(CronSchedule)

ClockNode = _reflection.GeneratedProtocolMessageType('ClockNode', (_message.Message,), {
  'DESCRIPTOR' : _CLOCKNODE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:messaging.rpc.providers.grpc.proto.ClockNode)
  })
_sym_db.RegisterMessage(ClockNode)

HealthPingRequest = _reflection.GeneratedProtocolMessageType('HealthPingRequest', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHPINGREQUEST,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:messaging.rpc.providers.grpc.proto.HealthPingRequest)
  })
_sym_db.RegisterMessage(HealthPingRequest)

HealthPingResponse = _reflection.GeneratedProtocolMessageType('HealthPingResponse', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHPINGRESPONSE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:messaging.rpc.providers.grpc.proto.HealthPingResponse)
  })
_sym_db.RegisterMessage(HealthPingResponse)

AddScheduleRequest = _reflection.GeneratedProtocolMessageType('AddScheduleRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDSCHEDULEREQUEST,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:messaging.rpc.providers.grpc.proto.AddScheduleRequest)
  })
_sym_db.RegisterMessage(AddScheduleRequest)

AddScheduleResponse = _reflection.GeneratedProtocolMessageType('AddScheduleResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDSCHEDULERESPONSE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:messaging.rpc.providers.grpc.proto.AddScheduleResponse)
  })
_sym_db.RegisterMessage(AddScheduleResponse)

RemoveScheduleRequest = _reflection.GeneratedProtocolMessageType('RemoveScheduleRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVESCHEDULEREQUEST,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:messaging.rpc.providers.grpc.proto.RemoveScheduleRequest)
  })
_sym_db.RegisterMessage(RemoveScheduleRequest)

RemoveScheduleResponse = _reflection.GeneratedProtocolMessageType('RemoveScheduleResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVESCHEDULERESPONSE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:messaging.rpc.providers.grpc.proto.RemoveScheduleResponse)
  })
_sym_db.RegisterMessage(RemoveScheduleResponse)

ReplaceSchedulesRequest = _reflection.GeneratedProtocolMessageType('ReplaceSchedulesRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPLACESCHEDULESREQUEST,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:messaging.rpc.providers.grpc.proto.ReplaceSchedulesRequest)
  })
_sym_db.RegisterMessage(ReplaceSchedulesRequest)

ReplaceSchedulesResponse = _reflection.GeneratedProtocolMessageType('ReplaceSchedulesResponse', (_message.Message,), {
  'DESCRIPTOR' : _REPLACESCHEDULESRESPONSE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:messaging.rpc.providers.grpc.proto.ReplaceSchedulesResponse)
  })
_sym_db.RegisterMessage(ReplaceSchedulesResponse)

RegisterClockNodeRequest = _reflection.GeneratedProtocolMessageType('RegisterClockNodeRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERCLOCKNODEREQUEST,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:messaging.rpc.providers.grpc.proto.RegisterClockNodeRequest)
  })
_sym_db.RegisterMessage(RegisterClockNodeRequest)

RegisterClockNodeResponse = _reflection.GeneratedProtocolMessageType('RegisterClockNodeResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERCLOCKNODERESPONSE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:messaging.rpc.providers.grpc.proto.RegisterClockNodeResponse)
  })
_sym_db.RegisterMessage(RegisterClockNodeResponse)


# @@protoc_insertion_point(module_scope)
