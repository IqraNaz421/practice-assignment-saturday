# # 🧠 AI Practice Assignments (Chainlit Projects)

This repository contains 3 mini AI projects built using **Chainlit**, simulating real-world agentic use cases with OpenAI integration.

---

## 📁 Project 1: Career Mentor Agent

### 🎯 What It Does:
- Acts as a career guide bot.
- Suggests fields like **Software Engineering** or **Data Science**.
- Provides a skill roadmap and real-world job roles.

### 🛠️ Technologies:
- `Chainlit`
- `OpenAI`
- `dotenv` (for API key)

### 💡 Features:
- Field suggestion based on input
- Skill roadmap and job roles
- Multi-stage agent handling

### 🧠 Agent Roles:
- **CareerAgent**: Suggests career paths
- **SkillAgent**: Returns skill roadmap
- **JobAgent**: Suggests job roles

---

## 📁 Project 2: AI Travel Designer Agent

### ✈️ What It Does:
- Plans travel based on mood or interests (e.g., adventure, culture).
- Suggests destinations, flights, hotels, and places to explore.

### 🧩 Agent Roles:
- **DestinationAgent**: Suggests destination based on interest
- **BookingAgent**: Returns mock flights & hotels
- **ExploreAgent**: Suggests places to visit and eat

### ⚙️ Tools:
- `Chainlit`, `dotenv`
- Mock data for flights, hotels, and exploration

### 🧭 Flow:
1. User gives interest
2. Destination suggested
3. Flights + Hotels shown
4. Places to explore listed

---

## 📁 Project 3: Fantasy Game Master Agent

### 🧙 What It Does:
- Runs a fantasy text-based adventure game.
- You explore, fight monsters, and receive rewards.

### 🧩 Agent Roles:
- **NarratorAgent**: Tells story & generates events
- **MonsterAgent**: Handles combat
- **ItemAgent**: Rewards you with items

### 🎮 Gameplay Flow:
1. Type `start` to begin
2. Game progresses through events
3. Fight monsters if needed
4. Receive magical rewards
5. Loop continues until game over

---

## 🔐 Environment Setup

Create a `.env` file in each project folder:

