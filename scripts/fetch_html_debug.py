import httpx
import asyncio

async def fetch_ebay_html(search_term):
    ebay_search_url = f'https://www.ebay.com/sch/i.html?_nkw={search_term.replace(" ", "+")}'
    
    async with httpx.AsyncClient() as client:
        response = await client.get(ebay_search_url)
        response.raise_for_status()
        return response.text

if __name__ == "__main__":
    search_term = input("Enter the product name that you want to search for on eBay: ")

    try:
        html_content = asyncio.run(fetch_ebay_html(search_term))
        print(f"HTML content for eBay search results of '{search_term}':\n")
        print(html_content)

    except httpx.RequestError as e:
        print(f"Request failed: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
