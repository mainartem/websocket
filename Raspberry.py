import socket
import cv2
HOST = '127.0.1.1' # The server's hostname or IP address
PORT = 65432        # The port used by the server
capture = cv2.VideoCapture(0)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Предположим, что video_stream - это ваш видеопоток
    while True:

        ret, video_stream = capture.read()
        data = cv2.imencode('.jpg', video_stream)[1].tostring()
        s.sendall(data)

capture.release()
