"""Ontopo API

Usage:
  ontopo-api.py find -m <month> -s <size> -t <time> -r <restaurant>
"""
import docopt
from calendar import monthrange
from ontopo_api import search_available_table

def find_in_month(month: int, size: int, time: str, restaurant: str):
    month_days = monthrange(2022, month)

    if month < 10:
        month = "0" + str(month)

    month = str(month)
    size = str(size)
    print("Searching...")
    for i in range(month_days[0], month_days[1] + 1):
        day = str(i)
        if i < 10:
            day = "0" + str(i)
        date = "2022" + month + day
        ans = search_available_table(restaurant, 
            {"size": size, "date": date, "time": time})
        if ans["method"] not in ["standby", "disabled"]:
            print("Found a table at " + day + "/" + month + " at " + time + " for " + size + " people")

def main():
    args = docopt.docopt(__doc__)
    if args["find"]:
        find_in_month(int(args["<month>"]), int(args["<size>"]), args["<time>"], restaurant=args["<restaurant>"])
    


if __name__ == "__main__":
    main()
