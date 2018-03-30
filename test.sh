#!/bin/bash
curl -i -X POST \
	-F "option={\"style\":\"google\"};type=application/json" \
	-F "source=@./client.py" \
	http://localhost:5000/
