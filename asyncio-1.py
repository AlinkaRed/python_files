import asyncio
import json
import signal
from aiohttp import ClientSession, web


async def get_weather(city):
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            try:
                return weather_json["weather"][0]["main"]
            except KeyError:
                return 'Нет данных'


async def handle(request):
    city = request.rel_url.query['city']
    weather = await get_weather(city)
    result = {'city': city, 'weather': weather}

    return web.Response(text=json.dumps(result, ensure_ascii=False))


async def main(host='127.0.0.1', port=8080):
    print(f'Старт сервера на {host}:{port}')
    app = web.Application()
    app.add_routes([web.get('/weather', handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host, port)
    await site.start()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

# await main()

# http://localhost:8080/weather?city=Sochi
# http://localhost:8080/weather?city=Sochi