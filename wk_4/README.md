# wk_4 Assignment

| Directory  | Description  |
|:--|:--|
| [`data`](https://github.com/tnakatani/python2_ccac/tree/master/wk_4/data)  | Location of capital projects dataset  |
| [`scripts`](https://github.com/tnakatani/python2_ccac/tree/master/wk_4/scripts)  | wk_4 assignment written in Python  |
| [`pandas`](https://github.com/tnakatani/python2_ccac/tree/master/wk_4/pandas)  | wk_4 assignment written with Pandas  |

---

Write python code that conforms to the following specs:

## Purpose

> Implement search criteria defined in the JSON format for searching for capital projects in PGH dataset, outputting resulting projects into a file in JSON format

## Program Requirement 1: Searching
>  Write code that can read in a search criterion JSON file of your specification. You'll need to be prepared to share this specification with others in the class

> Allow the user to specify search criteria for project fiscal year, start date, area, asset_type, and planning status

## JSON-encoded search criteria:

Use the following JSON search criteria for your query.  The `specifications.json` file can be found in the [`./specification`](https://github.com/tnakatani/python2_ccac/tree/master/wk_4/scripts/specifications) directory:

Instructions:
- Each field can take multiple items
- `fiscal_year` key accepts either integers or strings
- `area` key requires an exact match string.  It can't do fuzzy matching at the moment.
- An empty string won't limit results by this criteria
- Remember to use double-quotes for JSON files

```JSON
{
   "status":[
      "Completed"
   ],
   "neighborhood":[
      "Shadyside",
      "BROOKLINE",
      "carrick"
   ],
   "fiscal_year":[
      2017,
      "2018"
   ],
   "area":[
      "Facility Improvement"
   ]
}
```


