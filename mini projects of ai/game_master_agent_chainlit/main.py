import chainlit as cl
import os
from dotenv import load_dotenv
from agents.narrator_agent import NarratorAgent
from agents.monster_agent import MonsterAgent
from agents.item_agent import ItemAgent

# 🔐 Load API key from .env
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

# Agents Initialization
narrator = NarratorAgent()
monster = MonsterAgent()
item = ItemAgent()

# State Tracking
state = {"stage": "start", "inventory": [], "health": 100}

@cl.on_chat_start
async def start():
    state["stage"] = "intro"
    state["inventory"] = []
    state["health"] = 100

    intro_message = (
        "🧙‍♂️ **Welcome, Brave Adventurer!**\n\n"
        "You have entered a mystical realm filled with danger, monsters, and hidden treasures.\n"
        "Your journey will test your courage, wisdom, and fate.\n\n"
        "✨ **How to play:**\n"
        "- Type `start` to begin your epic quest.\n"
        "- Choose actions like `explore`, `fight`, or `run` when prompted.\n"
        "- Win battles, collect items, and survive the unknown.\n\n"
        "❤️ **Your starting health:** 100\n"
        "🎒 **Inventory will appear as you collect items**\n\n"
        "⚔️ *Type `start` to take your first step into the unknown...*"
    )

    await cl.Message(content=intro_message).send()

@cl.on_message
async def handle_message(message: cl.Message):
    msg = message.content.lower()

    if state["stage"] == "intro" and msg == "start":
        story = narrator.intro()
        state["stage"] = "explore"
        await cl.Message(content=story).send()

    elif state["stage"] == "explore":
        outcome = narrator.generate_event(msg)
        state["stage"] = "combat" if outcome.get("enemy") else "reward"
        await cl.Message(content=outcome["text"]).send()

    elif state["stage"] == "combat":
        result = monster.fight(state["health"])
        state["health"] = result["health"]
        state["stage"] = "reward" if result["won"] else "end"
        await cl.Message(content=result["text"]).send()
        await cl.Message(content=f"❤️ Your health: {state['health']}").send()

    elif state["stage"] == "reward":
        reward = item.give_item()
        state["inventory"].append(reward)
        state["stage"] = "explore"
        await cl.Message(content=f"🎁 You received: {reward}").send()
        await cl.Message(content=f"🎒 Inventory: {', '.join(state['inventory'])}").send()

    elif state["stage"] == "end":
        await cl.Message(content="💀 Game Over! Type `start` to play again.").send()
        state["stage"] = "intro"

    else:
        await cl.Message(content="❓ Type `start` to begin your fantasy adventure!").send()
