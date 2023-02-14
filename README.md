# __Remote procedure call__
## __Description__
ソケット通信によるremote procedure callです。<br>
サーバはPythonで、クライアントはnode.jsを介したJavaScript実装しています。<br>
JSONファイルをサーバに送信し、サーバはレスポンスとしてJSONファイルを返します。
- Request
```
{
    "method": "floor",
    "params": 2.345,
    "param_types": "double",
    "id": 1
}
```
- Response
```
{
    "results": "2",
    "result_type": "int",
    "id": 1
}
```
## __Usage__
- Server
```
python3 server.py
```
- Client
```
npm start
```
## __Example__
- Server
![](https://user-images.githubusercontent.com/106866329/218774992-8396c70a-b9ff-432a-8027-888216b46df9.png)
- Client
![](https://user-images.githubusercontent.com/106866329/218775020-a6ddbc69-22a8-4ec2-8989-87e43eae5380.png)
## __Reference__
- [socket --- 低水準ネットワークインターフェース](https://docs.python.org/ja/3/library/socket.html)
- [PythonでUnixドメインソケットを使って通信する - 偏った言語信者の垂れ流し](https://tokibito.hatenablog.com/entry/20150927/1443286053)
- [今更ながらソケット通信に入門する（Pythonによる実装例付き） - Qiita](https://qiita.com/t_katsumura/items/a83431671a41d9b6358f)
- [PythonソケットによるTCP通信入門 – なゆたり](https://nayutari.com/python-socket)
- [Node.js v19.6.0 documentation](https://nodejs.org/api/net.html#socketconnectpath-connectlistener)
- [Node.jsでもUNIXドメインソケットを使いたい - Qiita](https://qiita.com/walk8243/items/49ce3fc24500038f126f)
- [for文内でsetTimeoutを使うときの変数のスコープとクロージャ](https://kakechimaru.com/scope_closure/
)