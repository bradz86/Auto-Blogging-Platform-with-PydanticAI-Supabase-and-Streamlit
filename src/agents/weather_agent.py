"""
    Weather Agent Structure
    Following PydanticAI's weather agent documentation example
    """
    from dataclasses import dataclass
    from typing import Any, Optional
    from pydantic_ai import Agent, RunContext, ModelRetry
    from httpx import AsyncClient

    @dataclass
    class WeatherDependencies:
        """
        Dependencies for weather agent
        """
        client: AsyncClient
        weather_api_key: Optional[str]
        geo_api_key: Optional[str]

    # Initialize weather agent
    weather_agent = Agent(
        'openai:gpt-4o',
        deps_type=WeatherDependencies,
        system_prompt=(
            'Provide concise weather reports. '
            'Use the `get_lat_lng` tool for location coordinates and '
            '`get_weather` tool for weather data.'
        ),
        retries=2
    )

    @weather_agent.tool
    async def get_lat_lng(
        ctx: RunContext[WeatherDependencies], 
        location_description: str
    ) -> dict[str, float]:
        """
        Get latitude and longitude for a location

        Args:
            ctx: Run context with dependencies
            location_description: Location name or description

        Returns:
            Dictionary with latitude and longitude
        """
        # Implementation would go here
        pass

    @weather_agent.tool
    async def get_weather(
        ctx: RunContext[WeatherDependencies],
        lat: float,
        lng: float
    ) -> dict[str, Any]:
        """
        Get weather data for coordinates

        Args:
            ctx: Run context with dependencies
            lat: Latitude
            lng: Longitude

        Returns:
            Dictionary with weather data
        """
        # Implementation would go here
        pass

    async def get_weather_report(locations: str) -> str:
        """
        Get weather report for multiple locations

        Args:
            locations: Comma-separated list of locations

        Returns:
            Formatted weather report
        """
        # Implementation would go here
        pass
