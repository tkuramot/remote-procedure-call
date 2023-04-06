import json
import math
import os
import socket
import threading


class Server:
    def __init__(self, address, timeout:int = 10, buffer:int = 1024):
        self.__socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.__timeout = timeout
        self.__address = address
        self.__buffer = buffer

    def start(self) -> None:
        # ファイルが既に存在しないことを確認する
        try:
            os.unlink(self.__address)
        except FileNotFoundError:
            pass
        # ソケットをアドレスに紐付ける
        self.__socket.bind(self.__address)
        self.__socket.listen()
        self.accept()

    # クライアントからの接続を処理する
    # 接続待ちはメインスレッドで行う
    def accept(self) -> None:
        while True:
            connection, _ = self.__socket.accept()
            connection.settimeout(self.__timeout)
            # データの受信待ちはサブスレッドで行う
            thread = threading.Thread(target=self.recv, args=(connection,))
            thread.start()

    # データの受信をする
    def recv(self, connection):
        try:
            while True:
                data = connection.recv(self.__buffer)
                self.respond(connection, data.decode())
        except:
            pass

    def respond(self, connection, data:str) -> str:
        if data:
            print("receiving -> ", data)
        # str型のデータをjson(dict型)にキャストして渡す
        response = JsonProcessor.process(json.loads(data))
        print("sending -> ", response)
        connection.send(str(response).encode())


# 受信したjson形式のデータを処理する
class JsonProcessor:
    processor = {
        # key: (func, return type)
        "floor": (lambda x: math.floor(x), "int"),
        "nroot": (lambda params: (params[1] ** (1 / params[0])), "double"),
        "reverse": (lambda s: s[::-1], "string"),
        "validAnagram": (lambda params: set(params[0]) == set(params[1]), "string"),
        "sort": (lambda strArr: sorted(strArr), "string[]")
    }

    @staticmethod
    def process(jsonData):
        try:
            method = jsonData["method"]
            params = jsonData["params"]
            id = jsonData["id"]

            ans = JsonProcessor.processor[method][0](params)
            ansType = JsonProcessor.processor[method][1]
            return JsonProcessor.generateResponse(ans, ansType, id)
        except Exception as e:
            return {"error": e}

    def generateResponse(results, resultType, id):
        return {
            "results": results,
            "result_types": resultType,
            "id": id
        }


def main():
    socket_path = "./socket_file"
    server = Server(socket_path)
    server.start()


if __name__ == "__main__":
    main()