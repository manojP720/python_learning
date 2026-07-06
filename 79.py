import xml.etree.ElementTree as ET
import requests


def fetch_trending_news():
    # URL for Google News Top Stories RSS Feed
    url = "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en"

    print("\n" + "=" * 50)
    print(" 🚀 FETCHING LATEST TRENDING STORIES... 🚀 ")
    print("=" * 50 + "\n")

    try:
        # Send a GET request to the RSS feed
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # Parse the XML content
            root = ET.fromstring(response.content)

            # Loop through the first 10 'item' tags (each represents a trending story)
            for index, item in enumerate(root.findall(".//item")[:10], 1):
                title = item.find("title").text
                link = item.find("link").text
                pub_date = item.find("pubDate").text

                # Clean up the publication date format slightly
                clean_date = " ".join(pub_date.split()[:4])

                # Print the formatted output
                print(f"🔥 {index}. {title}")
                print(f"   📅 Published: {clean_date}")
                print(f"   🔗 Link: {link}")
                print("-" * 50)
        else:
            print(
                f"❌ Failed to retrieve news. Status Code: {response.status_code}"
            )

    except requests.exceptions.RequestException as e:
        print(f"❌ A network error occurred: {e}")
    except ET.ParseError:
        print("❌ Error parsing the news feed data.")


if __name__ == "__main__":
    fetch_trending_news()