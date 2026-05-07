# Data
**Source:** https://en.wikipedia.org/wiki/List_of_immigration_raids_and_arrests_in_the_second_Trump_presidency

Data located under the [raw](raw/) folder is the data that was web scraped from the source Wikipedia page.

The data under the [processed](processed/) folder was updated using with the following:

## Schema Explaination of the Processed Data

### "month" Column
This Column was populated by the Web Scraping script located in src/web_scraper.py

### "event" Column
This Column was populated by the Web Scraping script located in src/web_scraper.py

### "year" Column
I manually added the values in the `year` column, cross referencing the Wikipedia page.

### "city" Column
Utilized Google Gemini in order to save time by extracting the City and State from the `event` column.

#### Prompt Used:
```
**Task:**
- Read through each cell selected in Column B
- Find and Extract the City and State mentioned
- Populate the cell in Column C with the extracted City, State
```

### "zip_code" Column
Utilized Google Gemini in order to save time by finding the appropriate Zip Code for the City, State mentioned in the `city` column

#### Prompt Used:
```
**Feedback**:
- This was perfect, thank you! Here is your next task

**Task**:
- Read the City, State in each highlighted cell in Column C
- Look up Zip Code of the City, State (using official sources)
- Enter the corresponding Zip Code in the cell in Column D
- There may be cases where only a County is extracted, not a City. Use the first Zip Code that returns for that County

Think step-by-step.
```

