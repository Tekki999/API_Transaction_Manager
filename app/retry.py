import asyncio

async def retry_request(func, max_attempts=3, backoff=2):
    for attempt in range(max_attempts):
        try:
            return await func()
        except Exception as e:
            await asyncio.sleep(backoff ** attempt)
    return {"status": "failed", "error": "Max retries exceeded"}