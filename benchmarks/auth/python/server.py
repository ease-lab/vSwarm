# MIT License

# Copyright (c) 2022 EASE lab

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from concurrent import futures
import logging
from pprint import pprint

import grpc

import random
import string

import argparse
import os
import sys


# sys.path.append('./proto/auth')  # for local testing (i.e. not running in Docker-compose)
from proto.auth import auth_pb2
import auth_pb2_grpc

# adding python tracing sources to the system path
sys.path.insert(0, os.getcwd() + '/../../../../utils/tracing/python')
import tracing





print("python version: %s" % sys.version)
print("Server has PID: %d" % os.getpid())


parser = argparse.ArgumentParser()
parser.add_argument("-a", "--addr", dest="addr", default="0.0.0.0", help="IP address")
parser.add_argument("-p", "--port", dest="port", default="50051", help="serve port")
parser.add_argument("-zipkin", "--zipkin", dest="url", default="http://0.0.0.0:9411/api/v2/spans", help="Zipkin endpoint url")
args = parser.parse_args()


if tracing.IsTracingEnabled():


    tracing.initTracer("auth-python", url=args.url)
    tracing.grpcInstrumentClient()
    tracing.grpcInstrumentServer()

class Empty:  # declare this class to enable dynamically adding new attributes
    pass

def generatePolicy(principalId, effect, resource):
    authResponse = Empty()

    authResponse.principalId = principalId
    if effect and resource:
        policyDocument = Empty()
        policyDocument.Version = '2012-10-17'
        policyDocument.Statement = [None]
        statementOne = Empty()
        statementOne.Action = 'execute-api:Invoke'
        statementOne.Effect = effect
        statementOne.Resource = resource
        policyDocument.Statement[0] = statementOne
        authResponse.policyDocument = policyDocument

    # Optional output with custom properties of the String, Number or Boolean type.
    authResponse.context = {
      "stringKey": "stringval",
      "numberKey": 123,
      "booleanKey": True
    }

    return authResponse




class Greeter(auth_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):

        token = request.name
        fakeMethodArn = "arn:aws:execute-api:{regionId}:{accountId}:{apiId}/{stage}/{httpVerb}/[{resource}/[{child-resources}]]"

        with tracing.Span("Generate Policy"):
            if 'allow' in token:
                ret = generatePolicy('user', 'Allow', fakeMethodArn)
                resp = ret.__dict__
                msg = "fn: Auth | token: {token} | resp: {resp} | runtime: python".format(token=token, resp=str(resp))
            elif 'deny' in token:
                ret = generatePolicy('user', 'Deny', fakeMethodArn)
                resp = ret.__dict__
                msg = "fn: Auth | token: {token} | resp: {resp} | runtime: python".format(token=token, resp=str(resp))
            elif 'unauthorized':
                msg = "Unauthorized"   # Return a 401 Unauthorized response
            else:
                msg = "Error: Invalid token" # Return a 500 Invalid token response

        return auth_pb2.HelloReply(message=msg)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    auth_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

    address = (args.addr + ":" + args.port)
    server.add_insecure_port(address)
    print("Start Auth-python server. Addr: " + address)

    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
