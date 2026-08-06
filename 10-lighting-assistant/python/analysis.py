def calculate_statistics(readings):
    """
    Calculates summary statistics for collected light readings.

    Args:
        readings (list):
            Light-level measurements stored as integers.

    Returns:
        tuple:
            A tuple containing:
                - minimum reading
                - maximum reading
                - average reading
                - number of samples
    """
    minimum = min(readings)
    maximum = max(readings)
    average = sum(readings) / len(readings)
    sample_count = len(readings)

    return minimum, maximum, average, sample_count


def recommend_camera_settings(condition):
    """
    Provides educational starting camera settings for a lighting condition.

    These values are rough starting points rather than exact exposure
    measurements.

    Args:
        condition (str):
            Lighting category received from the Arduino.

    Returns:
        dict:
            Suggested ISO, aperture, shutter speed, and advice.
    """
    recommendations = {
        "Very Dark": {
            "iso": "1600",
            "aperture": "f/1.8",
            "shutter_speed": "1/50",
            "advice": "Add lighting or use a tripod.",
        },
        "Indoor": {
            "iso": "400–800",
            "aperture": "f/2.8–f/4",
            "shutter_speed": "1/50",
            "advice": "Check highlights and skin tones.",
        },
        "Bright": {
            "iso": "100–200",
            "aperture": "f/4–f/8",
            "shutter_speed": "1/100",
            "advice": "Good general filming conditions.",
        },
        "Very Bright": {
            "iso": "100",
            "aperture": "f/8–f/11",
            "shutter_speed": "1/200",
            "advice": "Consider an ND filter.",
        },
    }

    return recommendations.get(
        condition,
        {
            "iso": "Unknown",
            "aperture": "Unknown",
            "shutter_speed": "Unknown",
            "advice": "Unable to classify lighting.",
        },
    )