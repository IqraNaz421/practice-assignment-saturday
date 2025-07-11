import random

class DestinationAgent:
    def suggest_destination(self, interest: str) -> dict:
        data = {
            "adventure": [
                {
                    "destination": "Queenstown, New Zealand",
                    "reason": "The adventure capital of the world – bungee jumping, skydiving, and white-water rafting!"
                },
                {
                    "destination": "Cape Town, South Africa",
                    "reason": "Experience hiking Table Mountain and shark cage diving!"
                },
                {
                    "destination": "Banff, Canada",
                    "reason": "Majestic mountains, glacier lakes, and top-tier hiking and skiing."
                }
            ],
            "relaxation": [
                {
                    "destination": "Bali, Indonesia",
                    "reason": "Peaceful beaches, luxury spa resorts, and green rice terraces."
                },
                {
                    "destination": "Maldives",
                    "reason": "Private water villas, turquoise water, and total seclusion."
                },
                {
                    "destination": "Santorini, Greece",
                    "reason": "Stunning sunsets, cliffside resorts, and tranquil vibes."
                }
            ],
            "culture": [
                {
                    "destination": "Kyoto, Japan",
                    "reason": "Explore ancient shrines, geisha districts, and tea ceremonies."
                },
                {
                    "destination": "Istanbul, Turkey",
                    "reason": "Blend of East and West with grand mosques and bazaars."
                },
                {
                    "destination": "Cairo, Egypt",
                    "reason": "See the pyramids, sphinx, and ancient Egyptian treasures."
                }
            ],
            "romance": [
                {
                    "destination": "Paris, France",
                    "reason": "City of love – Eiffel Tower views, candle-lit dinners, and charming streets."
                },
                {
                    "destination": "Venice, Italy",
                    "reason": "Gondola rides through canals and romantic piazzas."
                },
                {
                    "destination": "Bruges, Belgium",
                    "reason": "Medieval charm, horse carriages, and beautiful bridges."
                }
            ]
        }

        # Fallback destination if interest is not recognized
        default = {
            "destination": "Barcelona, Spain",
            "reason": "A great mix of beaches, architecture, and nightlife."
        }

        # Get suggestions list based on interest
        suggestions = data.get(interest.lower())
        if suggestions:
            return random.choice(suggestions)
        else:
            return default
