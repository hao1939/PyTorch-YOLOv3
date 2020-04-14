FROM yoanlin/opencv-python3

# RUN git clone https://github.com/hao1939/PyTorch-YOLOv3.git
COPY . /PyTorch-YOLOv3

RUN cd /PyTorch-YOLOv3/ && pip install -r requirements.txt
# RUN cd /PyTorch-YOLOv3/weights/ && bash download_weights.sh

WORKDIR /PyTorch-YOLOv3

ENV FLASK_DEBUG=true
ENV FLASK_APP=server.py
ENV FLASK_RUN_PORT=5001
EXPOSE 5001
CMD flask run --host=0.0.0.0

# sudo docker build -t yolo .
# sudo docker run -d -p 5001:5001 yolo
# curl -X POST http://127.0.0.1:5001/score --header "Content-Type:application/octet-stream" --data-binary "@data/samples/dog.jpg" -v

#curl -X POST http://mir-yolo-14-ws.mir-yolo-14.mirstg.westus2.mi-azureml.net/score --header "Content-Type:application/octet-stream" --data-binary "@data/samples/dog.jpg" -v
