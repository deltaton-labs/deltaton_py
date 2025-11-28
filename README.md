# Deltaton Python Client
This is a Python client for the Deltaton Feed API. It allows you to connect to the Deltaton websocket and emit data to the Deltaton platform.

## Authentication
1. Create a Deltaton account at https://deltaton.com
2. Contact Deltaton support (support@deltaton.com) to receive your:
   - token - Required for authentication
   - userId - Your unique identifier

## Usage
Yhis is a drop in and use client. Here are steps to get started:
1. Clone the repo
2. Import the DeltatonFeedClient class
3. Connect to the websocket
4. Use the methods to emit data to the Deltaton platform.

## Example
See the [example.py](https://github.com/deltaton-labs/deltaton_feed_py/blob/main/example.py) file for a complete example.

## Methods
The client has the following methods:
- `connect()`
- `disconnect()`
- `emit_general(data: Dict[str, Any], callback: Optional[Callable] = None)`
- `emit_myfarm(data: Dict[str, Any], farm_id: str, callback: Optional[Callable] = None)`