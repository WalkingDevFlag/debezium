from fastapi import WebSocket


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ConnectionManager(metaclass=SingletonMeta):
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket, client_id: str):
        await websocket.accept()
        self.active_connections.append(websocket)
        await self.broadcast(f'Client {client_id} joined the chat')

    async def disconnect(self, websocket: WebSocket, client_id: str):
        self.active_connections.remove(websocket)
        await self.broadcast(f'Client {client_id} left the chat')

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
