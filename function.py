import autoit
from time import sleep


def wait(n):
  for x in range(0, n):
    sleep(1)
    print(x)


def fill_form(name, father_name, dob, nic,personal_number='11111',phone_number='33333333333', join_date='30-SEP-2022'):
  # Name
  wait(5)
  autoit.mouse_click("left", 120, 250)
  autoit.send("^a{BS}")
  # autoit.send({BS})
  autoit.send(name)

  # Father Name
  autoit.mouse_click("left", 450, 250)
  autoit.send("^a{BS}")
  autoit.send(father_name)

  # Gender
  autoit.mouse_click("left", 750, 250)
  autoit.mouse_click("left", 750, 300)
  
  # Birth
  autoit.mouse_click("left", 1000, 300)
  autoit.send("^a{BS}")
  autoit.send(dob)

  #nic
  autoit.mouse_click("left", 145, 360)
  wait(1)
  autoit.mouse_click("left", 145, 360)
  autoit.send("^a{BS}")
  autoit.send(nic)
# 1560230691329
  # JOin Date
  
  autoit.mouse_click("left", 450, 360)
  autoit.send("^a{BS}")
  autoit.send(join_date)

  # Personal Number
  autoit.mouse_click("left", 130, 417)
  wait(1)
  autoit.mouse_click("left", 130, 417)
  autoit.send("^a{BS}")
  autoit.send(personal_number)

  # Phone NO
  autoit.mouse_click("left", 145, 580)
  autoit.send("^a{BS}")
  autoit.send(phone_number)

  # Phone NO
  autoit.mouse_click("left",1180, 900)


