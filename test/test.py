import requests

def test_connection():
    url = 'localhost'
    ans = requests.get('http://localhost:6668/hello')
    print(ans.content)
    return 0

if __name__ == '__main__':
    test_connection()
