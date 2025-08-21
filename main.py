import requests
import urllib.parse as parse

# Trick: Pretend to be an old browser (like Netscape/Opera from early 2000s)
# These old browsers cannot display reCAPTCHAs, and Google knows it.
# So in many cases, Google just skips showing Captchas.
USER_AGENT = "Mozilla/4.0 (compatible; MSIE 6.0; Nitro) Opera 8.50 [ja]"

HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept-Language": "en-US,en;q=0.5"
}

def send_query(query: str) -> str:
    """
    Send a search query to Google and return the raw HTML results.
    
    Args:
        query (str): The search keyword(s).
    
    Returns:
        str: The HTML content of the Google search result page.
    """
    session = requests.Session()

    # Step 1: Handle Google's consent screen (needed in EU/strict regions).
    # Here we send a POST request to "consent.google.com/save"
    # with minimal parameters to skip cookie consent.
    session.post(
        "https://consent.google.com/save",
        headers=HEADERS,
        data={
            "set_eom": True,
            "uxe": "none",
            "hl": "en",
            "pc": "srp",
            "gl": "DE",  # country code
            "x": "8",
            "bl": "user",
            "continue": "https://www.google.com/"
        }
    )

    # Step 2: Perform the actual Google search
    url = f"https://www.google.com/search?hl=en&q={parse.quote(query)}"
    response = session.get(url, headers=HEADERS)

    # Return the HTML source
    return response.text


# Example usage
if __name__ == "__main__":
    html = send_query("python web scraping tricks")
    print(html[:1000])  # Print first 1000 characters of the result
