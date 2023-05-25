"""
This program prints out the names of TV shows from an API
Author: Adejumo Toluwani
When: Thursday
"""

import requests


BASE_URL = "https://api.tvmaze.com/"


def get_shows(query: str):
    """
    Search for TV shows using the TV Maze API.
    If the show is not found, return None
    """
    url = BASE_URL + "search/shows"  # Construct the API URL for searching TV shows
    # In the case of the TV Maze API, the q parameter in the query specifies the search query term. For example, if the
    # user searches for "Friends" using the get_shows() function, the q parameter will be set to "Friends". The endpoint
    # will then return a list of TV shows whose name, summary or any other information matches the search term "Friends"
    params = {"q": query}  # Create a dictionary of parameters to send with the API request, including the search query
    response = requests.get(url, params=params)  # response = requests.get(url, params=params)

    # # If the response status code is 200 (OK), return a list of TV show results
    if response.status_code == 200:
        return response.json()  # Parse the JSON response and return a list of TV show results
    else:
        return None


def main():
    """
    Main function
    """
    query = input("Search for a show: ")  # Prompt the user to enter a search query
    results = get_shows(query)  # Call the get_shows function with the user's query and store the results in a variable
    # If no results were found, print a message to the user
    if not results:
        print("No results found")
    # Otherwise, print a numbered list of the matching TV shows
    else:
        n = 1
        print("Here are the results:")
        # Loop through the list of results and print each one with a number prefix
        for result in results:
            show = result["show"]  # Access the "show" key in the dictionary and retrieve the "name" value
            print(f"{n}. {show['name']}")  # Print the show name and its number prefix
            n += 1  # Increment the number prefix for the next show


if __name__ == '__main__':
    main()
