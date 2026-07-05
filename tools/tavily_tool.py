import re
import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def get_salary_information(query: str):

    # ----------------------------------
    # Extract Job Title and Location
    # ----------------------------------
    match = re.search(
        r"(?:average salary for|salary for|salary of|expected salary for)\s+(.*?)\s+in\s+(.*)",
        query,
        re.IGNORECASE
    )

    if match:
        job_title = match.group(1).strip().title()
        location = match.group(2).strip().title()
    else:
        job_title = query.strip().title()
        location = ""

    # ----------------------------------
    # Tavily Search
    # ----------------------------------

    response = client.search(
        query=f"Average salary for {job_title} in {location}",
        search_depth="advanced",
        max_results=1
    )

    salaries = []

    for result in response.get("results", []):

        title = result.get("title", "")
        content = result.get("content", "")

        text = title + " " + content

        # ----------------------------------
        # Salary Extraction
        # ----------------------------------

        matches = re.findall(
            r"(?:₹|Rs\.?|INR|\$)\s*\d[\d,.]*\s*(?:LPA|lakhs?|crore|million|k)?",
            text,
            flags=re.IGNORECASE
        )

        # Remove duplicates
        matches = list(dict.fromkeys(matches))

        if len(matches) == 0:

            estimated_salary = "Not Found"

        elif len(matches) == 1:

            estimated_salary = matches[0]

        else:

            def salary_value(s):

                nums = re.findall(r"\d+(?:\.\d+)?", s)

                if nums:
                    return float(nums[0])

                return 0

            min_salary = min(matches, key=salary_value)
            max_salary = max(matches, key=salary_value)

            estimated_salary = f"{min_salary} - {max_salary}"

        salaries.append({

            "Job Title": job_title,

            "Location": location,

            "Estimated Salary": estimated_salary,

            "Source": title,

            "URL": result.get("url", "")

        })

    return salaries