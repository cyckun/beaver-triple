
import random
import tenseal as ts
import socket
import tcp_server
import threading


# Setup TenSEAL context
context = ts.context(
            ts.SCHEME_TYPE.BFV,
            poly_modulus_degree=4096, 
            plain_modulus=1032193
          )

sk = context.secret_key()
pk = context.public_key()


if __name__ == "__main__":
    server = tcp_server.TcpServer()
    server.listenPort()
    thrd = threading.Thread(target=server.getMessage)
    thrd.setDaemon(True)
    thrd.start()
    server.sendMessage("hete")

    #

    v3 = []
    for i in range(0, 10):
        num = random.randint(1, 1000)
        v3.append(num)
    print("plain = ", v3)
    enc_v3 = ts.bfv_vector(context, v3)

    enc_v3 = enc_v3 * enc_v3
    result_v3 = enc_v3.decrypt()
    print("v3 result =", result_v3)



