# Spreadsheet Cleanup & Dashboard 

This tool automates:
- Removing duplicates
- Standardizing columns
- Generating simple dashboards

## Tech Used
- Python
- Pandas
- Matplotlib / Plotly
- openpyxl

## Sample Input
| Name | Sales | Sales  | Month  |
|------|-------|--------|--------|
| John | 2000  | NULL   | Jan    |
| John |       | 2000   | Jan    |
| Mary | 3000  | NULL   | Feb    |

## Output:
- Cleaned table with merged columns
- Monthly totals
- Sales trend graph

## Files:
- `cleanup.py`: the data cleaning script
- `data.xlsx`: messy input example (optional)
