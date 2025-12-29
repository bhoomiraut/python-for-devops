
import requests

API_KEY = "AIzaSyCx4Uv_5B8pPnti6l40jFBdDkU-Q2PHvZA"
BASE_URL = "https://www.googleapis.com/youtube/v3/search"

#https://console.cloud.google.com/apis/library/ - tryout free apis here 

#----------------------------------------------------------------------------------------------------
    #try and except block for exception handling
# --> to ckeck except block, disconnect internet and run the code or use wrong Base URL or wrong API key
#----------------------------------------------------------------------------------------------------

def search_youtube(query_text):
    try:  
        query = (f"?part=snippet&q={query_text}&type=video&maxResults=5&key={API_KEY}")
                    
        full_url = BASE_URL + query
        response = requests.get(full_url, timeout=10) #not required, but useful in devops scripts

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

    except requests.exceptions.RequestException: 
        print("Network or API error occurred. Please check your API or internet connection.")

    except Exception as e:
        print("Unexpected error:", e) 

if __name__ == "__main__":
    search_youtube(input("Enter vdo search term: "))
  