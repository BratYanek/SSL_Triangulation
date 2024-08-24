import numpy as np
import socket
import json
import intersection_algorythm as ta

                                                                ##########################################
                                                                #                                        #
                                                                # NETWORK CONNECTION AND DATA PROCESSING #
                                                                #                                        #
                                                                ##########################################


def handle_client(conn, addr):
    print(f"Connection established from {addr}")

    try:
        while True:
            data = conn.recv(1024)  # Adjust buffer size as needed
            if not data:
                print(f"Connection closed from {addr}")
                break

            # Decode the received JSON and convert to Python list
            received_data = json.loads(data.decode('utf-8'))
            #print(f"Received data from {addr}: {received_data}")

            # Assuming received_data is a list [x, y]
            if isinstance(received_data, list) and len(received_data) == 2:

                # Angles received form nodes
                azimuth, elevation = received_data
                data = np.array([addr[0], azimuth, elevation])
                print(data)
                return(data)
                
    except KeyboardInterrupt:
        print(f"Interrupt received. Closing connection from {addr}")

    conn.close()

def start_server():
    host = '0.0.0.0'                # Listen on all available interfaces
    port = 12345                    # Choose a port number

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print(f"Listening for connections on {host}:{port}")

        try:
            while True:
                conn, addr = server_socket.accept()
                data = handle_client(conn, addr)
                return(data)

        except KeyboardInterrupt:
            print("Server interrupted. Closing.")

def build_data_matrix(data):
    # building data matrix, where each row with unique IP responds to different node
    
    if data[0] == IP_node1:
        data_matrix[0][0] = data[0] 
        data_matrix[0][1] = data[1] 
        data_matrix[0][2] = data[2] 

    elif data[0] == IP_node2:
        data_matrix[1][0] = 8 
        data_matrix[1][1] = data[1] 
        data_matrix[1][2] = data[2] 
    print(data_matrix)
    return data_matrix

data_matrix = np.zeros((2,), dtype=[('IP', 'U15'), ('Value1', float), ('Value2', float)])

if __name__ == "__main__":
        
    # Set IP addres of each node 
    IP_node1 = '192.168.101.10'
    IP_node2 = '192.168.101.9'

    try:
        while True:
            data = start_server()
            data_matrix = build_data_matrix(data=data)
            ta.intersection(data_matrix=data_matrix)
    
    except KeyboardInterrupt:
        print("Server interrupted. Closing.")
