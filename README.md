# f1_api_calling_PROGRAM
# F1 Race Report & Driver Stats Viewer

A Python application that fetches and displays Formula 1 race reports and comprehensive driver statistics using object-oriented programming principles and the F1 Motorsport Data API.

## Team Member:

- Andres Bodington

*Note: Update this section with actual team members and their contributions*

## API Information

This application uses the **F1 Motorsport Data API** from RapidAPI with the following endpoints:

1. **`/race-report`** - Detailed race information (circuit, dates, broadcasts)
2. **`/athlete-info`** - Driver biographical and team information
3. **`/race-results`** - Season-by-season race results for drivers
4. **`/stats`** - Complete career statistics for drivers

**API Base URL:** `https://f1-motorsport-data.p.rapidapi.com`

## Features

### 🏎️ Race Reports
- View detailed F1 race reports by Event ID
- Circuit information and location
- Race dates and broadcast details

### 👤 Driver Statistics (2024 Grid)
- **Driver Information**: Bio, team, car details, birthplace
- **2024 Race Results**: Current season performance with points
- **Career Statistics**: Year-by-year championship history
- **View All Stats**: Complete driver profile in one view

### 🛠️ Technical Features
- Clean, formatted console output
- Input validation and error handling
- Object-oriented design with abstract base classes
- Multi-endpoint API integration

## Requirements

- Python 3.7+
- Required packages:
  - `requests`
  - `python-dotenv`

Install dependencies:
```bash
pip install requests python-dotenv
```

## Setup Instructions

1. Clone the repository:
```bash
git clone <your-repo-url>
cd f1-race-report-viewer
```

2. Create a `.env` file in the project root with your API key:
```
OWM_API_KEY=your_api_key_here
```

3. Get your API key:
   - Sign up at [RapidAPI](https://rapidapi.com/)
   - Subscribe to the [F1 Motorsport Data API](https://rapidapi.com/api-sports/api/f1-motorsport-data/)
   - Copy your API key and add it to the `.env` file

4. Test the API connection:
```bash
python test_api.py
```

## Usage

Run the application:
```bash
python main.py
```

### Main Menu Options:

```
============================================================
                  F1 RACE REPORT VIEWER                      
============================================================

1. View Race Report by Event ID
2. View Driver Statistics (2024 Grid)
3. Exit
============================================================
```

### Feature 1: Race Reports

Enter an Event ID to see detailed race information:

**Example Event IDs:**
- `600041133` - Bahrain GP 2024
- `600041134` - Saudi Arabian GP 2024
- `600041140` - Monaco GP 2024

See `EVENT_IDS.md` for complete list.

**Example Output:**
```
================================================================================
                             F1 RACE REPORT                                     
================================================================================

Race: STC Saudi Arabian Grand Prix
Short Name: STC Saudi Arabian GP
Season: 2024
Start Date: 2024-03-07T13:30Z
End Date: 2024-03-09T17:00Z

Circuit: Jeddah Street Circuit
Country: Saudi Arabia

Broadcasts:
  - ESPN
  - Sky Sports
  - F1 TV

================================================================================
```

### Feature 2: Driver Statistics

Select a driver from the 2024 F1 grid:

```
======================================================================
                        2024 F1 DRIVER GRID                           
======================================================================

#    Driver Name               Team                          
----------------------------------------------------------------------
1    Max Verstappen            Red Bull Racing              
2    Sergio Perez              Red Bull Racing              
3    Lewis Hamilton            Mercedes                     
4    George Russell            Mercedes                     
5    Charles Leclerc           Ferrari                      
... (20 drivers total)
======================================================================
```

After selecting a driver, choose what to view:

```
==================================================
         DRIVER STATISTICS OPTIONS                
==================================================

1. Driver Information
2. 2024 Race Results
3. Career Statistics
4. View All Stats
5. Back to Driver Selection
==================================================
```

**Example: Driver Information**
```
================================================================================
                           DRIVER INFORMATION                                   
================================================================================

Name: Max Verstappen
Date of Birth: 1997-09-30T07:00Z
Birth Place: Hasselt

Current Team Information:
  Team: Red Bull
  Number: 1
  Manufacturer: Red Bull
  Chassis: RB16B
  Engine: Honda RA621H
  Tire: Pirelli

ESPN Profile: https://www.espn.com/racing/driver/_/id/4665/max-verstappen

================================================================================
```

**Example: 2024 Race Results**
```
================================================================================
                   2024 RACE RESULTS - Max Verstappen                          
================================================================================

Date       Race                                     Pos   Start   Pts  
--------------------------------------------------------------------------------
10/27      Mexico City Grand Prix                   6     2       8    
10/20      Pirelli United States Grand Prix         3     2       23   
9/22       Singapore Airlines Singapore Grand Prix  2     2       18   
...
--------------------------------------------------------------------------------
Total Points (2024): 395
================================================================================
```

**Example: Career Statistics**
```
================================================================================
                  CAREER STATISTICS - Max Verstappen                           
================================================================================

Year   Rank   Starts   Wins   Poles   Top5    Top10   Points  
--------------------------------------------------------------------------------
2015   12     19       0      0       2       10      49      
2016   5      21       1      0       11      17      204     
2017   6      20       2      5       13      16      168     
2018   4      21       2      3       11      18      249     
2019   3      21       3      2       9       18      278     
2020   3      17       2      1       11      14      214     
2021   1      22       10     10      18      21      395.5   
2022   1      22       15     7       21      22      454     
2023   1      22       19     12      22      22      575     
2024   1      18       8      7       15      17      395     
--------------------------------------------------------------------------------
Career Totals - Wins: 62 | Poles: 47 | Points: 2981.5
================================================================================
```

## File Structure

```
project/
│
├── abc_api_base.py      # Abstract base class defining API interface
├── api_f1.py            # F1 API implementation with driver data
├── main.py              # Application entry point and user interface
├── test_api.py          # Comprehensive test script for all endpoints
├── .env                 # API key configuration (not committed to git)
├── .gitignore           # Git ignore file
├── README.md            # This file
├── QUICKSTART.md        # 5-minute setup guide
├── EVENT_IDS.md         # Event ID reference
└── DRIVER_IDS.md        # Driver ID reference
```

## Object-Oriented Design

### Abstract Base Class (APIBase)
Defines the contract that all API implementations must follow:
- `configure_api()` - Set up API credentials and base URL
- `validate_input()` - Validate user input before API calls
- `format_output()` - Format API response for display
- `fetch_data()` - Retrieve data from the API
- `make_request()` - Handle HTTP requests with error handling

### Concrete Implementation (F1API)
Implements the abstract methods for the F1 Motorsport Data API:
- Configures RapidAPI headers and multiple endpoints
- Validates Event IDs and Driver IDs
- Formats race reports, driver info, race results, and career stats
- Provides menu-driven user interface for both features
- Manages 2024 F1 driver grid data

## Testing

Run the comprehensive test script:

```bash
python test_api.py
```

This tests all four endpoints:
1. Race Report (Event ID: 600041134)
2. Driver Information (Max Verstappen: 4665)
3. Race Results (Max Verstappen 2024)
4. Career Statistics (Max Verstappen)

**Expected Output:**
```
============================================================
              F1 API COMPREHENSIVE TEST SCRIPT              
============================================================

🔧 Initializing F1 API...
✅ API initialized successfully

[Tests run...]

============================================================
                      TEST SUMMARY                          
============================================================
Race Report                    ✅ PASSED
Driver Information             ✅ PASSED
Race Results                   ✅ PASSED
Career Statistics              ✅ PASSED
============================================================

🎉 ALL TESTS PASSED! 🎉
```

## Error Handling

The application includes comprehensive error handling for:
- Missing or invalid API keys
- Network connection issues
- Invalid Event ID or Driver ID input
- HTTP errors (401, 403, 404, 429, 500, 503)
- JSON parsing errors
- API timeout issues

## Future Enhancements

Potential features to add:
- Constructor (team) standings by year
- Head-to-head driver comparisons
- Race-by-race season analysis
- Historical data visualization
- Export data to CSV or JSON files
- Real-time race results during race weekends
- Driver photo gallery integration

## Reference Documents

- **QUICKSTART.md** - Get started in 5 minutes
- **EVENT_IDS.md** - Complete list of race Event IDs
- **DRIVER_IDS.md** - Complete list of Driver IDs and usage guide

## API Request Examples

### Race Report
```
GET /race-report?eventId=600041134
Headers:
  x-rapidapi-host: f1-motorsport-data.p.rapidapi.com
  x-rapidapi-key: your_key_here
```

### Driver Information
```
GET /athlete-info?athleteId=4665
Headers:
  x-rapidapi-host: f1-motorsport-data.p.rapidapi.com
  x-rapidapi-key: your_key_here
```

### Race Results
```
GET /race-results?driverId=4665&year=2024
Headers:
  x-rapidapi-host: f1-motorsport-data.p.rapidapi.com
  x-rapidapi-key: your_key_here
```

### Career Statistics
```
GET /stats?driverId=4665
Headers:
  x-rapidapi-host: f1-motorsport-data.p.rapidapi.com
  x-rapidapi-key: your_key_here
```

## Troubleshooting

### "API key not found" error
- Make sure you have a `.env` file in the project root
- Verify the variable name is `OWM_API_KEY`
- Check that there are no extra spaces or quotes around the key

### "401 Unauthorized" error
- Your API key may be invalid or expired
- Check your RapidAPI subscription status
- Verify you've subscribed to the F1 Motorsport Data API

### "No data received" error
- Check your internet connection
- Verify the Event ID or Driver ID is correct
- Try a different ID from the reference documents
- The API may be experiencing issues

### Test script fails
- Run `python test_api.py` to diagnose which endpoint is failing
- Check the error messages for specific issues
- Verify your `.env` file is configured correctly

## License

This project is for educational purposes as part of an Object-Oriented Programming course assignment.

## Acknowledgments

- F1 Motorsport Data API provided by [API-SPORTS](https://api-sports.io/)
- Data sourced from ESPN F1
- 2024 F1 driver data from official Formula 1 sources
