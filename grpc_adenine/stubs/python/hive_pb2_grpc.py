# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import hive_pb2 as hive__pb2


class HiveStub(object):
    """The service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadAndSign = channel.unary_unary(
                '/hive.Hive/UploadAndSign',
                request_serializer=hive__pb2.Request.SerializeToString,
                response_deserializer=hive__pb2.Response.FromString,
                )
        self.VerifyAndShow = channel.unary_unary(
                '/hive.Hive/VerifyAndShow',
                request_serializer=hive__pb2.Request.SerializeToString,
                response_deserializer=hive__pb2.Response.FromString,
                )


class HiveServicer(object):
    """The service definition.
    """

    def UploadAndSign(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerifyAndShow(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HiveServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadAndSign': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadAndSign,
                    request_deserializer=hive__pb2.Request.FromString,
                    response_serializer=hive__pb2.Response.SerializeToString,
            ),
            'VerifyAndShow': grpc.unary_unary_rpc_method_handler(
                    servicer.VerifyAndShow,
                    request_deserializer=hive__pb2.Request.FromString,
                    response_serializer=hive__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hive.Hive', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Hive(object):
    """The service definition.
    """

    @staticmethod
    def UploadAndSign(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hive.Hive/UploadAndSign',
            hive__pb2.Request.SerializeToString,
            hive__pb2.Response.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VerifyAndShow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hive.Hive/VerifyAndShow',
            hive__pb2.Request.SerializeToString,
            hive__pb2.Response.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
