def format_duration(seconds):
    
    if seconds == 0:
        return "now"
    
    years, restYears = divmod(seconds, 365*24*3600)

    days, restDays = divmod(restYears, 24*3600)


    hours, restHours = divmod(restDays, 3600)

    minutes, seconds = divmod(restHours, 60)


    result = []

    if years > 0:
        if years == 1:
            result.append(f"{years} year")
        else:
            result.append(f"{years} years")
    if days > 0:
        if days == 1:
            result.append(f"{days} day")
        else:
            result.append(f"{days} days")
    if hours > 0:
        if hours == 1:
            result.append(f"{hours} hour")
        else:
            result.append(f"{hours} hours")
    if minutes > 0:
        if minutes == 1:
            result.append(f"{minutes} minute")
        else:
            result.append(f"{minutes} minutes")
    if seconds > 0:
        if seconds == 1:
            result.append(f"{seconds} second")
        else:
            result.append(f"{seconds} seconds")

    if len(result) > 2:
        finalResult = ", ".join(result[:-1]) + " and " + result[-1]
    elif len(result) == 2:
        finalResult = result[0] + " and " + result[1]
    else:
        finalResult = result[0]

    return finalResult