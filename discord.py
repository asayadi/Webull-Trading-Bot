import websocket
import json

def send_json_request(ws, request):
    ws.send(json.dumps(request))

def receive_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response) #was json_loads(response) but that wasnt recognized

ws = websocket.WebSocket()
ws.connect("wss://gateway.discord.gg/?v=6&encording=json")
heartbeat_interval = receive_json_response(ws)["d"]["heartbeat_interval"]

token = "see README for instructions on how to get your token for this"

payload = {
    "op": 2,
    "d": {
        "token": token,
        "intents": 513,
        "properties": {
            "$os": 'linux',
            "$browser": 'chrome',
            "$device": 'pc'
        }
    }
}
send_json_request(ws, payload)

while True:
    event = receive_json_response(ws)
    try:
        content = event['d']['content']
        author = event['d']['author']['username']
        print(f'{author}: {content}')
    except:
        pass
