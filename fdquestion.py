from datetime import datetime


def date_difference(date_str1, date_str2, date_format="%Y-%m-%d"):
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        tensors = date2 - date1
        return abs(tensors.days)


senior_citizen = input("Are you a senior citizen type 'Y' fro yes and 'N' for no").upper()
start_Date = input("enter your startdate in dd/mm/yyyy format").strip()
end_Date = input("enter your enddate in dd/mm/yyyy format").strip()

days = date_difference(start_Date, end_Date)

def interest_rate(senior_citizen,start_Date,end_Date):
  if senior_citizen == 'Y' and start_Date < '2019/05/09':
     print("Senior citizens")
     if days >= 7 and days <= 45:
        return '6.25'
     elif days >= 46 and days <= 179:
        return '6.75'
     elif days >= 180 and days <= 210:
        return '6.85'
     elif days >= 211 and days <= 365:
        return '6.90'
     elif days >= 366 and days <= 730:
        return '7.30'
     elif days >= 730 and days <=1000 :
        return '7.30'
     elif days >= 1001 and days <= 1300 :
        return '7.35'
  elif senior_citizen == 'Y' and start_Date > '2019/05/09':
      print("Senior citizens")
      if days >= 7 and days <= 45:
        return '6.25'
      elif days >= 46 and days <= 179:
        return '6.75'
      elif days >= 180 and days <= 210:
        return '6.85'
      elif days >= 211 and days <= 364:
        return '6.90'
      elif days >= 365 and days <= 730:
        return '7.50'
      elif days >= 730 and days <=1000 :
        return '7.20'
      elif days >= 1001 and days <= 1300 :
        return '7.10'
  elif senior_citizen == 'N' and start_Date < '2019/05/09':
      print("Non Senior citizens")
      if days >= 7 and days <= 45:
        return '5.75'
      elif days >= 46 and days <= 179:
        return '6.25'
      elif days >= 180 and days <= 210:
        return '6.35'
      elif days >= 211 and days <= 365:
        return '6.40'
      elif days >= 366 and days <= 730:
        return '6.80'
      elif days >= 730 and days <=1000 :
        return '6.80'
      elif days >= 1001 and days <= 1300 :
        return '6.85'
  elif senior_citizen == 'N' and start_Date > '2019/05/09':
      print("Non Senior citizens")
      if days >= 7 and days <= 45:
        return '5.75'
      elif days >= 46 and days <= 179:
        return '6.25'
      elif days >= 180 and days <= 210:
        return '6.35'
      elif days >= 211 and days <= 365:
        return '6.40'
      elif days >= 366 and days <= 730:
        return '7.00'
      elif days >= 730 and days <=1000 :
        return '6.70'
      elif days >= 1001 and days <= 1300 :
        return '6.60'
      else :
        if days > 1300 :
          print("fd not aviable for this period of days")
      interest_rate(senior_citizen , start_Date , end_Date)
# ----------------------------------------------------------------------


from datetime import datetime

def date_difference(date1, date2):
    format = "%d/%m/%Y"
    d1 = datetime.strptime(date1, format)
    d2 = datetime.strptime(date2, format)
    return abs((d2 - d1).days)

def get_interest_rate(senior, start_date, days):
    change_date = datetime.strptime("09/05/2019", "%d/%m/%Y")
    start = datetime.strptime(start_date, "%d/%m/%Y")
    rates = {
        "Y": {
            "before": [
                (7,45,6.25),(46,179,6.75),(180,210,6.85),
                (211,365,6.90),(366,1000,7.30),(1001,1300,7.35)
            ],
            "after": [
                (7,45,6.25),(46,179,6.75),(180,210,6.85),
                (211,364,6.90),(365,730,7.50),
                (731,1000,7.20),(1001,1300,7.10)
            ]
        },
        "N": {
            "before": [
                (7,45,5.75),(46,179,6.25),(180,210,6.35),
                (211,365,6.40),(366,1000,6.80),(1001,1300,6.85)
            ],
            "after": [
                (7,45,5.75),(46,179,6.25),(180,210,6.35),
                (211,365,6.40),(366,730,7.00),
                (731,1000,6.70),(1001,1300,6.60)
            ]
        }
    }
    period = "before" if start < change_date else "after"
    for min_d, max_d, rate in rates[senior][period]:
        if min_d <= days <= max_d:
            return rate
    return "FD not available"
senior = input("Senior citizen (Y/N): ").upper()
start = input("Enter Start Date (dd/mm/yyyy): ")
end = input("Enter End Date (dd/mm/yyyy): ")
days = date_difference(start, end)
rate = get_interest_rate(senior, start, days)
print("Total Days:", days)
print("Interest Rate:", rate)
