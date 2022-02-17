async def test_execute_bytes(async_client):
    assert await async_client.bytes("SELECT arrayJoin([1, 2, 3])") == b"1\n2\n3\n"


async def test_execute_bytes_iter(async_client):
    expected = [b"1\n2\n3\n", b""]
    actual = [x async for x in async_client.iter_bytes("SELECT arrayJoin([1, 2, 3])")]
    assert actual == expected


async def test_execute_text(async_client):
    assert await async_client.text("SELECT arrayJoin([1, 2, 3])") == "1\n2\n3"


async def test_execute_text_iter(async_client):
    expected = ["1\n", "2\n", "3\n"]
    actual = [x async for x in async_client.iter_text("SELECT arrayJoin([1, 2, 3])")]
    assert actual == expected


async def test_execute_json(async_client):
    expected = [{"x": 1}, {"x": 2}, {"x": 3}]
    actual = await async_client.json("SELECT arrayJoin([1, 2, 3]) AS x")
    assert actual == expected


async def test_execute_json_iter(async_client):
    expected = [{"x": 1}, {"x": 2}, {"x": 3}]
    actual = [
        x async for x in async_client.iter_json("SELECT arrayJoin([1, 2, 3]) AS x")
    ]
    assert actual == expected
