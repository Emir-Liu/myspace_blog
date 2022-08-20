import requests

# 测试类
class Test():

    # 测试连接
    def test_connection(self):
        url = 'localhost'
        ans = requests.get('http://localhost:6668/hello')
        print(ans.content)
        return 0

if __name__ == '__main__':
    Test().test_connection()
