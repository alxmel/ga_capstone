# ga_capstone
Capstone Project for the Applied AI and Deep Learning General Assembly Course

## How to Run
1. Navigate to the [Backend API Folder](api/) and run the following command: `uvicorn main:app --reload`
2. In a separate terminal, navigate to [Streamlit UI Folder](ui/) and run the following command: `streamlit run app.py`

## In Streamlit:
There is no agent, only canned responses. In order to hit the API, there are two following prompts that you can enter:
- `healthcheck` - makes a GET request against the "/health" API endpoint
- `predict` - makes a POST request against the "/predict" API endpoint

Any other prompts will result in a random selection of 3 hardcoded responses.

## If I had more time...
- Automate the web-scraping further, to not require any human intervention.
- Utilize an algorithm like K-Nearest Neighbors to add more observations and see the impact on the Accuracy score with more observations.
- Try a different Algorithm, like XGBoost.
- Create an Agent for the Streamlit UI.
- <sub>and solve world peace...</sub>

