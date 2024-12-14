def make_readable(seconds):

    hours, restHours = divmod(seconds, 3600)

    minutes, seconds = divmod(restHours, 60)


    result = []
    if hours < 10:
        result.append(f"0{hours}")
    else:
        result.append(f"{hours}")

    if minutes < 10:
        result.append(f"0{minutes}")
    else:
        result.append(f"{minutes}")

    if seconds < 10:
        result.append(f"0{seconds}")
    else:
        result.append(f"{seconds}")

    return ':'.join(result)