import csv

#2 points - print the most common occupation and how many people were employed in that occupation - done
#2 points - print the least common occupation and how many people were employed in that occupation - done
#1 point - print the number of "Grape Growers" - done
#1 point - print the occupation with 14298 employees - done
#1 point - print the name of the occupation with the code 451311 - done
#1 point EXTRA CREDIT - print the top five most common occupations and their titles - done

with open("C:\\Users\\826311\\Documents\\Intro to Programming\\Intro-to-programming\\Assignments\\csv\\occupation-2018-census-csv.csv", "r", newline='', encoding='utf-8', errors='ignore') as file:
    table = csv.DictReader(file)

    job_codes = []
    occupations = []
    employees = []

    for row in table:
        if row["Occupation"] != "Total" and row["Occupation"] != "Total stated":
            job_codes.append(row["Code"])
            occupations.append(row["Occupation"])
            employees.append(int(row["Employed"]))
        else:
            continue
    
print("The most common occupation is:", occupations[employees.index(max(employees))], "with", max(employees), "employees")
print("The least common occupation is:", occupations[employees.index(min(employees))], "with", min(employees), "employees")
print("The number of Grape Growers is:", employees[job_codes.index("121215")] if "121215" in job_codes else 0)
print("The occupation with 14298 employees is:", occupations[employees.index(14298)] if 14298 in employees else "Not found")
print("The occupation with code 451311 is:", occupations[job_codes.index("451311")] if "451311" in job_codes else "Not found")
print("The top five most common occupations and their titles are:")
top_five = sorted(zip(employees, occupations), reverse=True)[:5]
for emp, occ in top_five:
    print(occ, "with", emp, "employees")