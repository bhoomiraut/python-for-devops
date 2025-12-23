
import requests

API_KEY = "AIzaSyCx4Uv_5B8pPnti6l40jFBdDkU-Q2PHvZA"
BASE_URL = "https://www.googleapis.com/youtube/v3/search"

#https://console.cloud.google.com/apis/library/ - tryout free apis here 

def search_youtube(query_text):

    query = (
        f"?part=snippet"
        f"&q={query_text}"
        f"&type=video"
        f"&maxResults=5"
        f"&key={API_KEY}"
    )

    full_url = BASE_URL + query
    response = requests.get(full_url)

    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        return

    data = response.json()

    for item in data.get("items", []):
        title = item["snippet"]["title"]
        channel = item["snippet"]["channelTitle"]
        video_id = item["id"]["videoId"]

        print("\nTitle:", title)
        print("Channel:", channel)
        print("URL: https://www.youtube.com/watch?v=" + video_id)


if __name__ == "__main__":
    search_youtube(input("Enter vdo search term: "))
  