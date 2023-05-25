"""
This program prints additional information alongside the names of TV shows
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
    params = {"q": query}  # Create a dictionary of parameters to send with the API request, including the search query
    response = requests.get(url, params=params)  # response = requests.get(url, params=params)

    # # If the response status code is 200 (OK), return a list of TV show results
    if response.status_code == 200:
        return response.json()  # Parse the JSON response and return a list of TV show results
    else:
        return None


def format_show_name(show: dict):
    """
    Format the show name.
    """
    premiere = show['show']['premiered'][:4] if show['show']['premiered'] else '?'  # Extract the first 4 characters of
    # the 'premiered' string, or use '?' if it's empty
    end = show['show']['ended'][:4] if show['show']['ended'] else '?'  # Extract the first 4 characters of the 'ended'
    # string, or use '?' if it's empty
    genres = ', '.join(show['show']['genres']) if show['show']['genres'] else '?'  # Join the list of 'genres' with
    # commas, or use '?' if it's empty
    return f"({premiere} - {end}, {genres})"  # Return a formatted string with the premiere year, end year, and genres

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
            formatted_name = format_show_name(result)
            show = result["show"]  # Access the "show" key in the dictionary and retrieve the "name" value
            print(f"{n}. {show['name']} {formatted_name}")  # Print the show name and its number prefix
            n += 1  # Increment the number prefix for the next show


if __name__ == '__main__':
    main()
