import random

class ItemAgent:
    def give_item(self) -> str:
        items = ["🔮 Magic Potion", "🗡️ Silver Sword", "🛡️ Wooden Shield", "📜 Scroll of Wisdom"]
        return random.choice(items)
