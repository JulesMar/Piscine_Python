import datetime

today = datetime.date.today()
now = datetime.datetime.now()

past_date = datetime.datetime(1970, 1, 1)
seconds_since_epoch = (now - past_date).total_seconds()
print("Seconds since January 1, 1970: %s or %s in scientific notation"
      % ("{:,.4f}".format(seconds_since_epoch),
         "{:.2e}".format(seconds_since_epoch)))

formatted_date = today.strftime('%b %d %Y')

print(formatted_date)
