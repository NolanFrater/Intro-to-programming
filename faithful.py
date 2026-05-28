import csv

#average eruption time - done
#longest eruption time - done
#shortest eruption time - done
#average wait time - done
#longest wait time - done
#shortest wait time - done
#eruption time with the longest wait time - done

with open("C:\\Users\\826311\\Documents\\Intro to Programming\\Intro-to-programming\\Assignments\\csv\\faithful.csv", "r") as file:
    table = csv.DictReader(file)

    wait_times = []
    total_wait_time = 0
    eruption_times = []
    total_eruption_time = 0


    for row in table:
        wait_times.append(float(row["wait"]))
        total_wait_time += float(row["wait"])
        eruption_times.append(float(row["eruption"]))
        total_eruption_time += float(row["eruption"])


print("The longest eruption time is:", max(eruption_times), "minutes")
print("The shortest eruption time is:", min(eruption_times), "minutes")
print("The average eruption time is:", total_eruption_time / len(eruption_times), "minutes")
print("The longest wait time is:", max(wait_times), "minutes")
print("The shortest wait time is:", min(wait_times), "minutes")
print("The average wait time is:", total_wait_time / len(wait_times), "minutes")
print("The eruption time with the longest wait time is:", eruption_times[wait_times.index(max(wait_times))], "minutes")

