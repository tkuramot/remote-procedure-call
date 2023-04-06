const net = require("node:net");

const socket_path = "./socket_file"

class Client {
    constructor(address) {
        this.__socket = net.createConnection(address);
        this.__socket.setTimeout(3000);
        this.__socket.on("connect", () => {
            console.log("connected");
        });
        this.__socket.on("data", (data) => {
            console.log(data.toString());
        });
        this.__socket.on("end", () => {
            console.log("disconnected");
        });
        this.__socket.on("timeout", () => {
            console.log("socket timeout");
            this.__socket.destroy();
        })
        this.__socket.on("error", (err) => {
            console.error(err.message);
        });
    }
    write(data) {
        this.__socket.write(data);
    }
    destroy() {
        this.__socket.destroy();
    }
}

data = [
    {
        "method": "floor",
        "params": 2.345,
        "param_types": "double",
        "id": 1
    },
    {
        "method": "nroot",
        "params": [2, 4],
        "param_types": ["int", "int"],
        "id": 1
    },
    {
        "method": "reverse",
        "params": "abcdefg",
        "param_types": "string",
        "id": 1
    },
    {
        "method": "validAnagram",
        "params": ["abcdefg", "gfedcba"],
        "param_types": ["string", "string"],
        "id": 1
    },
    {
        "method": "sort",
        "params": ["kiwi", "banana", "apple", "orage"],
        "param_types": "string[]",
        "id": 1
    }
]

for(let i = 0; i < data.length; i++) {
    let client = new Client(socket_path);
    client.write(JSON.stringify(data[i]));
}
