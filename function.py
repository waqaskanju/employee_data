import autoit
from time import sleep

months = ['Jan', 'Feb', 'Mar', "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def wait(n):
  for x in range(0, n):
    sleep(1)
    print(x)

def format_date(date):
  date = str(date)[:10]
  current_date, current_month, current_year = date.split("-")
  try:
    current_month = int(current_month)
    current_month = months[current_month-1]
  except ValueError:
    pass
  return str(current_year.strip() + "-" + current_month.strip() + "-" +  current_date.strip()) 



def fill_form(name, father_name, dob, nic,personal_number='11111',phone_number='33333333333', join_date='30-SEP-2022'):
  # Name
  wait(5)
  autoit.mouse_click("left", 126, 228)
  autoit.send("^a{BS}")
  # autoit.send({BS})
  autoit.send(name)

  # Father Name
  autoit.mouse_click("left", 430, 228)
  autoit.send("^a{BS}")
  autoit.send(father_name)

  # Gender
  autoit.mouse_click("left", 737, 228)
  # Click on Male
  autoit.mouse_click("left", 690, 280)
  
  # Date of Birth Birth
  autoit.mouse_click("left", 987, 280)
  autoit.send("^a{BS}")
  autoit.send(dob)

  #nic
  autoit.mouse_click("left", 118, 337)
  wait(1)
  autoit.mouse_click("left", 118, 337)
  autoit.send("^a{BS}")
  autoit.send(nic)
# 1560230691329
  # JOin Date
  
  autoit.mouse_click("left", 433, 338)
  autoit.send("^a{BS}")
  autoit.send(join_date)

  # Personal Number
  autoit.mouse_click("left", 126, 398)
  wait(1)
  autoit.mouse_click("left", 126, 398)
  autoit.send("^a{BS}")
  autoit.send(personal_number)

  # Phone NO
  autoit.mouse_click("left", 133, 563)
  autoit.send("^a{BS}")
  autoit.send(phone_number)

  # Phone NO
  autoit.mouse_click("left",1183, 875)


