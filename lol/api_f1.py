import os
import requests
import json
from abc_api_base import APIBase
import dotenv
dotenv.load_dotenv()


class F1API(APIBase):
    """
    F1 Motorsport Data API implementation.
    Fetches Formula 1 race reports and driver statistics.
    """

    # 2024 F1 Grid - Driver ID mapping
    DRIVERS_2024 = {
        "1": {"name": "Max Verstappen", "id": "4665", "team": "Red Bull Racing"},
        "2": {"name": "Sergio Perez", "id": "4662", "team": "Red Bull Racing"},
        "3": {"name": "Lewis Hamilton", "id": "4444", "team": "Mercedes"},
        "4": {"name": "George Russell", "id": "4722", "team": "Mercedes"},
        "5": {"name": "Charles Leclerc", "id": "4725", "team": "Ferrari"},
        "6": {"name": "Carlos Sainz", "id": "4728", "team": "Ferrari"},
        "7": {"name": "Lando Norris", "id": "4763", "team": "McLaren"},
        "8": {"name": "Oscar Piastri", "id": "5038", "team": "McLaren"},
        "9": {"name": "Fernando Alonso", "id": "20", "team": "Aston Martin"},
        "10": {"name": "Lance Stroll", "id": "4893", "team": "Aston Martin"},
        "11": {"name": "Pierre Gasly", "id": "4757", "team": "Alpine"},
        "12": {"name": "Esteban Ocon", "id": "4755", "team": "Alpine"},
        "13": {"name": "Alexander Albon", "id": "4761", "team": "Williams"},
        "14": {"name": "Logan Sargeant", "id": "5031", "team": "Williams"},
        "15": {"name": "Valtteri Bottas", "id": "4655", "team": "Alfa Romeo"},
        "16": {"name": "Zhou Guanyu", "id": "4979", "team": "Alfa Romeo"},
        "17": {"name": "Kevin Magnussen", "id": "4464", "team": "Haas"},
        "18": {"name": "Nico Hulkenberg", "id": "4467", "team": "Haas"},
        "19": {"name": "Yuki Tsunoda", "id": "4896", "team": "AlphaTauri"},
        "20": {"name": "Daniel Ricciardo", "id": "4524", "team": "AlphaTauri"}
    }

    def __init__(self):
        """Initialize F1 API with base URL and headers."""
        super().__init__()
        self.configure_api()

    def configure_api(self):
        """Configure F1 API settings."""
        self.api_key = "12f7ba7e0bmsha880fa500da986fp1423afjsn8b48944f0c3e"
        self.base_url = "https://f1-motorsport-data.p.rapidapi.com"
        self.headers = {
            "x-rapidapi-host": "f1-motorsport-data.p.rapidapi.com",
            "x-rapidapi-key": self.api_key
        }
        if not self.api_key:
            raise ValueError(
                "Error: F1 Motorsport Data API key not found. Please set OWM_API_KEY in your .env file.")

    def validate_input(self, **kwargs):
        """
        Validate user input before making API call.

        Args:
            **kwargs: Should contain 'eventId' or 'driverId' parameter

        Returns:
            bool: True if valid, False otherwise
        """
        # Validate Event ID for race reports
        event_id = kwargs.get('eventId')
        if event_id is not None:
            if event_id == "":
                print("Error: Event ID is required.")
                return False
            if not str(event_id).isdigit():
                print("Invalid input. Event ID should be numeric.")
                return False
            return True

        # Validate Driver ID for driver stats
        driver_id = kwargs.get('driverId')
        if driver_id is not None:
            if driver_id == "":
                print("Error: Driver ID is required.")
                return False
            if not str(driver_id).isdigit():
                print("Invalid input. Driver ID should be numeric.")
                return False
            return True

        return False

    def fetch_data(self, **kwargs):
        """
        Fetch data from the API based on endpoint type.

        Args:
            **kwargs: Should contain endpoint-specific parameters

        Returns:
            dict: Parsed JSON response from the API
        """
        endpoint_type = kwargs.get('endpoint_type', 'race-report')

        if endpoint_type == 'race-report':
            event_id = kwargs.get('eventId')
            endpoint = "/race-report"
            params = {"eventId": event_id}
        elif endpoint_type == 'athlete-info':
            athlete_id = kwargs.get('athleteId')
            endpoint = "/athlete-info"
            params = {"athleteId": athlete_id}
        elif endpoint_type == 'race-results':
            driver_id = kwargs.get('driverId')
            year = kwargs.get('year', '2024')
            endpoint = "/race-results"
            params = {"driverId": driver_id, "year": year}
        elif endpoint_type == 'stats':
            driver_id = kwargs.get('driverId')
            endpoint = "/stats"
            params = {"driverId": driver_id}
        else:
            return None

        return self.make_request(endpoint=endpoint, params=params)

    def format_output(self, data):
        """
        Format F1 race report data for console display.

        Args:
            data: Raw JSON data from the API

        Returns:
            str: Formatted string for console output
        """
        if not data:
            return "No data available."

        output = []
        output.append("=" * 80)
        output.append("F1 RACE REPORT".center(80))
        output.append("=" * 80)
        output.append("")

        if isinstance(data, dict) and 'report' in data:
            report = data['report']

            if 'racestrip' in report:
                racestrip = report['racestrip']

                race_name = racestrip.get('name', 'Unknown Race')
                short_name = racestrip.get('shortName', 'Unknown')
                season = racestrip.get('season', 'Unknown')
                start_date = racestrip.get('date', 'TBA')
                end_date = racestrip.get('endDate', 'TBA')

                output.append(f"Race: {race_name}")
                output.append(f"Short Name: {short_name}")
                output.append(f"Season: {season}")
                output.append(f"Start Date: {start_date}")
                output.append(f"End Date: {end_date}")
                output.append("")

                if 'circuit' in racestrip:
                    circuit = racestrip['circuit']
                    circuit_name = circuit.get('name', 'Unknown Circuit')
                    output.append(f"Circuit: {circuit_name}")

                    if 'countryFlag' in circuit:
                        country = circuit['countryFlag'].get(
                            'alt', 'Unknown Country')
                        output.append(f"Country: {country}")

                    output.append("")

                if 'broadcasts' in racestrip and racestrip['broadcasts']:
                    output.append("Broadcasts:")
                    for broadcast in racestrip['broadcasts'][:3]:
                        if isinstance(broadcast, dict):
                            network = broadcast.get(
                                'network', 'Unknown Network')
                            output.append(f"  - {network}")
                    output.append("")

            output.append("=" * 80)
        else:
            return "Unexpected data format received from API."

        return "\n".join(output)

    def format_athlete_info(self, data):
        """Format driver information for display."""
        if not data:
            return "No driver information available."

        output = []
        output.append("=" * 80)
        output.append("DRIVER INFORMATION".center(80))
        output.append("=" * 80)
        output.append("")

        full_name = data.get('fullName', 'Unknown Driver')
        dob = data.get('dateOfBirth', 'Unknown')
        birth_place = data.get('birthPlace', {})
        city = birth_place.get('city', 'Unknown') if birth_place else 'Unknown'

        output.append(f"Name: {full_name}")
        output.append(f"Date of Birth: {dob}")
        output.append(f"Birth Place: {city}")
        output.append("")

        # Vehicle/Team info
        if 'vehicles' in data and data['vehicles']:
            vehicle = data['vehicles'][0]
            output.append("Current Team Information:")
            output.append(f"  Team: {vehicle.get('team', 'Unknown')}")
            output.append(f"  Number: {vehicle.get('number', 'N/A')}")
            output.append(
                f"  Manufacturer: {vehicle.get('manufacturer', 'Unknown')}")
            output.append(f"  Chassis: {vehicle.get('chassis', 'Unknown')}")
            output.append(f"  Engine: {vehicle.get('engine', 'Unknown')}")
            output.append(f"  Tire: {vehicle.get('tire', 'Unknown')}")
            output.append("")

        # Link
        link = data.get('link', '')
        if link:
            output.append(f"ESPN Profile: {link}")
            output.append("")

        output.append("=" * 80)
        return "\n".join(output)

    def format_race_results(self, data, driver_name="Driver"):
        """Format race results for display."""
        if not data:
            return "No race results available."

        output = []
        output.append("=" * 80)
        output.append(f"2024 RACE RESULTS - {driver_name}".center(80))
        output.append("=" * 80)
        output.append("")
        output.append(
            f"{'Date':<10} {'Race':<40} {'Pos':<5} {'Start':<7} {'Pts':<5}")
        output.append("-" * 80)

        total_points = 0
        for race in data:
            date = race.get('date', 'N/A')
            race_name = race.get('race', 'Unknown Race')
            place = race.get('place', 'N/A')
            start = race.get('start', 'N/A')
            points = race.get('points', 0)
            total_points += points

            # Truncate race name if too long
            if len(race_name) > 38:
                race_name = race_name[:35] + "..."

            output.append(
                f"{date:<10} {race_name:<40} {place:<5} {start:<7} {points:<5}")

        output.append("-" * 80)
        output.append(f"Total Points (2024): {total_points}")
        output.append("=" * 80)
        return "\n".join(output)

    def format_career_stats(self, data, driver_name="Driver"):
        """Format career statistics for display."""
        if not data:
            return "No career statistics available."

        output = []
        output.append("=" * 80)
        output.append(f"CAREER STATISTICS - {driver_name}".center(80))
        output.append("=" * 80)
        output.append("")
        output.append(
            f"{'Year':<6} {'Rank':<6} {'Starts':<8} {'Wins':<6} {'Poles':<7} {'Top5':<7} {'Top10':<7} {'Points':<8}")
        output.append("-" * 80)

        total_wins = 0
        total_poles = 0
        total_points = 0

        for season in data:
            year = season.get('year', 'N/A')
            rank = season.get('rank', 'N/A')
            starts = season.get('starts', 0)
            wins = season.get('wins', 0)
            poles = season.get('poles', 0)
            top5 = season.get('top5', 0)
            top10 = season.get('top10', 0)
            points = season.get('points', 0)

            total_wins += wins
            total_poles += poles
            total_points += points

            output.append(
                f"{year:<6} {rank:<6} {starts:<8} {wins:<6} {poles:<7} {top5:<7} {top10:<7} {points:<8}")

        output.append("-" * 80)
        output.append(
            f"Career Totals - Wins: {total_wins} | Poles: {total_poles} | Points: {total_points}")
        output.append("=" * 80)
        return "\n".join(output)

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "=" * 60)
        print("F1 RACE REPORT VIEWER".center(60))
        print("=" * 60)
        print("\n1. View Race Report by Event ID")
        print("2. View Driver Statistics (2024 Grid)")
        print("3. Exit")
        print("=" * 60)

    def display_driver_menu(self):
        """Display the 2024 F1 driver selection menu."""
        print("\n" + "=" * 70)
        print("2024 F1 DRIVER GRID".center(70))
        print("=" * 70)
        print(f"\n{'#':<4} {'Driver Name':<25} {'Team':<30}")
        print("-" * 70)

        for choice, driver_info in self.DRIVERS_2024.items():
            print(
                f"{choice:<4} {driver_info['name']:<25} {driver_info['team']:<30}")

        print("=" * 70)

    def get_user_choice(self):
        """Get user's menu choice."""
        print("\nPlease select an option:")
        user_choice = input("\nEnter your choice (1-3): ").strip()
        while user_choice not in ['1', '2', '3']:
            print("Invalid choice. Please enter 1, 2, or 3.")
            user_choice = input("\nEnter your choice (1-3): ").strip()
        return user_choice

    def get_driver_choice(self):
        """Get user's driver selection."""
        while True:
            choice = input(
                "\nEnter driver number (1-20) or 'b' to go back: ").strip()
            if choice.lower() == 'b':
                return None
            if choice in self.DRIVERS_2024:
                return self.DRIVERS_2024[choice]
            else:
                print("Invalid choice. Please enter a number between 1 and 20.")

    def get_event_id_input(self):
        """Get event ID input from user."""
        while True:
            event_id = input("\nEnter the Event ID: ").strip()
            if event_id.isdigit():
                return event_id
            else:
                print("Invalid input. Please enter a numeric Event ID.")

    def get_driver_stats_choice(self):
        """Get user's choice for which stats to view."""
        print("\n" + "=" * 50)
        print("DRIVER STATISTICS OPTIONS".center(50))
        print("=" * 50)
        print("\n1. Driver Information")
        print("2. 2024 Race Results")
        print("3. Career Statistics")
        print("4. View All Stats")
        print("5. Back to Driver Selection")
        print("=" * 50)

        choice = input("\nEnter your choice (1-5): ").strip()
        while choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please enter 1-5.")
            choice = input("\nEnter your choice (1-5): ").strip()
        return choice
