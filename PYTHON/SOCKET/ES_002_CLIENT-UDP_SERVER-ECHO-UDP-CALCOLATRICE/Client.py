import socket as sck


def client():

    host = "192.168.178.33"
    port = 6000     # server port number

    c = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)    # instantiate

    print("Enter 'exit' to end the connection")
    msg = input("->")   # take input

    while True:

        c.sendto(msg.encode(), (host, port))    # send message

        data = c.recv(4096)    # receive message

        print(f"Received from server: Result = {data.decode()}")   # show response

        msg = input("->")   # again take input

        if msg == "exit":
            c.sendto(msg.encode(), (host, port))  # send message
            print("Close the connection")
            break

    c.close()   # close the connection


if __name__ == '__main__':
    client()
