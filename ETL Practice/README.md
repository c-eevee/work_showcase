# ETL Practice — Sales Data Cleaning

A hands-on ETL (Extract, Transform, Load) project where I took an intentionally messy sales dataset and cleaned it into a Tableau-ready file using Python and pandas.

---

## Files

| File | Description |
|------|-------------|
| `sales_dirty_data.xlsx` | Raw dataset with duplicates, inconsistent formatting, wrong data types, and missing values |
| `sales_data.py` | Python cleaning script |
| `sales_cleaned.xlsx` | Final cleaned output, ready for analysis or visualization |

---

## Tools Used

- **Python** (pandas, numpy, openpyxl)
- **Excel** (source and output format)

---

## Cleaning Challenges & Approach

### Challenge A — Remove Duplicates
The raw dataset had 215 rows with 15 duplicate entries. Used `drop_duplicates()` to bring it down to 200 clean rows.

### Challenge B — Standardize Region & Country
Columns had inconsistent variants like `"north america"`, `"N. America"`, `"EUROPE"`, `"U.S.A"`, `"ger"`, `"sgp"`.

**Two-step approach:**
1. Used regex to strip special characters, then lowercased and stripped whitespace to normalize all values as much as possible before mapping
2. Applied `np.where()` for Region (keyword matching on `"eur"`, `"america"`, `"asia"`) and a dictionary map for Country to handle the high number of variations cleanly

### Challenge C — Fix Data Types
Some `Revenue` and `Units_Sold` values were stored as strings. Converted `Revenue` to float and `Units_Sold` to numeric so they could be aggregated correctly.

### Challenge D — Handle Missing Values
Identified nulls across `Salesperson`, `Customer_Segment`, `Payment_Method`, and `Country`. Filled all missing values with `"Not Available"` to preserve row count while flagging incomplete records.

---

## Output

The cleaned file `sales_cleaned.xlsx` is fully Tableau-ready — consistent categories, correct data types, and no nulls.

---

## Key Takeaway

The regex normalization step before dictionary mapping was the most important design decision — it dramatically reduced the number of edge cases that needed to be handled manually.
