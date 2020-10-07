from concurrent import futures
import socket
import logging

import grpc 

import rsa_pb2
import rsa_pb2_grpc

class SecureMessaging(rsa_pb2_grpc.SecureMessagingServicer):
    def GetPublicKey(self, request, context):
        return rsa_pb2.PublicKey(n=3233,e=17)
    def SendEncryptedMessage(self, request, context):
        m = decrypt(request.message)
        print("Server received encrypted message: " + str(m))
        return rsa_pb2.MsgAck(status=1,src=request.src,dst=request.dst)
class Greeter(rsa_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return rsa_pb2.HelloReply(message='Hello, %s!' % request.name)

def encrypt(m, e, n):
    return (m**e)%n 

def decrypt(c,n=3233,d=413):
    return (c**d)%n

def run():
    e=0
    n=0
    with grpc.insecure_channel('server:50051') as channel:
        stub = rsa_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(rsa_pb2.HelloRequest(name='you'))
        print("Client received: " + response.message)
        
        stub2 = rsa_pb2_grpc.SecureMessagingStub(channel)
        response2 = stub2.GetPublicKey(rsa_pb2.NullMsg(status=1))
        e = response2.e
        n = response2.n
        print("Client received public key: " + str(response2.n) + " " + str(response2.e))

        m = encrypt(4812, e, n)

        stub3 = rsa_pb2_grpc.SecureMessagingStub(channel)
        response3 = stub3.SendEncryptedMessage(rsa_pb2.EncryptedMessage(message=m,src='1',dst='2'))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rsa_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    rsa_pb2_grpc.add_SecureMessagingServicer_to_server(SecureMessaging(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(name)s %(message)s', level=logging.DEBUG)
    if socket.gethostname() == 'server':
        serve()
    elif socket.gethostname() == 'client1':
        run()
    elif socket.gethostname() == 'client2':
        run()
    else:
        print("Unexpected hostname")
