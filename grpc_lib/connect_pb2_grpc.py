# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import grpc_lib.connect_pb2 as connect__pb2


class SystemStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.cpu = channel.unary_unary(
        '/System/cpu',
        request_serializer=connect__pb2.Request.SerializeToString,
        response_deserializer=connect__pb2.ReplyInt.FromString,
        )
    self.mem_per = channel.unary_unary(
        '/System/mem_per',
        request_serializer=connect__pb2.Request.SerializeToString,
        response_deserializer=connect__pb2.ReplyInt.FromString,
        )
    self.mem = channel.unary_unary(
        '/System/mem',
        request_serializer=connect__pb2.Request.SerializeToString,
        response_deserializer=connect__pb2.ReplyFloat.FromString,
        )
    self.swap = channel.unary_unary(
        '/System/swap',
        request_serializer=connect__pb2.Request.SerializeToString,
        response_deserializer=connect__pb2.ReplyFloat.FromString,
        )
    self.net = channel.unary_unary(
        '/System/net',
        request_serializer=connect__pb2.Request.SerializeToString,
        response_deserializer=connect__pb2.ReplyFloat.FromString,
        )
    self.uptime = channel.unary_unary(
        '/System/uptime',
        request_serializer=connect__pb2.Request.SerializeToString,
        response_deserializer=connect__pb2.ReplyInt.FromString,
        )


class SystemServicer(object):
  """The greeting service definition.
  """

  def cpu(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def mem_per(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def mem(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def swap(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def net(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def uptime(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SystemServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'cpu': grpc.unary_unary_rpc_method_handler(
          servicer.cpu,
          request_deserializer=connect__pb2.Request.FromString,
          response_serializer=connect__pb2.ReplyInt.SerializeToString,
      ),
      'mem_per': grpc.unary_unary_rpc_method_handler(
          servicer.mem_per,
          request_deserializer=connect__pb2.Request.FromString,
          response_serializer=connect__pb2.ReplyInt.SerializeToString,
      ),
      'mem': grpc.unary_unary_rpc_method_handler(
          servicer.mem,
          request_deserializer=connect__pb2.Request.FromString,
          response_serializer=connect__pb2.ReplyFloat.SerializeToString,
      ),
      'swap': grpc.unary_unary_rpc_method_handler(
          servicer.swap,
          request_deserializer=connect__pb2.Request.FromString,
          response_serializer=connect__pb2.ReplyFloat.SerializeToString,
      ),
      'net': grpc.unary_unary_rpc_method_handler(
          servicer.net,
          request_deserializer=connect__pb2.Request.FromString,
          response_serializer=connect__pb2.ReplyFloat.SerializeToString,
      ),
      'uptime': grpc.unary_unary_rpc_method_handler(
          servicer.uptime,
          request_deserializer=connect__pb2.Request.FromString,
          response_serializer=connect__pb2.ReplyInt.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'System', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class NVIDIAStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.mem = channel.unary_unary(
        '/NVIDIA/mem',
        request_serializer=connect__pb2.Request.SerializeToString,
        response_deserializer=connect__pb2.ReplyFloat.FromString,
        )


class NVIDIAServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def mem(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NVIDIAServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'mem': grpc.unary_unary_rpc_method_handler(
          servicer.mem,
          request_deserializer=connect__pb2.Request.FromString,
          response_serializer=connect__pb2.ReplyFloat.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'NVIDIA', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))