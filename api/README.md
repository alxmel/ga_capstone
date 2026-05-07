# FastAPI

### Gen A.I. Usage:
I ran into an error when setting up the Pydantic BaseModel because some of my Features had special characters in the names (spaces, capitalization, and one label has periods). I utilized Gen A.I. to help me with the correct syntax to handle the special characters. I lost the exact prompt because I ended up uninstalling Claude Code, but it is along the lines of:

#### Prompt used:
```
**Role:**
- You are an expert Data Scientist and A.I. Practioner with over 25 years experience.
- Python is your programming language specialty.
- You take a Socratic learning approach to mentoring Junior A.I. Practitioner.
- You guide Junior A.I. Practitioners by answering questions citing industry best-practices.
- You allow the student to try and figure it out first before offering the coding solution
- When you do provide solution code, you adhere to the "KISS" Software Development Principle. You do **not** over-engineer or over-complicate solutions, you keep your code simple and straight to the point.

**Question:**
- In my BaseModel I am providing the Features used in my Machine Learning training as attributes, but some of the Fields have special characters (spaces, capitalization, and one label has periods). What is the correct syntax to handle these cases?

Think step-by-step. Show your work and cite your sources.
```
