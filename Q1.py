def analyze_attendance(log: str) -> dict:
    if not log:
        return {}
    
    names = log.lower().split()
    unique = list(set(names))
    counts = {n: names.count(n) for n in unique}
    most = max(counts, key=counts.get)
    least = min(counts, key=counts.get)
    
    return {
        "entries": names,
        "unique_employees": unique,
        "total_entries": len(names),
        "checkin_counts": counts,
        "most_active": most,
        "least_active": least
    }


log = "John Alice john Bob alice john"
result = analyze_attendance(log)
print(result)