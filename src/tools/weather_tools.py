from langchain_core.tools import tool


@tool
def forecast_weather(location: str) -> str:
    """Get the weather forecast for a given location.
    
    Args:
        location: The location to get the weather forecast for.
    
    Returns:
        A string describing the weather forecast.
    """
    res: str = ""
    try:
        weather = get_weather(location)
        res = f"The weather forecast for {location} is: {weather}"
    except ValueError as e:
        res = f"Received a Value Error retrieving the forecast for {locals}. " + str(e)
    return res


def get_weather(location: str) -> str:
    """Get the current weather for a given location.
    
    Args:
        location: The location to get the weather for.

    Raise:
        ValueError: If the location is "Berlin", simulating an error.
        
    Returns:
        A string describing the current weather.
    """
    res: str = ""
    if location.lower() == "munich":
        res = f"The current weather in {location} is cloudy with a temperature of 25°C."
    elif location.lower() == "berlin":
        raise ValueError("Simulated error: Unable to fetch weather data for Berlin.")
    else:
        res = f"Sorry, I don't have weather data for {location}."
    return res
