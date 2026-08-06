import os


def clear_terminal():
    """
    Clears the terminal window.

    Uses the correct command for Windows or macOS/Linux.
    """
    command = "cls" if os.name == "nt" else "clear"
    os.system(command)


def display_dashboard(
    light_level,
    condition,
    minimum,
    maximum,
    average,
    sample_count,
    recommendation,
):
    """
    Displays the live Lighting Assistant dashboard.

    Args:
        light_level (int):
            Current sensor reading.

        condition (str):
            Current lighting category.

        minimum (int):
            Lowest reading from the current session.

        maximum (int):
            Highest reading from the current session.

        average (float):
            Average session reading.

        sample_count (int):
            Number of collected readings.

        recommendation (dict):
            Suggested camera settings.
    """
    clear_terminal()

    print("=" * 46)
    print("          CINEMATOGRAPHY LIGHTING ASSISTANT")
    print("=" * 46)
    print()

    print(f"{'Current reading':<20}: {light_level}")
    print(f"{'Condition':<20}: {condition}")
    print()
    print(f"{'Minimum':<20}: {minimum}")
    print(f"{'Maximum':<20}: {maximum}")
    print(f"{'Average':<20}: {average:.1f}")
    print(f"{'Samples':<20}: {sample_count}")

    print()
    print("-" * 46)
    print("Suggested starting settings")
    print("-" * 46)

    print(f"{'ISO':<20}: {recommendation['iso']}")
    print(f"{'Aperture':<20}: {recommendation['aperture']}")
    print(f"{'Shutter speed':<20}: {recommendation['shutter_speed']}")
    print(f"{'Advice':<20}: {recommendation['advice']}")

    print()
    print("Press Control+C to stop and save the graph.")