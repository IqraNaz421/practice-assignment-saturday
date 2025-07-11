def get_career_roadmap(field: str) -> str:
    roadmaps = {
        "software engineering": "1. Learn Python or JavaScript → 2. Study Algorithms → 3. Build real-world projects",
        "data science": "1. Learn Python → 2. Master Pandas/NumPy → 3. Study Machine Learning & Visualization",
        "ui/ux design": "1. Learn Figma/Sketch → 2. Understand Design Principles → 3. Build UI Kits and Prototypes",
        "cybersecurity": "1. Learn Networking Basics → 2. Study Ethical Hacking → 3. Get Certified (e.g., CEH)"
    }
    return roadmaps.get(field, "No roadmap found.")
