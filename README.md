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

## If I had more time/Instructor feedback
- Maybe a Binary Classification would have had higher scores lol
- Automate the web-scraping further, to not require any human intervention.
- PLOTLY MAP IN STREAMLIT:
  - https://plotly.com/python/maps/ 
  - https://python-visualization.github.io/folium/latest/getting_started.html
  - "geojson" file, use Claude to generate one
- Utilize an algorithm like K-Nearest Neighbors to add more observations and see the impact on the Accuracy score with more observations.
  - `SMOTE` for imbalanced data, look into this specifically!
    - Caveat: it is SYNTHETIC DATA that is being generated
    - Look into `sklearn` "pipeline" to add SMOTE "imbalanced learn library"

```
# Source - https://stackoverflow.com/a/72751225
# Posted by Abhishek, modified by community. See post 'Timeline' for change history
# Retrieved 2026-05-07, License - CC BY-SA 4.0

from imblearn.pipeline import Pipeline

# define pipeline
model = DecisionTreeClassifier()
over = SMOTE(sampling_strategy=0.1)
under = RandomUnderSampler(sampling_strategy=0.5)
steps = [('over', over), ('under', under), ('model', model)]
pipeline = Pipeline(steps=steps)

# evaluate pipeline
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
scores = cross_val_score(pipeline, X, Y, scoring='roc_auc', cv=cv, n_jobs=-1)
```

- False Positive/False Negatives
  - Specifically, for our usecase, we'd want to look at `recall` and `precision` and not just `accuracy`
- Try a different Algorithm, TIME-SERIES MODEL
  - Facebook Prophet(?): http://facebook.github.io/prophet/
    - Specifically, "special events": https://facebook.github.io/prophet/docs/seasonality,_holiday_effects,_and_regressors.html#modeling-holidays-and-special-events 
  - Stats forecasting model: https://nixtlaverse.nixtla.io/statsforecast/index.html
- Create an Agent for the Streamlit UI.
- Improve the overall UI
- <sub>and solve world peace...</sub>
- USE sklearn's `One Hot Encoder` INSTEAD OF Panda's `get_dummies()` FOR ONE HOT ENCODING
- My Model was very likely overfit
- sklearn has a "Column Transformer", to transform each of my columns
  - SKLEARN Pipeline in a highlevel overview:
    - `COLUMN TRANSFORM:` For example, for the `event` column: vectorize the long text data (word2vec)
    - `SCALE:` Then use Sklearn's ONE HOT ENCODING 
    - `PCA:` PCA for Dimensionality reduction AFTER 
    - Then feed this to the model :) 
    - EXAMPLE BELOW:

```
# Define which columns are numeric and which are categorical
numeric_features = ['sqft', 'bedrooms', 'bathrooms', 'income_area']
categorical_features = ['neighborhood', 'garage', 'condition']

# Create transformers for each type

# Std. Scale our numeric features
numeric_transformer = StandardScaler()

# One-hot encode cateogrical features
categorical_transformer = OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')
# handle_uknown='ignore' so it won't throw an error if it encounters a category in .transform()
# it didn't see in .fit()

print('Transformer create, robots in disguise')

# Combine transformers with ColumnTransformer
preprocessor = ColumnTransformer(
    transformers = [
        # ('alias', transformer, features_to_apply_to)
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

print('Preprocessor Created!')

X_train_tr = preprocessor.fit_transform(X_train)
X_test = preprocessor.transform(X_test)

lr = LinearRegression()

lr.fit(X_train_tr, y_train)

---
## Creating a Complete Pipeline
Now let's combine our preprocessing with a model:
---

# Create a complete pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('lr', LinearRegression())
])

print(pipeline)
```



