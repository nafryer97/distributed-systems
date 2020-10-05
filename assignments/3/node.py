from concurrent import futures
import logging

import grpc 

import rsa_pb2
import rsa_pb2_grpc

'''class SecureMessaging(rsa_pb2_grpc.SecureMessagingServicer):

    def GetPublicKey():
        return rsa_pb2.PublicKey()
'''

class Greeter(rsa_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return rsa_pb2.HelloReply(message='Hello, %s!' % request.name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rsa_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(name)s %(message)s', level=logging.DEBUG)
    serve()
