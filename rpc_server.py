import random
from xmlrpc.server import SimpleXMLRPCServer

import tenseal as ts

# Setup TenSEAL context
context = ts.context(
    ts.SCHEME_TYPE.BFV,
    poly_modulus_degree=4096,
    plain_modulus=1032193
)

# sk = context.secret_key()
# bcontext.make_context_public()
print(len(context.serialize()))


def twice(x):  # 定义函数
    return x * 2


def get_context():
    return context.serialize()


def get_share(bob):
    return


def get_result(share):
    cipher = ts.BFVVector.load(context, share.data)
    plain = cipher.decrypt()
    return plain


def get_cipher():
    temp = encrypted_vector.serialize()
    a = bytes(0)
    for i  in range(0, 10):
        a = a + plain_share1[i].to_bytes(2, "big", signed=False)
    print("share1 len = ", len(a))
    return temp + a


if __name__ == '__main__':
    s = SimpleXMLRPCServer(("0.0.0.0", 9292))
    s.register_function(twice)
    s.register_function(get_context)
    s.register_function(get_result)
    s.register_function(get_cipher)

    plain_vector = []
    for i in range(0, 10):
        plain_vector.append(random.randint(0, 1000))
    plain_share0 = []
    plain_share1 = []
    for i in range(0, 10):
        plain_share0.append(random.randint(0, plain_vector[i]-1))
        plain_share1.append(plain_vector[i] - plain_share0[i])

    print(plain_vector)
    print(plain_share0)
    print(plain_share1)

    encrypted_vector = ts.bfv_vector(context, plain_vector)

    s.serve_forever()
