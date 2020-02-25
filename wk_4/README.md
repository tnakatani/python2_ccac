# wk_4 Assignment

Write python code that conforms to the following specs:

## Purpose
> Implement search criteria defined in the JSON format for searching for capital projects in PGH dataset, outputting resulting projects into a file in JSON format

## JSON-encoded search criteria:

Use the following JSON search criteria for your query.  The `specifications.json` file can be found in the [`./scripts/specification`](https://github.com/tnakatani/python2_ccac/tree/master/wk_4/scripts/specifications) directory
```JSON
{"status": ["Completed"], "neighborhood":["Shadyside", "BROOKLINE", "carrick"], "fiscal_year": [2017,"2018"], "area": ["Facility Improvement"]}
```

### Search Notes:
- For dates: We will throw out malformed dates that are not YYYY-MM-DD~~ (This requirement was removed due to lack of connecetion to the primary data set)
- A blank value in any specified query for a column/field will disqualify that record from inclusion in the results
- Empty string: do not limit results by this criteria at all
- Note: the "planning_status" key in the search JSON corresponds to the field named "status" in the csv

### Program Requirement 1: Searching
Write code that can read in a search criterion JSON file of your specification. You'll need to be prepared to share this specification with others in the class

Allow the user to specify search criteria for project fiscal year, start date, area, asset_type, and planning status
