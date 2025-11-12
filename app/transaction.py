import httpx
from app.retry import retry_request

async def call_mock_api(payload):
    async with httpx.AsyncClient() as client:
        response = await client.post("https://httpbin.org/status/500", json=payload)
        response.raise_for_status()
        return response.json()

async def process_transaction(key, payload):
    async def wrapped_call():
        return await call_mock_api(payload)

    result = await retry_request(wrapped_call)
    return {"status": "success", "response": result}