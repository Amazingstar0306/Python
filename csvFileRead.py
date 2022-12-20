import csv
with open("python.csv") as csv_file:
    csv_reader=csv.DictReader(csv_file)
    line_count=0
    for row in csv_reader:
        if line_count==0:
            print(f'colum names are{",".join(row)}')
            line_count+=1
        print(f'\t{row["name"]} works in {row["department"]} in department, was born in {row["birthday month"]}')
        line_count+=1
    print(f'processed {line_count} lines')
