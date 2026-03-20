import requests

def search_web(query):
    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json"
        response = requests.get(url).json()

        if response.get("Abstract"):
            return response["Abstract"]
        else:
            return "No useful web result found."
    except:
        return "Web search failed."