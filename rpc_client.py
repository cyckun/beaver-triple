import random
import xmlrpc.client    #导入模块
import tenseal as ts

# Setup TenSEAL context
# context_client = ts.context(
#     ts.SCHEME_TYPE.BFV,
#     poly_modulus_degree=4096,
#     plain_modulus=1032193
# )

if __name__ == '__main__':
    s = xmlrpc.client.ServerProxy('http://0.0.0.0:9292')  # 链接服务端
    print(s.twice(2))  # 调用函数
    context_server = s.get_context()

    # context_client.load(context_server.data)
    context_client = ts.Context.load(context_server.data)
    print("get context ok", len(context_server.data))

    # test cipher
    cipher_stream = s.get_cipher()
    data = cipher_stream.data

    server_share1_bytes = []
    for i in range(0, 20):
        server_share1_bytes.append(data[len(data)-i-1])
    cipher = ts.BFVVector.load(context_client, cipher_stream.data[:len(data)-20])


    ll = len(server_share1_bytes)
    server_share1 = []
    for i in range(0, 10):
        server_share1.append(server_share1_bytes[ll-2*i-1]*256 + server_share1_bytes[ll-2*i-2])
    print("load ok, server share1 = ", server_share1)

    bob_plain = []
    bob_share0 = []
    bob_share1 = []
    bob_r = []
    for i in range(0, 10):
        bob_plain.append(random.randint(0, 1000))
        bob_r.append(random.randint(0, 1000))
        bob_share0.append(random.randint(0, bob_plain[i]))
        bob_share1.append(bob_plain[i] - bob_share0[i])
    cipher = bob_plain * cipher - bob_r
    # cipher = cipher - [1, 1, 1]

    plain = s.get_result(cipher.serialize())

    print(plain)




