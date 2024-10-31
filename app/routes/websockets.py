import json
from fastapi import APIRouter, WebSocket
from starlette.websockets import WebSocketDisconnect
from typing import List
from aiokafka import AIOKafkaConsumer

router = APIRouter(prefix="/ws")

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@router.websocket("/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            message = f"Client {client_id}: {data}"
            await manager.broadcast(message)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

async def consume_kafka():
    consumer = AIOKafkaConsumer(
        'posgres.public.customers',
        bootstrap_servers='localhost:9092',
        group_id='my-group'
    )
    await consumer.start()
    try:
        while True:
            async for msg in consumer:
                if msg.value:
                    data = json.loads(msg.value)
                    operation = data.get("payload", {}).get("op", {})

                    match operation:
                        case "u":
                            changes = data.get("payload", {}).get("after", {})
                            message = f"Customers [Updated]: {changes}"                        
                        case "c":
                            changes = data.get("payload", {}).get("after", {})
                            message = f"Customers [Created]: {changes}"
                        case "d":
                            changes = data.get("payload", {}).get("before", {})
                            message = f"Customers [Deleted]: {changes}"                            
                    await manager.broadcast(message)
    finally:
        await consumer.stop()

