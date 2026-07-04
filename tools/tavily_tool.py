import re
from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def get_salary_information(job_title, location=""):

    response = client.search(
        query=f"Average salary for {job_title} in {location}",
        search_depth="advanced",
        max_results=1
    )

    salaries = []

    for result in response.get("results", []):

        text = result["content"]

        salary = "Not Found"

        match = re.search(r"\$[\d,]+", text)

        if match:
            salary = match.group()

        salaries.append({

            "Job": job_title,

            "Estimated Salary": salary,

            "Source": result["title"],

            "URL": result["url"]

        })

    return salaries