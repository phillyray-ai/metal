import random
from typing import Tuple

def get_random_activity() -> Tuple[int, str]:
    """
    Generate a random integer between 1 and 1000, then return it along
    with a corresponding "todo" activity based on its range.

    Returns:
        A tuple (number, activity), where:
        - number is a random integer in the inclusive range [1, 1000].
        - activity is a string describing the designated task for that number.
    """
    number = random.randint(1, 1000)

    # Define activity thresholds and their associated tasks
    ranges_to_tasks = [
        (range(1, 101), "run"),
        (range(101, 251), "walk"),
        (range(251, 501), "weights"),
        (range(501, 1001), "golf"),
    ]

    # Find the appropriate activity based on which range the number falls into
    activity = next(
        task for rng, task in ranges_to_tasks if number in rng
    )

    return number, activity


if __name__ == "__main__":
    num, task = get_random_activity()
    print(f"Generated number: {num} — Activity: {task}")
