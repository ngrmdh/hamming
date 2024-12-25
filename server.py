import socket
 

def hamming_decode(data):
    data = [int(bit) for bit in data.decode()]

    s0 = data [0] ^ data[2] ^ data[4] ^ data[6]
    s1 = data [1] ^ data[2] ^ data[5] ^ data[6]
    s2 = data [3] ^ data[4] ^ data[5] ^ data[6]

    syndrome = s0 * 1 + s1 * 2 + s2 * 4

    if syndrome != 0:
      print(f"Error detected at bit position: {syndrome}")
      data[syndrome - 1] = 1 - data[syndrome - 1]
    
    decoded_data = ''.join(map(str, data[:4]))
    return decoded_data.encode()

def main():
  
  host = '127.0.0.1'
  port = 65433

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind ((host,port))
    s.listen()
    print('Waiting for a connection...')
    while True: #برای هر اتصال جدید یک سوکت جدید ایجاد می کنه
     conn, addr = s.accept()
     with conn:
      print('Connected by', addr)
      data = conn.recv(1024)
      if not data:
        break
      decoded_data = hamming_decode(data)
      conn.sendall(decoded_data)

if __name__ == '__main__':
  main()      

