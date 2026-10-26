# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

General Assembly "Applied AI and Deep Learning" capstone ("P.R.E.D.I.C.T.I.C.E"). A scikit-learn `RandomForestClassifier` predicts the **state** of the next immigration raid from the previous raid's state and the month, served through FastAPI and consumed by a Streamlit chat UI.

There is no test suite, linter config, or build step. Dependencies are pinned in `requirements.txt` (`pip install -r requirements.txt`).

## Running

Both services must be started from inside their own directories, because they use cwd-relative paths:

```bash
cd api && uvicorn main:app --reload     # backend on http://127.0.0.1:8000
cd ui && streamlit run app.py           # frontend on :8501
```

- `ui/app.py` imports `from demo import SAMPLE_REQUEST` and loads `avatar/iron_mask.png`, so it only works with `ui/` as cwd.
- The UI hardcodes `BASE_URL = "http://127.0.0.1:8000"`.
- The root-level `main.py` is a leftover hello-world FastAPI stub, not the real API.

The Streamlit UI has no agent or LLM. The prompt `healthcheck` calls `GET /health`, `predict` calls `POST /predict` with the fixed payload in `ui/demo.py`, and anything else returns a random canned reply in the "Iron Oracle" persona.

## Data → model → API pipeline

1. **Scrape**: `src/web_scraper.py` is a top-level script (no functions or `main` guard) that scrapes a Wikipedia list of raids and writes `../data/raw/trackingice.csv`, so run it from `src/`. It assigns each paragraph a month by substring matching. Paragraphs with no month are printed for manual review.
2. **Enrich (manual)**: `data/processed/tracking_ice_processed.csv` adds `day_with_month`, `city`, `zip_code`, and `year`. These were filled by hand and with Gemini, not by code (see `data/README.md`). `trackingice_processed.csv` is an earlier version with no `day_with_month`. Re-running the scraper does **not** regenerate the processed data.
3. **Train**: there are two notebooks, and both read `../data/processed/tracking_ice_processed.csv`.
   - `model_training.ipynb` is the abandoned first attempt, which predicted `zip_code` (about 5% accuracy).
   - `model_target_variable_pivot.ipynb` produces the shipped model. It pulls `state` out of `city`, builds `previous_state` with `shift(1)`, and one-hot encodes it with `pd.get_dummies(prefix="is")` as `is_<State>` columns, plus `is_<Month>` columns. It then saves `../model/icepredictor.joblib`.
4. **Serve**: `api/main.py` loads the joblib model in the FastAPI `lifespan` from `model/icepredictor.joblib`, resolved relative to the file. `/predict` returns `prediction_label` and per-class `probabilities`.

## Feature-schema coupling (important)

The feature column names come from `get_dummies` output on the training data, and they are repeated by hand in three places that must stay in sync:

- the model's `feature_names_in_` (set by the notebook)
- `PredictionRequest` in `api/main.py`
- `SAMPLE_REQUEST` in `ui/demo.py`

Some column names aren't valid Python identifiers (`is_D.C.`, `is_New York`, …). The Pydantic model handles these with `Field(alias=...)` plus `populate_by_name=True`. `predict()` then dumps `by_alias=True` and reorders columns to `model.feature_names_in_`. If you retrain with different states or months, update all three places, or `/predict` will raise a 500 KeyError. The state dummies only cover states that appear as a `previous_state` in the data, so the feature set isn't all 50 states.
