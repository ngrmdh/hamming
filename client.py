import socket
import random

def generate_random_bit():
    return ''.join(str(random.randint(0,1)) for _ in range(4))
def hamming_encode(data):
    d = [int(bit) for bit in data]
    r = [0,0,0] # بیت توازن
    
    r[0] = d[0] ^ d[1] ^ d[3]
    r[1] = d[0] ^ d[2] ^ d[3]
    r[2] = d[1] ^ d[2] ^ d[3]

    hamming_code = data + ''.join(map(str,r))
    return hamming_code.encode()

def main():
    host = '127.0.0.1'
    port = 65433

    for _ in range(10): #ارسال ۱۰ رشته تصادفی به سرور 
        message = generate_random_bit()
        encoded_message = hamming_encode(message)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(encoded_message)
            data = s.recv(1024)
            print('Sent:', message,'Encoded:', encoded_message.decode(), 'Received:', data.decode())

if __name__ == '__main__':  
    main()