"""Ontopo API

Usage:
  ontopo-api.py find -m <month> -s <size> -t <time> -r <restaurant>
"""
from typing import List, Tuple
import docopt
from calendar import monthrange
from api import search_available_table

def find_in_month(month: int, size: int, time: str, restaurant: str) -> List[Tuple[str]]:
    month_days = monthrange(2022, month)
    found = []

    if month < 10:
        month = "0" + str(month)

    month = str(month)
    size = str(size)
    print("Searching...")
    for i in range(month_days[0], month_days[1] + 1):
        day = str(i)
        if i < 10:
            day = "0" + str(i)
        print(f"Searching for {day}/{month}", end="\r")
        date = "2022" + month + day
        ans = search_available_table(restaurant, 
            {"size": size, "date": date, "time": time})
        if ans["method"] not in ["standby", "disabled"]:
            found.append((day, month, time, size))
    print()
    return found

def main():
    args = docopt.docopt(__doc__)
    if args["find"]:
        found = find_in_month(int(args["<month>"]), int(args["<size>"]), args["<time>"], restaurant=args["<restaurant>"])
        
        for day, month, time, size in found:
            hours, min = time[:2], time[2:]
            print(f"Found {day}/{month} at {hours}:{min} for {size} people")
            
        if not found:
            print("No tables found")
    


if __name__ == "__main__":
    main()
