<div align="center">
  <picture>
    <img alt="Life Book" src="assets/images/life-book.png" width=250>
  </picture>
</div>

  
## Profile Summary

An IT professional with extensive experience from different industries who aims to make a positive change.
Recognized for the ability to build relationships with key personnel using profound communication skills that lead and inspire the team and company.

[Link to Resume](https://drive.google.com/file/d/1nwgmD_oLFdUNI-lavPyt5yMc-PU3tIyr/view?usp=sharing)

## Skill
|  |  |
| ---      | ---       |
| Hard  | Google Sheet, Excel, MySQL, Looker Studio, Power BI, Python, JavaScript, Adobe Photoshop  |
| Soft  | Adaptive, Critical thinking, Relationship Builder, Leadership, Project Management, Attention to details  |

## Sample Works

<details>
  <summary>Subscriber Report Dashboard</summary>
  
  ### Overview
  * Dashboard Link [Looker Studio](https://lookerstudio.google.com/reporting/c085222c-25ec-4874-aa92-b92bcbaa3f00/page/GKZWD)
  * Files
    - United States List: [Google Sheets](https://docs.google.com/spreadsheets/d/1P2oIZsxwsV8IrUEutHvUlIXO7e928WH_FZWHzeLMMEo/edit#gid=1539076785) ([Source](http://download.geonames.org/export/zip/US.zip))
    - Ads Campaign: [Google Sheets](https://docs.google.com/spreadsheets/d/1fk9GCI8qUoEDceJkKiozZqUHPvUtqXsglgPUWy9Ys00/edit#gid=0)
    - Subscriber Status: [Google Sheets](https://docs.google.com/spreadsheets/d/1LK8hu4rqJrEYZoenyxN9AZSEBvD1mcgEq_ZD0u3Tp2I/edit?pli=1#gid=1288018274)
  * Scripts
    - Python: [python_to_gsheet.py](assets/scripts/python_to_gsheet.py) (web scraping)
    - Apps Script: [generateGoogleAdsLocation.gy](assets/scripts/generateGoogleAdsLocation.gs), [generateCityStateLevel.gs](assets/scripts/generateCityStateLevel.gs)
  * How It Works
    - Using scripts and formulas (please see below)
  
  <picture>
    <img alt="Subscriber Report" src="assets/images/subscriber-report.PNG" width=800>
  </picture>

  ### How It Works
  1. [Download](http://download.geonames.org/export/zip/US.zip) the United States' list of cities, states and zipcodes from geonames. Extract to [United States List](https://docs.google.com/spreadsheets/d/1P2oIZsxwsV8IrUEutHvUlIXO7e928WH_FZWHzeLMMEo/edit#gid=1539076785).
  2. We will only be working with a few records, we need to reduce the list of locations that we will be using.

     Create another sheet named [Reduce List](https://docs.google.com/spreadsheets/d/1P2oIZsxwsV8IrUEutHvUlIXO7e928WH_FZWHzeLMMEo/edit#gid=314707040) and this is where we will be using our formula.
     
     ['Reduce List!A2](https://docs.google.com/spreadsheets/d/1P2oIZsxwsV8IrUEutHvUlIXO7e928WH_FZWHzeLMMEo/edit#gid=314707040&range=A2)
     ```javascript
     =ARRAY_CONSTRAIN(
       SORT(
         FILTER('US List'!C:D, 'US List'!C:C<>"", REGEXMATCH('US List'!C:C, "[^A-Z]{2}$")),
         RANDARRAY(
           COUNTA(FILTER('US List'!C:C, 'US List'!C:C<>"", REGEXMATCH('US List'!C:C, "[^A-Z]{2}$")))
         , 1)
       , TRUE)
     , 20, 2)
     ```
      - **FILTER()** - First argument is the column range where we need to get the data from. Second and onwards are conditions that should be met.
      - **REGEXMATCH()** - Uses the expression ```"[^A-Z]{2}$"``` that excludes the data from a list that contains two letters in uppercase from its last two characters. The US List contains the following.

         We can get these areas by using the formula: ```=unique(filter(C:C, regexmatch(C:C, "[A-Z]{2}$")))``` inside the US List Sheet.
          ```
          APO AA
          APO AE
          FPO AE
          FPO AA
          APO STA
          ```
      - **RANDARRAY()** - Returns random numbers. It fills up both the row and column indicated. This is needed to randomize the sorting order of our data. The row count should be the same with the number of rows returned by the filter, hence the function ```COUNTA()``` was used.
      - **ARRAY_CONSTRAIN(input_range, num_rows, num_cols)** - Limit the number of rows and columns being returned by the ```FILTER()``` function.
          
  4. Create an [Ads Campaign](https://docs.google.com/spreadsheets/d/1fk9GCI8qUoEDceJkKiozZqUHPvUtqXsglgPUWy9Ys00/edit#gid=0) worksheet. Generate different locations from the Reduce List sheet and generate campaign names for each location.

     ['Generate Location And Campaign'!A2](https://docs.google.com/spreadsheets/d/1fk9GCI8qUoEDceJkKiozZqUHPvUtqXsglgPUWy9Ys00/edit#gid=738177274&range=A2)
     ```javascript
     =ARRAY_CONSTRAIN(
       SORT(
        FILTER(
             importrange("1P2oIZsxwsV8IrUEutHvUlIXO7e928WH_FZWHzeLMMEo", "'Reduce List'!A2:B"),
             importrange("1P2oIZsxwsV8IrUEutHvUlIXO7e928WH_FZWHzeLMMEo", "'Reduce List'!A2:A")<>""
           ), RANDARRAY(COUNTA(
                         FILTER(
                           importrange("1P2oIZsxwsV8IrUEutHvUlIXO7e928WH_FZWHzeLMMEo", "'Reduce List'!A2:A"),
                           importrange("1P2oIZsxwsV8IrUEutHvUlIXO7e928WH_FZWHzeLMMEo", "'Reduce List'!A2:A")<>""
                         )
                       )
               , 1)
       , TRUE)
     , 100,2)
     ```
     - **IMPORTRANGE()** - Use the spreadsheet ID for a shorter ```spreadsheet_url```. This pulls data from a different worksheet and access permission should be accepted.
  
      ['Generate Location And Campaign'!C2](https://docs.google.com/spreadsheets/d/1fk9GCI8qUoEDceJkKiozZqUHPvUtqXsglgPUWy9Ys00/edit#gid=738177274&range=C2)
      ```javascript
      =ARRAYFORMULA(IF(A2:A="",,"Campaign - " & iferror(1/(1/round(RANDBETWEEN(ROW(A1:A110), 100)/30)),1)))
      ```
      - **ARRAYFORMULA()** - Iterate each row. ```IF()``` conditon was used to stop an iteration.

      Since ```RANDARRAY()``` randomizes data each time changes has been made in the worksheet, we need to capture its data and paste it as a static value. We will be using the [generateGoogleAdsLocation.gy](assets/scripts/generateGoogleAdsLocation.gs) script to produce a static data.


  5. Create a [Subscriber Status](https://docs.google.com/spreadsheets/d/1LK8hu4rqJrEYZoenyxN9AZSEBvD1mcgEq_ZD0u3Tp2I/edit?pli=1#gid=1288018274) worksheet. Generate names using [python_to_gsheet.py](assets/scripts/python_to_gsheet.py) by web scraping most common names in namecensus.com and using [generateCityStateLevel.gs](assets/scripts/generateCityStateLevel.gs) script to pipulate City, State and Level for each subscriber.

  6. Connect [Subscriber Status](https://docs.google.com/spreadsheets/d/1LK8hu4rqJrEYZoenyxN9AZSEBvD1mcgEq_ZD0u3Tp2I/edit?pli=1#gid=1288018274) worksheet to [Looker Studio](https://lookerstudio.google.com/reporting/c085222c-25ec-4874-aa92-b92bcbaa3f00/page/GKZWD).
    
</details>

<details>
  <summary>Emplyoee Feedback with KPI</summary>
  
  ### Soon
</details>

<details>
  <summary>Nearby Cities Within X Miles (API)</summary>
  
  ### Soon
</details>

