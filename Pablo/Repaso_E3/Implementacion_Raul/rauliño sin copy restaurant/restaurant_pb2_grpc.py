# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import restaurant_pb2 as restaurant__pb2


class RestaurantStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.request = channel.unary_unary(
                '/restaurant.Restaurant/request',
                request_serializer=restaurant__pb2.ReservationRequest.SerializeToString,
                response_deserializer=restaurant__pb2.ServerResponse.FromString,
                )
        self.check = channel.unary_unary(
                '/restaurant.Restaurant/check',
                request_serializer=restaurant__pb2.ReservationID.SerializeToString,
                response_deserializer=restaurant__pb2.ServerResponse.FromString,
                )
        self.cancel = channel.unary_unary(
                '/restaurant.Restaurant/cancel',
                request_serializer=restaurant__pb2.ReservationID.SerializeToString,
                response_deserializer=restaurant__pb2.ServerResponse.FromString,
                )
        self.list = channel.unary_unary(
                '/restaurant.Restaurant/list',
                request_serializer=restaurant__pb2.ListReq.SerializeToString,
                response_deserializer=restaurant__pb2.ServerResponse.FromString,
                )


class RestaurantServicer(object):
    """Missing associated documentation comment in .proto file."""

    def request(self, request, context):
        """Dentro del servicio restaurante, incluyo las operaciones que debe realizar
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def check(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def cancel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RestaurantServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'request': grpc.unary_unary_rpc_method_handler(
                    servicer.request,
                    request_deserializer=restaurant__pb2.ReservationRequest.FromString,
                    response_serializer=restaurant__pb2.ServerResponse.SerializeToString,
            ),
            'check': grpc.unary_unary_rpc_method_handler(
                    servicer.check,
                    request_deserializer=restaurant__pb2.ReservationID.FromString,
                    response_serializer=restaurant__pb2.ServerResponse.SerializeToString,
            ),
            'cancel': grpc.unary_unary_rpc_method_handler(
                    servicer.cancel,
                    request_deserializer=restaurant__pb2.ReservationID.FromString,
                    response_serializer=restaurant__pb2.ServerResponse.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=restaurant__pb2.ListReq.FromString,
                    response_serializer=restaurant__pb2.ServerResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'restaurant.Restaurant', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Restaurant(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def request(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/restaurant.Restaurant/request',
            restaurant__pb2.ReservationRequest.SerializeToString,
            restaurant__pb2.ServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def check(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/restaurant.Restaurant/check',
            restaurant__pb2.ReservationID.SerializeToString,
            restaurant__pb2.ServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def cancel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/restaurant.Restaurant/cancel',
            restaurant__pb2.ReservationID.SerializeToString,
            restaurant__pb2.ServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/restaurant.Restaurant/list',
            restaurant__pb2.ListReq.SerializeToString,
            restaurant__pb2.ServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
