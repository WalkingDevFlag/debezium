from fastapi import APIRouter, WebSocket
from starlette.websockets import WebSocketDisconnect

from app.internal.connection_manager import ConnectionManager

router = APIRouter(prefix='/ws')


manager = ConnectionManager()


@router.websocket('/{client_id}')
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_text()
            message = f'Client {client_id}: {data}'
            await manager.broadcast(message)
    except WebSocketDisconnect:
        await manager.disconnect(websocket, client_id)
