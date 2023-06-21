def tandem_bicycle(red_shirt_speeds, blue_shirt_speeds, fastest):
    red_shirt_speeds.sort()
    blue_shirt_speeds.sort(reverse=fastest)
    result = 0
    for i, value in enumerate(red_shirt_speeds):
        result += max(red_shirt_speeds[i], blue_shirt_speeds[i])
    return result
