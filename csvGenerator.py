import csv
import re
input_file = '/home/black-water/Desktop/CSV_generator/usagestat.txt'

output_csv = '/home/black-water/Desktop/CSV_generator/usagestat.csv'

def parse_line(line):
    match = rezex_pattern.search(line)
    return match.groupdict() if match else None

rezex_pattern = re.compile(
    r"time=\"(?P<Time>[^\"]+)\"\s+"
    r"type=(?P<Type>[^\s]+)\s+"
    r"package=(?P<Package>[^\s]+)\s+"
    r"(class=(?P<Class>[^\s]+)\s+)?"
    r"(instanceId=(?P<InstanceId>[^\s]+)\s+)?"
    r"(taskRootPackage=(?P<TaskRootPackage>[^\s]+)\s+)?"
    r"(taskRootClass=(?P<TaskRootClass>[^\s]+)\s+)?"
)


with open(input_file, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
    csv_write = csv.DictWriter(outfile, fieldnames=["Time", "Type", "Package", "Class", "InstanceId", "TaskRootPackage", "TaskRootClass"])
    csv_write.writeheader()
    
    for line in infile:
        parsed = parse_line(line)
        if parsed:
            csv_write.writerow(parsed)

print(f"CSV file has been created at: {output_csv}")
