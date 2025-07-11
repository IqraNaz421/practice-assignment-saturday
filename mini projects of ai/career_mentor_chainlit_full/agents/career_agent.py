class CareerAgent:
    def suggest_fields(self) -> str:
        return (
            "🧠 Based on your interests, here are some career options:\n\n"
            "**1. Software Engineering** - Build apps, websites, and systems using code.\n"
            "**2. Data Science** - Analyze data to extract insights and build models.\n"
            "**3. UI/UX Design** - Design user-friendly digital experiences and interfaces.\n"
            "**4. Cybersecurity** - Protect systems and data from digital threats.\n\n"
            "👉 Please type the career name you'd like to explore."
        )

    def valid_fields(self):
        return [
            "software engineering",
            "data science",
            "ui/ux design",
            "cybersecurity"
        ]
