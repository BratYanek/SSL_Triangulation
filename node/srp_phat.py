import time
import torch
import numpy as np
import socket
import json

from src.utilis.ssl import doa_detection
from src.mic.audio_recorder import get_microphone_chunks

def send(azimuth, elevation):
    host = '192.168.101.5'
    port = 12345
    
    azimuth_elevation = np.array([azimuth, elevation])
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        json_data = json.dumps(azimuth_elevation.tolist())
                
        client_socket.sendall(json_data.encode('utf-8'))

def main():
    try:
            for sample_rate, waveform in get_microphone_chunks(
                rate=16000,
                chunk=1600,
                n_channels=4,
                min_to_cumulate=3,
                max_to_cumulate=10,
            ):
                print(waveform)
                waveform = waveform.T
                waveform = np.array([waveform])
                print('Torch: ', torch.from_numpy(waveform))
                doas = doa_detection(torch.from_numpy(waveform))
                doas[doas[:, 0] < 0] += torch.FloatTensor([[360, 0]])
                for doa in doas:
                    print(f"azi: {doa[0]: 6.1f}, ele: {doa[1]: 6.1f}")
                    azimuth = float(doa[0])
                    elevation = float(doa[1])
                    send(azimuth, elevation)
                print("="*51)

    except KeyboardInterrupt:
        exit()


if __name__ == '__main__':
    main()

