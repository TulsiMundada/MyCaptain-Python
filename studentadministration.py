import csv

def write_into_csv(stud_list):
  with open('students.csv', 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
  
    if csv_file.tell() == 0:
      writer.writerow(["Name","Age","E-mail","Contact"])
  
    writer.writerow(stud_list)

if __name__ == '__main__':
  print("School Administration Program")
  n=0
  repeat = 'y'

  while repeat == 'y':
    print("\nNumber of details entered today: ", n ,'\n')
    details = input("Enter the details of students(Format: Name, Age, Email, Contact no.) : \n")

    details_list = details.split(', ')

    print("\nThe Entered Details are -\nName: {}\nAge: {}\nEmail: {}\nContact no: {}\n" .format(details_list[0],details_list[1],details_list[2],details_list[3]))

    correct= input("Are the details correct (Y/N): ").casefold()

    if correct=='y':
      write_into_csv(details_list)
      n+=1
    else:
      print("Please Re-enter")
      continue

    repeat = input("Do you want to add another student detail (Y/N)").casefold()

  print("All changes were Saved!")

