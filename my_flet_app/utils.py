def format_minutes(minutes):
    minutes = int(minutes)
    total_seconds = minutes * 60
    formatted_time = f"{total_seconds // 60:02}:{total_seconds % 60:02}"
    return formatted_time