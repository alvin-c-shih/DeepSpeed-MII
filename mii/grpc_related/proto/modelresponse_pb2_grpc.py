# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mii.grpc_related.proto.modelresponse_pb2 as modelresponse__pb2


class ModelResponseStub(object):
    """The greeting service definition.
    """
    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GeneratorReply = channel.unary_unary(
            '/modelresponse.ModelResponse/GeneratorReply',
            request_serializer=modelresponse__pb2.SingleStringRequest.SerializeToString,
            response_deserializer=modelresponse__pb2.SingleStringReply.FromString,
        )
        self.ClassificationReply = channel.unary_unary(
            '/modelresponse.ModelResponse/ClassificationReply',
            request_serializer=modelresponse__pb2.SingleStringRequest.SerializeToString,
            response_deserializer=modelresponse__pb2.SingleStringReply.FromString,
        )
        self.QuestionAndAnswerReply = channel.unary_unary(
            '/modelresponse.ModelResponse/QuestionAndAnswerReply',
            request_serializer=modelresponse__pb2.QARequest.SerializeToString,
            response_deserializer=modelresponse__pb2.SingleStringReply.FromString,
        )


class ModelResponseServicer(object):
    """The greeting service definition.
    """
    def GeneratorReply(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClassificationReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuestionAndAnswerReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModelResponseServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GeneratorReply':
        grpc.unary_unary_rpc_method_handler(
            servicer.GeneratorReply,
            request_deserializer=modelresponse__pb2.SingleStringRequest.FromString,
            response_serializer=modelresponse__pb2.SingleStringReply.SerializeToString,
        ),
        'ClassificationReply':
        grpc.unary_unary_rpc_method_handler(
            servicer.ClassificationReply,
            request_deserializer=modelresponse__pb2.SingleStringRequest.FromString,
            response_serializer=modelresponse__pb2.SingleStringReply.SerializeToString,
        ),
        'QuestionAndAnswerReply':
        grpc.unary_unary_rpc_method_handler(
            servicer.QuestionAndAnswerReply,
            request_deserializer=modelresponse__pb2.QARequest.FromString,
            response_serializer=modelresponse__pb2.SingleStringReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler('modelresponse.ModelResponse',
                                                           rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler, ))


# This class is part of an EXPERIMENTAL API.
class ModelResponse(object):
    """The greeting service definition.
    """
    @staticmethod
    def GeneratorReply(request,
                       target,
                       options=(),
                       channel_credentials=None,
                       call_credentials=None,
                       insecure=False,
                       compression=None,
                       wait_for_ready=None,
                       timeout=None,
                       metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/modelresponse.ModelResponse/GeneratorReply',
            modelresponse__pb2.SingleStringRequest.SerializeToString,
            modelresponse__pb2.SingleStringReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata)

    @staticmethod
    def ClassificationReply(request,
                            target,
                            options=(),
                            channel_credentials=None,
                            call_credentials=None,
                            insecure=False,
                            compression=None,
                            wait_for_ready=None,
                            timeout=None,
                            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/modelresponse.ModelResponse/ClassificationReply',
            modelresponse__pb2.SingleStringRequest.SerializeToString,
            modelresponse__pb2.SingleStringReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata)

    @staticmethod
    def QuestionAndAnswerReply(request,
                               target,
                               options=(),
                               channel_credentials=None,
                               call_credentials=None,
                               insecure=False,
                               compression=None,
                               wait_for_ready=None,
                               timeout=None,
                               metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/modelresponse.ModelResponse/QuestionAndAnswerReply',
            modelresponse__pb2.QARequest.SerializeToString,
            modelresponse__pb2.SingleStringReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata)
