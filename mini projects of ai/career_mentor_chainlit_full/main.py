


import chainlit as cl
import os
from dotenv import load_dotenv
from agents.career_agent import CareerAgent
from agents.skill_agent import SkillAgent
from agents.job_agent import JobAgent

# 🔐 Load .env API key
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

# Agent instances
career_agent = CareerAgent()
skill_agent = SkillAgent()
job_agent = JobAgent()

# State tracker
state = {"stage": "start", "field": ""}


@cl.on_chat_start
async def start():
    state["stage"] = "career"
    await cl.Message(content="💼 Welcome to the Career Mentor Agent!\nType `career help` to explore career options.").send()


@cl.on_message
async def main(message: cl.Message):
    msg = message.content.lower()

    if state["stage"] == "career":
        if "career" in msg:
            state["stage"] = "skill"
            await cl.Message(content=career_agent.suggest_fields()).send()
        else:
            await cl.Message(content="❓ Please type `career help` to begin.").send()

    elif state["stage"] == "skill":
        if msg in career_agent.valid_fields():
            state["field"] = msg
            state["stage"] = "job"
            roadmap = skill_agent.get_roadmap(msg)
            await cl.Message(content=f"📚 Skill Roadmap for **{msg.title()}**:\n{roadmap}").send()
        else:
            await cl.Message(content="❓ Please choose one of the suggested fields (e.g. software engineering, ui/ux, cybersecurity).").send()

    elif state["stage"] == "job":
        field = state["field"]
        roles = job_agent.get_roles(field)
        await cl.Message(content=f"💼 Real-world roles in **{field.title()}** include:\n{roles}").send()
        await cl.Message(content="🎯 Type `career help` to explore again.").send()
        state["stage"] = "career"

    else:
        await cl.Message(content="✅ You're done! Type `career help` to restart.").send()
        state["stage"] = "career"
