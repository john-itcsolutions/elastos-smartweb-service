# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import sidechain_eth_pb2 as sidechain__eth__pb2


class SidechainEthStub(object):
    """The service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DeployEthContract = channel.unary_unary(
                '/sidechain_eth.SidechainEth/DeployEthContract',
                request_serializer=sidechain__eth__pb2.Request.SerializeToString,
                response_deserializer=sidechain__eth__pb2.Response.FromString,
                )
        self.WatchEthContract = channel.unary_unary(
                '/sidechain_eth.SidechainEth/WatchEthContract',
                request_serializer=sidechain__eth__pb2.Request.SerializeToString,
                response_deserializer=sidechain__eth__pb2.Response.FromString,
                )


class SidechainEthServicer(object):
    """The service definition.
    """

    def DeployEthContract(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchEthContract(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SidechainEthServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DeployEthContract': grpc.unary_unary_rpc_method_handler(
                    servicer.DeployEthContract,
                    request_deserializer=sidechain__eth__pb2.Request.FromString,
                    response_serializer=sidechain__eth__pb2.Response.SerializeToString,
            ),
            'WatchEthContract': grpc.unary_unary_rpc_method_handler(
                    servicer.WatchEthContract,
                    request_deserializer=sidechain__eth__pb2.Request.FromString,
                    response_serializer=sidechain__eth__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sidechain_eth.SidechainEth', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SidechainEth(object):
    """The service definition.
    """

    @staticmethod
    def DeployEthContract(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sidechain_eth.SidechainEth/DeployEthContract',
            sidechain__eth__pb2.Request.SerializeToString,
            sidechain__eth__pb2.Response.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WatchEthContract(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sidechain_eth.SidechainEth/WatchEthContract',
            sidechain__eth__pb2.Request.SerializeToString,
            sidechain__eth__pb2.Response.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
