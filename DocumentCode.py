# Import the timeit module
import timeit

def time_conversion(time):
    """
    This function converts a time in hh:mm:ss AM/PM format to military time format.

    Args:
    time (str): A string representing time in hh:mm:ss AM/PM format.

    Returns:
    military (str): A string representing time in military format.

    """
    # Split the time string into hours, minutes, seconds, and AM/PM
    hh, mm, ss = map(int, time[:-2].split(':'))
    am_pm = time[-2:]

    # Convert the hours to military format
    if am_pm == 'PM' and hh != 12:
        hh += 12
    elif am_pm == 'AM' and hh == 12:
        hh = 0

    # Format the military time string
    military = f"{hh:02d}:{mm:02d}:{ss:02d}"

    # Return the military time string
    return military


# Get user input for time in hh:mm:ss AM/PM format
time = input("Enter a time in hh:mm:ss AM/PM format: ")

# Call the time_conversion function to convert the time to military format
start = timeit.default_timer()
military = time_conversion(time)
end = timeit.default_timer()

# Print the military time and time complexity
print(f"The military time is: {military}")
print(f"Time complexity: {end - start}")