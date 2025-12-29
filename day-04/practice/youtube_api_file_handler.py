import requests

API_KEY = "AIzaSyCx4Uv_5B8pPnti6l40jFBdDkU-Q2PHvZA"
BASE_URL = "https://www.googleapis.com/youtube/v3/search"


def write_results_to_file(results):
    try:
        with open("youtube_results.txt", "w") as output_file:
            output_file.write("YouTube Search Results\n")

            if not results:
                output_file.write("No results found.\n")
                return

            for video in results:
                output_file.write(f"Title: {video['title']}\n")
                output_file.write(f"Channel: {video['channel']}\n")
                output_file.write(f"URL: {video['url']}\n\n")

    except Exception as e:
        print("Error while writing results to file:", e)


def search_youtube(query_text):
    try:
        query = (
            f"?part=snippet&q={query_text}"
            f"&type=video&maxResults=5&key={API_KEY}"
        )

        full_url = BASE_URL + query
        response = requests.get(full_url)

        if response.status_code != 200:
            print("API error:", response.status_code)
            print(response.text)
            write_results_to_file([])   # still create file safely
            return

        data = response.json()
        items = data.get("items", [])

        if not items:
            print("No results found.")
            write_results_to_file([])
            return

        results = []

        for item in items:
            title = item["snippet"]["title"]
            channel = item["snippet"]["channelTitle"]
            video_id = item["id"]["videoId"]
            url = "https://www.youtube.com/watch?v=" + video_id

            print("\nTitle  :", title)
            print("Channel:", channel)
            print("URL    :", url)

            results.append({
                "title": title,
                "channel": channel,
                "url": url
            })

        write_results_to_file(results)

        print("\nResults saved to youtube_results.txt")

    except requests.exceptions.RequestException:
        print("Network or API error occurred.")
        write_results_to_file([])

    except Exception as e:
        print("Unexpected error:", e)
        write_results_to_file([])


def main():
    query = input("Enter video search term: ")
    search_youtube(query)


if __name__ == "__main__":
    main()
