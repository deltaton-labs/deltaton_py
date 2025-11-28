import socketio
from typing import Dict, Any, Optional, Callable

class DeltatonFeedClient:
  def __init__(self, token: str, user_id: str, host: str = 'https://api.deltaton.com'):
    self.token = token
    self.user_id = user_id
    if not self.token or not self.user_id:
      raise ValueError("token and user_id are required")
    self.host = host
    self.socket = socketio.AsyncClient(
      reconnection=True,
      reconnection_attempts=5,
      reconnection_delay=1,
      reconnection_delay_max=5
    )
    self._setup_events()

  def _setup_events(self):
    @self.socket.event
    async def connect():
      print('Successfully connected to WebSocket')

    @self.socket.event  
    async def connect_error(error):
      print('Connection failed:', error)

    @self.socket.event
    async def error(error):
      print('Error:', error)

    @self.socket.event
    async def disconnect():
      print('Disconnected from WebSocket')

  async def connect(self):
    await self.socket.connect(
      self.host,
      auth={
        'token': f'DeltaFeed {self.token}',
        'userId': self.user_id
      },
      transports=['websocket'],
      wait_timeout=20
    )

  async def emit_data(self, agent_type: str, data: Dict[str, Any], callback: Optional[Callable] = None):
    feed_data = {
      'agentType': agent_type,
      'data': data
    }
    if callback:
      await self.socket.emit('deltatonFeedData', feed_data, callback=callback)
    else:
      await self.socket.emit('deltatonFeedData', feed_data)

  async def disconnect(self):
    await self.socket.disconnect()

  async def wait(self):
    await self.socket.wait()

  async def emit_general(self, data: Dict[str, Any], callback: Optional[Callable] = None):
    await self.emit_data('general', data, callback)

  async def emit_myfarm(self, data: Dict[str, Any], farm_id: str, callback: Optional[Callable] = None):
    await self.emit_data(f'myfarm-{farm_id}', data, callback)