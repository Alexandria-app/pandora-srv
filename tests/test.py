import requests


def make_post_request():
    body = {
        'module': 'youtube',
        'path': r'D:\Dev\Flutter\alexandria\pandora\assets\youtube.py'
    }
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        res = requests.post('http://127.0.0.1:55001/load', json=body, headers=headers)
        print(res.content)

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def test_handle():
    make_post_request()


def get_home():
    try:
        res = requests.get('http://127.0.0.1:55001/script/home')
        print(res.content)

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == '__main__':
    test_handle()
    get_home()
