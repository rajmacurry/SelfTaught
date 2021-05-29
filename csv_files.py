import csv
with open("data.csv","w") as f:
    write=csv.writer(f,delimiter=",")
    write.writerow(["one","two","three"])
    write.writerow(["four","five","six"])
    write.writerow(["seven","eight","nine"])

with open("data.csv","r") as f:
    r = csv.reader(f,delimiter=",")
    for row in r:
        print(",".join(row))
        