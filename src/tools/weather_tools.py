from langchain_core.tools import tool


@tool
def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
    res: str = ""
    if location.lower() == "munich":
        res = f"The current weather in {location} is cloudy with a temperature of 25°C."
    else:
        res = f"Sorry, I don't have weather data for {location}."
    return res
