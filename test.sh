#!/bin/bash
curl -X POST \
http://localhost:5000/ \
-H "Content-Type: multipart/form-data" \
-F "option={\"style\":\"google\"}; type=application/json" \
-F "source=@./client.py; type=text/plain"
