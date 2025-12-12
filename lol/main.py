from api_f1 import F1API


def handle_race_report(f1_api):
    """Handle race report viewing."""
    print("\nExample Event IDs:")
    print("  - 600041134 (Saudi Arabian GP 2024)")
    print("  - 600041133 (Bahrain GP 2024)")
    print("  - 600041135 (Australian GP 2024)")

    event_id = f1_api.get_event_id_input()

    if not f1_api.validate_input(eventId=event_id):
        return

    try:
        print(f"\n Fetching race report for Event ID: {event_id}...")
        data = f1_api.fetch_data(endpoint_type='race-report', eventId=event_id)

        if data:
            formatted_output = f1_api.format_output(data)
            print("\n" + formatted_output)
        else:
            print("\n Failed to fetch data. Please check the Event ID and try again.")

    except Exception as e:
        print(f"\n Error: {e}")
        print("Please try again.")


def handle_driver_stats(f1_api):
    """Handle driver statistics viewing."""
    while True:
        f1_api.display_driver_menu()

        driver = f1_api.get_driver_choice()
        if driver is None:
            return  # User chose to go back

        driver_name = driver['name']
        driver_id = driver['id']

        print(f"\n Selected: {driver_name} ({driver['team']})")

        # Inner loop for stats options
        while True:
            stats_choice = f1_api.get_driver_stats_choice()

            if stats_choice == '5':
                break  # Back to driver selection

            try:
                if stats_choice == '1':
                    # Driver Information
                    print(f"\n Fetching information for {driver_name}...")
                    data = f1_api.fetch_data(
                        endpoint_type='athlete-info', athleteId=driver_id)
                    if data:
                        print("\n" + f1_api.format_athlete_info(data))
                    else:
                        print("\n Failed to fetch driver information.")

                elif stats_choice == '2':
                    # 2024 Race Results
                    print(
                        f"\n Fetching 2024 race results for {driver_name}...")
                    data = f1_api.fetch_data(
                        endpoint_type='race-results', driverId=driver_id, year='2024')
                    if data:
                        print("\n" + f1_api.format_race_results(data, driver_name))
                    else:
                        print("\n Failed to fetch race results.")

                elif stats_choice == '3':
                    # Career Statistics
                    print(
                        f"\n Fetching career statistics for {driver_name}...")
                    data = f1_api.fetch_data(
                        endpoint_type='stats', driverId=driver_id)
                    if data:
                        print("\n" + f1_api.format_career_stats(data, driver_name))
                    else:
                        print("\n Failed to fetch career statistics.")

                elif stats_choice == '4':
                    # View All Stats
                    print(f"\n Fetching all statistics for {driver_name}...")

                    # Fetch all three types of data
                    print("\n Loading driver information...")
                    info_data = f1_api.fetch_data(
                        endpoint_type='athlete-info', athleteId=driver_id)

                    print(" Loading 2024 race results...")
                    results_data = f1_api.fetch_data(
                        endpoint_type='race-results', driverId=driver_id, year='2024')

                    print(" Loading career statistics...")
                    stats_data = f1_api.fetch_data(
                        endpoint_type='stats', driverId=driver_id)

                    # Display all data
                    if info_data:
                        print("\n" + f1_api.format_athlete_info(info_data))
                    if results_data:
                        print(
                            "\n" + f1_api.format_race_results(results_data, driver_name))
                    if stats_data:
                        print(
                            "\n" + f1_api.format_career_stats(stats_data, driver_name))

                    if not (info_data or results_data or stats_data):
                        print("\n Failed to fetch driver statistics.")

                # Ask if user wants to continue with this driver
                continue_choice = input(
                    "\nPress Enter to view more stats or 'b' to select another driver: ").strip().lower()
                if continue_choice == 'b':
                    break

            except Exception as e:
                print(f"\n Error: {e}")
                print("Please try again.")


def main():
    """
    Main application entry point.
    Handles user interaction and API calls.
    """
    try:
        f1_api = F1API()
    except ValueError as e:
        print(f"\n{e}")
        return

    print("\n  Welcome to the F1 Race Report & Driver Stats Viewer! 🏁")

    while True:
        f1_api.display_menu()
        choice = f1_api.get_user_choice()

        if choice == '1':
            # Race Report
            handle_race_report(f1_api)

            continue_choice = input(
                "\nPress Enter to continue or 'q' to quit: ").strip().lower()
            if continue_choice == 'q':
                break

        elif choice == '2':
            # Driver Statistics
            handle_driver_stats(f1_api)

            continue_choice = input(
                "\nPress Enter to return to main menu or 'q' to quit: ").strip().lower()
            if continue_choice == 'q':
                break

        elif choice == '3':
            print("\n Thank you for using F1 Race Report & Driver Stats Viewer!")
            print("See you at the next race! 🏎️💨\n")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Application exited by user. Goodbye!")
    except Exception as e:
        print(f"\n An unexpected error occurred: {e}")
