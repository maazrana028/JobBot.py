# JobBot.py
The python (made with ChatGPT) program is a great way to demonstrate that we can create a bot that searches our jobs without us spending countless hours manually searching for jobs, this code can help many. However the code does come with minor issues, but the tone has been set.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1. Saves Time & Automates Job Search
Instead of manually searching for jobs every day, the bot automates the process:
Searches for multiple roles.
Scans across different UK cities.
Filters for jobs posted within the last week.
This can save hours daily and ensure you don’t miss fresh opportunities.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2. Keyword Matching for Relevance
Evaluates job descriptions based on keywords from your CV (e.g., technical skills like Windows, Active Directory, etc.).
Scores each job based on how well it matches your skills.
Helps focus on the best-suited roles instead of wasting time on irrelevant ones.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
3. Human-Inclusive Decision-Making
You remain in control: The bot doesn’t apply automatically.
It prompts you:
"Would you like to apply for this job?"
You can choose to apply or skip.
Option to write a personalized message for the hiring manager (good for increasing response rates).

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
4. Generates a Job List
Saves a latest_jobs.txt file with job titles and links.
You can revisit this list later, recheck roles, or apply manually.
Acts as a personal job board tailored to your preferences.

____________________________________________________________________________________________________________________________________________________________________________________________________
Limitations and What the code does for you.

1. Bot Detection on LinkedIn
LinkedIn is strict with bots. You’re already using good stealth techniques:
Masking Selenium detection.
Adding random delays and human-like scrolling.
However, heavy usage (too frequent searches) can still trigger CAPTCHAs or temporary bans.
Avoid running it every day for too many locations/roles. Space out usage.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2. Does Not Apply Automatically
It prompts you for each application, which is good for personalization.
If you want fully automated applications, you’d need to extend the bot to submit applications on LinkedIn Easy Apply jobs.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
4. Limited to Public Job Descriptions
If some jobs have restricted descriptions (e.g., require login), the bot may struggle to retrieve those.
Good for open listings, but private/invite-only roles won’t work.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
6. Not 100% Foolproof
Dynamic page changes on LinkedIn can break the bot if LinkedIn updates its layout.
You may need occasional maintenance (e.g., updating CSS selectors).

