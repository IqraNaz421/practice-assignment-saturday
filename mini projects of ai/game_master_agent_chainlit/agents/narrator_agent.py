class NarratorAgent:
    def intro(self):
        return "🏰 You awaken in a mysterious forest near a dark castle. What do you do?"

    def generate_event(self, action: str) -> dict:
        if "castle" in action:
            return {"text": "You approach the castle and a monster appears!", "enemy": True}
        elif "forest" in action:
            return {"text": "You wander deeper into the forest and find a hidden treasure chest!", "enemy": False}
        else:
            return {"text": "You roam the land... it's quiet... too quiet.", "enemy": False}
