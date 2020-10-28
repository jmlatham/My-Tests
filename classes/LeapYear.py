class LeapYear:
  def __init__(self):
    pass
  
  def determineYearStatus(self, year):
    # if  not isinstance(year, int):
    #   return "invalid data"
    try:
      yearInt = int(year)

      if yearInt < 1582:
          return "Not within the Gregorian calendar period!"
      elif yearInt % 4 != 0:
          return "Common year"
      elif yearInt % 100 == 0:
          return "Leap year"
      elif yearInt % 400 == 0:
          return "Common year"
      else:
        return "not sure"
    except:
      return "invalid data"