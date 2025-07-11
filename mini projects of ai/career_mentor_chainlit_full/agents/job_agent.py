class JobAgent:
    def get_roles(self, field: str) -> str:
        jobs = {
            "software engineering": "- Frontend Developer\n- Backend Developer\n- Mobile App Developer",
            "data science": "- Data Analyst\n- Machine Learning Engineer\n- Research Scientist",
            "ui/ux design": "- UI Designer\n- UX Researcher\n- Product Designer",
            "cybersecurity": "- Security Analyst\n- Penetration Tester\n- SOC Engineer"
        }
        return jobs.get(field, "No roles found.")
