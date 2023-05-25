"""
This program prints TV shows as well as the number of seasons in a selected TV show from an API
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

    # If the response status code is 200 (OK), return a list of TV show results
    if response.status_code == 200:
        shows = response.json()  # Parse the JSON response and return a list of TV show results

        # If the list of shows is not empty, return it
        if shows:
            return shows
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


def get_seasons(show_id: int):
    """
    Get the seasons for a given show_id
    """
    url = BASE_URL + f"shows/{show_id}/seasons"  # Construct the API URL for getting the seasons
    response = requests.get(url)  # Send a GET request to the API endpoint
    if response.status_code == 200:  # If the response status code is 200 (OK), the request was successful
        return response.json()  # Return the JSON data of the response
    else:  # If the response status code is not 200, the request was not successful
        return None  # Return None to indicate that no season information could be obtained


def format_season_name(season: dict):
    """
    Format the season name
    """
    # Retrieve the season number from the dictionary
    number = season['number']

    # Retrieve the year in which the season premiered from the 'premiereDate' field
    # If the 'premiereDate' field is empty, set the start year to '?'
    start_year = season['premiereDate'][:4] if season['premiereDate'] else '?'

    # Retrieve the year in which the season ended from the 'endDate' field
    # If the 'endDate' field is empty, set the end year to '?'
    end_year = season['endDate'][:4] if season['endDate'] else '?'

    # Retrieve the number of episodes in the season from the 'episodeOrder' field
    # If the 'episodeOrder' field is empty, set the episode count to '?'
    episode_count = season['episodeOrder'] if season['episodeOrder'] else '?'
    
    return f"Season {number} ({start_year} - {end_year}), {episode_count} episodes"  # Format and return the season 
    # name with the retrieved fields


def main():
    query = input("Search for a show: ")  # Get the user's search query
    shows = get_shows(query)   # Search for TV shows using the TV Maze API

    # If no TV shows were found, print an error message and exit the program
    if shows is None or len(shows) == 0:
        print("No TV shows found with that name.")
        return

    # Display a list of TV shows and prompt the user to select one
    if not shows:
        print("No results found")
    # Otherwise, print a numbered list of the matching TV shows
    else:
        n = 1
        print("Here are the results:")
        # Loop through the list of results and print each one with a number prefix
        for result in shows:
            formatted_name = format_show_name(result)
            show = result["show"]  # Access the "show" key in the dictionary and retrieve the "name" value
            print(f"{n}. {show['name']} {formatted_name}")  # Print the show name and its number prefix
            n += 1  # Increment the number prefix for the next show
    selection = int(input("Select a show: "))

    # Get the selected show's ID and retrieve its seasons using get_seasons function
    selected_show = shows[selection - 1]['show']
    show_id = selected_show['id']
    seasons = get_seasons(show_id)

    # If no seasons are found for the show, print a message and return
    if seasons is None:
        print("No seasons found for that show.")
        return

    # Print the name of the show and its seasons, with a counter for each season
    print(f"Seasons of {selected_show['name']}:")
    n = 1
    for season in seasons:
        # Format the season name and print the counter with the formatted name
        formatted_season = format_season_name(season)
        print(f"{n}. {formatted_season}")
        n += 1


if __name__ == '__main__':
    main()
