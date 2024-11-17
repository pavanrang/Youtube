import requests
from typing import List
from termcolor import colored

def search_for_stock_videos(tags: list, api_key: str) -> List[str]:
    headers = {
        "Authorization": api_key
    }

    links = []

    for tag in tags:
        url = f"https://api.pexels.com/videos/search?query={tag}&per_page=1"
        r = requests.get(url, headers=headers)
        response = r.json()
        video_urls = []
        video_url = ""
        try:
            video_urls = response["videos"][0]["video_files"]
            # print(video_urls)
        except:
            print(colored("[-] No Videos found.", "red"))
            print(colored(response, "red"))

        for video in video_urls:
            if ".com/video-" in video["link"]:
                video_url = video["link"]
                # print(f"{video_url} | {video['quality']} | {video['width']}/{video['height']}")

        print(colored(f"\t=> {video_url}", "cyan"))
        links.append(video_url)

    return links


#example usage
# tags = [
#     "Movie Scenes",
#     "Film Characters",
#     "Action Sequences",
#     "Superhero Movies",
#     "Adventure Films",
#     "Classic Cinema",
#     "Iconic Moments",
#     "Hollywood Blockbusters",
#     "Cult Favorites",
#     "Movie Posters"
# ]

# print(type(tags))
# links = search_for_stock_videos(tags,api_key="nMCqvCEfIc6j3eNHaZ9vfLXiVjZb8j5bVtzUmYKj9QIpXKU93XbJhdLe")
# print(links)

