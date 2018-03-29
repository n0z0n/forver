import requests
import argparse
import json


def main(host, inputSource):
    with open(inputSource, 'r') as f:
        source = f.read()
    payload = json.dumps({"src": source})
    headers = {'Content-Type': "application/json", 'Cache-Control': "no-cache"}
    response = requests.post(host, data=payload, headers=headers)
    with open(inputSource, 'w') as f:
        f.write(response.json()["formated"])
        f.flush()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument(
        'host', action='store', nargs=None, type=str, help='forver host')
    parser.add_argument(
        'input', action='store', nargs=None, type=str, help='input sourcefile')
    args = parser.parse_args()
    main(args.host, args.input)
