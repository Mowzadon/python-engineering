from pathlib import Path

import matplotlib.pyplot as plt


PROJECT_FOLDER = Path(__file__).resolve().parent.parent
GRAPHS_FOLDER = PROJECT_FOLDER / "graphs"
GRAPH_FILE = GRAPHS_FOLDER / "light_session.png"


def plot_session(readings):
    """
    Creates and saves a line graph of the current light-measurement session.

    Args:
        readings (list):
            Light-level measurements collected during the current run.
    """
    if not readings:
        print("No readings available to graph.")
        return

    GRAPHS_FOLDER.mkdir(exist_ok=True)

    sample_numbers = range(1, len(readings) + 1)

    plt.figure(figsize=(10, 5))
    plt.plot(sample_numbers, readings)

    plt.title("Lighting Assistant Session")
    plt.xlabel("Sample Number")
    plt.ylabel("Light Level")
    plt.ylim(0, 1023)
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(GRAPH_FILE)
    plt.show()
    plt.close()

    print(f"Graph saved to: {GRAPH_FILE}")