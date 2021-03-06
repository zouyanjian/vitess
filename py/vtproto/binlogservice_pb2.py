# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: binlogservice.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import binlogdata_pb2 as binlogdata__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='binlogservice.proto',
  package='binlogservice',
  syntax='proto3',
  serialized_pb=_b('\n\x13\x62inlogservice.proto\x12\rbinlogservice\x1a\x10\x62inlogdata.proto2\x99\x02\n\x0cUpdateStream\x12U\n\x0cStreamUpdate\x12\x1f.binlogdata.StreamUpdateRequest\x1a .binlogdata.StreamUpdateResponse\"\x00\x30\x01\x12[\n\x0eStreamKeyRange\x12!.binlogdata.StreamKeyRangeRequest\x1a\".binlogdata.StreamKeyRangeResponse\"\x00\x30\x01\x12U\n\x0cStreamTables\x12\x1f.binlogdata.StreamTablesRequest\x1a .binlogdata.StreamTablesResponse\"\x00\x30\x01\x62\x06proto3')
  ,
  dependencies=[binlogdata__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





import abc
from grpc.beta import implementations as beta_implementations
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

class BetaUpdateStreamServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def StreamUpdate(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def StreamKeyRange(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def StreamTables(self, request, context):
    raise NotImplementedError()

class BetaUpdateStreamStub(object):
  """The interface to which stubs will conform."""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def StreamUpdate(self, request, timeout):
    raise NotImplementedError()
  @abc.abstractmethod
  def StreamKeyRange(self, request, timeout):
    raise NotImplementedError()
  @abc.abstractmethod
  def StreamTables(self, request, timeout):
    raise NotImplementedError()

def beta_create_UpdateStream_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import binlogdata_pb2
  import binlogdata_pb2
  import binlogdata_pb2
  import binlogdata_pb2
  import binlogdata_pb2
  import binlogdata_pb2
  request_deserializers = {
    ('binlogservice.UpdateStream', 'StreamKeyRange'): binlogdata_pb2.StreamKeyRangeRequest.FromString,
    ('binlogservice.UpdateStream', 'StreamTables'): binlogdata_pb2.StreamTablesRequest.FromString,
    ('binlogservice.UpdateStream', 'StreamUpdate'): binlogdata_pb2.StreamUpdateRequest.FromString,
  }
  response_serializers = {
    ('binlogservice.UpdateStream', 'StreamKeyRange'): binlogdata_pb2.StreamKeyRangeResponse.SerializeToString,
    ('binlogservice.UpdateStream', 'StreamTables'): binlogdata_pb2.StreamTablesResponse.SerializeToString,
    ('binlogservice.UpdateStream', 'StreamUpdate'): binlogdata_pb2.StreamUpdateResponse.SerializeToString,
  }
  method_implementations = {
    ('binlogservice.UpdateStream', 'StreamKeyRange'): face_utilities.unary_stream_inline(servicer.StreamKeyRange),
    ('binlogservice.UpdateStream', 'StreamTables'): face_utilities.unary_stream_inline(servicer.StreamTables),
    ('binlogservice.UpdateStream', 'StreamUpdate'): face_utilities.unary_stream_inline(servicer.StreamUpdate),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_UpdateStream_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import binlogdata_pb2
  import binlogdata_pb2
  import binlogdata_pb2
  import binlogdata_pb2
  import binlogdata_pb2
  import binlogdata_pb2
  request_serializers = {
    ('binlogservice.UpdateStream', 'StreamKeyRange'): binlogdata_pb2.StreamKeyRangeRequest.SerializeToString,
    ('binlogservice.UpdateStream', 'StreamTables'): binlogdata_pb2.StreamTablesRequest.SerializeToString,
    ('binlogservice.UpdateStream', 'StreamUpdate'): binlogdata_pb2.StreamUpdateRequest.SerializeToString,
  }
  response_deserializers = {
    ('binlogservice.UpdateStream', 'StreamKeyRange'): binlogdata_pb2.StreamKeyRangeResponse.FromString,
    ('binlogservice.UpdateStream', 'StreamTables'): binlogdata_pb2.StreamTablesResponse.FromString,
    ('binlogservice.UpdateStream', 'StreamUpdate'): binlogdata_pb2.StreamUpdateResponse.FromString,
  }
  cardinalities = {
    'StreamKeyRange': cardinality.Cardinality.UNARY_STREAM,
    'StreamTables': cardinality.Cardinality.UNARY_STREAM,
    'StreamUpdate': cardinality.Cardinality.UNARY_STREAM,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'binlogservice.UpdateStream', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
