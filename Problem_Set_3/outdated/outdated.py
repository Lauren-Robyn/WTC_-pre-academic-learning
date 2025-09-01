def main():
    import re

    months = [
         "January",
         "February",
         "March",
         "April",
         "May",
         "June",
         "July",
         "August",
         "September",
         "October",
         "November",
         "December"
        ]
    while True:
        date_ad = input("Date: ").strip()
        try:
            if "/"in date_ad:
                month, day, year = map(int, date_ad.split("/"))
            else:
                date_variables = re.split(r"[,\s/]+", date_ad)
                date_variables = [var for var in date_variables if var]
                month_str, day, year =date_variables
                month = months.index(month_str)+1
                day = int(day)
                year = int(year)

            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError
            break
        except (ValueError, IndexError):
            continue
    print(f"{year:04}-{month:02}-{day:02}")
main()
