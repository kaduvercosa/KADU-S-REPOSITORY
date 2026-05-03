import asyncio
from playwright.async_api import async_playwright

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()

        # Desktop
        desktop_page = await browser.new_page(viewport={"width": 1200, "height": 1000}, color_scheme="dark")
        await desktop_page.route("**/*", lambda route: route.continue_() if "pokeapi" in route.request.url or "127.0.0.1" in route.request.url or "localhost" in route.request.url else route.abort())
        await desktop_page.goto("http://localhost:8000/Pokedex/?id=bulbasaur", wait_until="domcontentloaded")
        await desktop_page.wait_for_selector("#poke-shiny", state="visible", timeout=10000)
        await desktop_page.wait_for_timeout(3000)
        await desktop_page.screenshot(path="desktop_layout.png", full_page=True)
        await desktop_page.close()

        # Mobile
        mobile_page = await browser.new_page(viewport={"width": 375, "height": 812}, color_scheme="dark", user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1")
        await mobile_page.route("**/*", lambda route: route.continue_() if "pokeapi" in route.request.url or "127.0.0.1" in route.request.url or "localhost" in route.request.url else route.abort())
        await mobile_page.goto("http://localhost:8000/Pokedex/?id=bulbasaur", wait_until="domcontentloaded")
        await mobile_page.wait_for_selector("#poke-shiny", state="visible", timeout=10000)
        await mobile_page.wait_for_timeout(3000)
        await mobile_page.screenshot(path="mobile_layout.png", full_page=True)
        await mobile_page.close()

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
