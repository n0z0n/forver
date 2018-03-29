#!/bin/bash
curl -i -X POST \
http://localhost:5000/ \
-H "Content-Type: multipart/form-data" \
-F "metadata={\"edipi\":123456789}; type=application/json" \
-F "file=@./client.py; type=plain/text"
