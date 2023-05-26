import timeit

def time_coversion(time):
    hh, mm, ss = map(int, time[:-2].split(':'))
    am_pm = time[-2:]

    if am_pm == 'PM' and hh != 12:
        hh += 12
    elif am_pm == 'AM' and hh == 12:
        hh = 0

    return f"{hh:02d}:{mm:02d}:{ss:02d}"


#user input
time = input("Enter a time in hh:mm:ss AM/PM format: ")

#Call the function
start = timeit.default_timer()
military = time_coversion(time)
end = timeit.default_timer()

#Print the result and time complexity
print(f"The military time is: {military}")
print(f"Time complexity: {end - start}")
