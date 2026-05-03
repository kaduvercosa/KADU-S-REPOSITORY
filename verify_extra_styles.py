import asyncio
from playwright.async_api import async_playwright

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1200, "height": 1000}, color_scheme="dark")

        # Abort requests to external domains except PokeAPI (if possible locally)
        await page.route("**/*", lambda route: route.continue_() if "pokeapi" in route.request.url or "127.0.0.1" in route.request.url or "localhost" in route.request.url else route.abort())

        await page.goto("http://localhost:8000/Pokedex/?id=bulbasaur", wait_until="domcontentloaded")

        # Wait for the image to load
        await page.wait_for_selector("#poke-shiny", state="visible", timeout=10000)
        await page.wait_for_timeout(3000)

        # Light mode capture
        await page.emulate_media(color_scheme="light")
        await page.wait_for_timeout(500)
        await page.screenshot(path="light_extra_styles.png", full_page=True)

        # Dark mode capture
        await page.emulate_media(color_scheme="dark")
        await page.wait_for_timeout(500)
        await page.screenshot(path="dark_extra_styles.png", full_page=True)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
