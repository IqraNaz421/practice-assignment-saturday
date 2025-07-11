import random

class MonsterAgent:
    def fight(self, health: int) -> dict:
        damage = random.randint(10, 30)
        health -= damage
        if health > 0:
            return {"text": f"⚔️ You defeated the monster but lost {damage} HP. Remaining HP: {health}", "health": health, "won": True}
        else:
            return {"text": f"☠️ The monster overpowered you. You died!", "health": 0, "won": False}
