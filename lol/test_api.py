"""
Demo script to showcase all features of the F1 Race Report & Driver Stats Viewer.
This script automatically demonstrates key features without user input.
"""

from api_f1 import F1API
import time


def print_section_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70)


def demo_race_report(f1_api):
    """Demonstrate the race report feature."""
    print_section_header("DEMO: RACE REPORT FEATURE")

    races_to_demo = [
        ("600041134", "Saudi Arabian GP 2024"),
        ("600041140", "Monaco GP 2024"),
    ]

    for event_id, race_name in races_to_demo:
        print(f"\n Fetching: {race_name} (Event ID: {event_id})")
        time.sleep(1)

        try:
            data = f1_api.fetch_data(
                endpoint_type='race-report', eventId=event_id)
            if data:
                formatted = f1_api.format_output(data)
                print("\n" + formatted)
                input("\nPress Enter to continue...")
            else:
                print(f" Could not fetch data for {race_name}")
        except Exception as e:
            print(f" Error: {e}")


def demo_driver_info(f1_api):
    """Demonstrate the driver information feature."""
    print_section_header("DEMO: DRIVER INFORMATION FEATURE")

    drivers_to_demo = [
        ("4665", "Max Verstappen", "Red Bull Racing"),
        ("4444", "Lewis Hamilton", "Mercedes"),
    ]

    for driver_id, driver_name, team in drivers_to_demo:
        print(f"\n Fetching information for: {driver_name} ({team})")
        time.sleep(1)

        try:
            data = f1_api.fetch_data(
                endpoint_type='athlete-info', athleteId=driver_id)
            if data:
                formatted = f1_api.format_athlete_info(data)
                print("\n" + formatted)
                input("\nPress Enter to continue...")
            else:
                print(f" Could not fetch data for {driver_name}")
        except Exception as e:
            print(f" Error: {e}")


def demo_race_results(f1_api):
    """Demonstrate the 2024 race results feature."""
    print_section_header("DEMO: 2024 RACE RESULTS FEATURE")

    drivers_to_demo = [
        ("4665", "Max Verstappen"),
        ("4763", "Lando Norris"),
    ]

    for driver_id, driver_name in drivers_to_demo:
        print(f"\n Fetching 2024 race results for: {driver_name}")
        time.sleep(1)

        try:
            data = f1_api.fetch_data(
                endpoint_type='race-results', driverId=driver_id, year='2024')
            if data:
                formatted = f1_api.format_race_results(data, driver_name)
                print("\n" + formatted)
                input("\nPress Enter to continue...")
            else:
                print(f" Could not fetch data for {driver_name}")
        except Exception as e:
            print(f" Error: {e}")


def demo_career_stats(f1_api):
    """Demonstrate the career statistics feature."""
    print_section_header("DEMO: CAREER STATISTICS FEATURE")

    drivers_to_demo = [
        ("4665", "Max Verstappen"),
        ("20", "Fernando Alonso"),
    ]

    for driver_id, driver_name in drivers_to_demo:
        print(f"\n Fetching career statistics for: {driver_name}")
        time.sleep(1)

        try:
            data = f1_api.fetch_data(endpoint_type='stats', driverId=driver_id)
            if data:
                formatted = f1_api.format_career_stats(data, driver_name)
                print("\n" + formatted)
                input("\nPress Enter to continue...")
            else:
                print(f" Could not fetch data for {driver_name}")
        except Exception as e:
            print(f" Error: {e}")


def demo_driver_grid(f1_api):
    """Demonstrate the 2024 driver grid display."""
    print_section_header("DEMO: 2024 F1 DRIVER GRID")

    print("\n Displaying all 20 drivers from the 2024 season:")
    time.sleep(1)

    f1_api.display_driver_menu()

    print("\n In the main application, you can select any driver to view their stats!")
    input("\nPress Enter to continue...")


def main():
    """Run the complete feature demonstration."""
    print("\n" + "=" * 70)
    print("F1 RACE REPORT & DRIVER STATS VIEWER".center(70))
    print("FEATURE DEMONSTRATION".center(70))
    print("=" * 70)

    print("\nThis demo will showcase all major features of the application.")
    print("The demo will automatically fetch and display data from the API.")
    print("\n  Note: This requires a valid API key in your .env file.")

    input("\nPress Enter to start the demo...")

    try:
        # Initialize API
        print("\n Initializing F1 API...")
        f1_api = F1API()
        print(" API initialized successfully!")
        time.sleep(1)

        # Show menu structure
        print_section_header("APPLICATION MENU STRUCTURE")
        print("\nThe main application has the following options:")
        f1_api.display_menu()
        input("\nPress Enter to continue...")

        # Demo each feature
        demo_race_report(f1_api)
        demo_driver_grid(f1_api)
        demo_driver_info(f1_api)
        demo_race_results(f1_api)
        demo_career_stats(f1_api)

        # Summary
        print_section_header("DEMO COMPLETE!")
        print("\n✅ All features demonstrated successfully!")
        print("\nFeatures showcased:")
        print("  1. ✅ Race Report by Event ID")
        print("  2. ✅ 2024 F1 Driver Grid Display")
        print("  3. ✅ Driver Information (Bio & Team)")
        print("  4. ✅ 2024 Race Results")
        print("  5. ✅ Career Statistics")

        print("\n" + "=" * 70)
        print("Ready to use the full application!".center(70))
        print("=" * 70)
        print("\nRun 'python main.py' to use the interactive application.")
        print("You'll be able to:")
        print("  - Select any race from 2024 to view details")
        print("  - Choose from 20 F1 drivers")
        print("  - View comprehensive statistics")
        print("  - Compare different drivers")
        print("\nHappy racing!")

    except ValueError as e:
        print(f"\n Configuration Error: {e}")
        print("\nMake sure you have:")
        print("  1. Created a .env file")
        print("  2. Added your API key: OWM_API_KEY=your_key_here")

    except Exception as e:
        print(f"\n Unexpected Error: {e}")
        print("\nPlease check:")
        print("  - Your internet connection")
        print("  - Your API key is valid")
        print("  - You're not rate limited")
        import traceback
        print("\nFull traceback:")
        traceback.print_exc()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Demo interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n Demo error: {e}")
