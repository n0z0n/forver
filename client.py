import requests
import argparse
import json


def main(host, inputSource):
    url = 'http://localhost:5000/'
    files = {
        'source': (inputSource, open(inputSource, 'rb'), 'text/plain'),
    }
    data = {"option": json.dumps({'style': 'google'})}
    response = requests.post(url, files=files, data=data)
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
