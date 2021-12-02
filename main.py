data = []
with open("./data.csv") as f:
    for line in f:
        row = line.strip().split(',')
        if row[0] == 'RANK TIER':
            continue

        new_row = []
        for n in row[1:]:
            new_row.append(float(n.replace("%", "")))
        data.append(new_row)

ranks = [
    "Bronze 1",
    "Bronze 2",
    "Bronze 3",
    "Silver 1",
    "Silver 2",
    "Silver 3",
    "Gold 1",
    "Gold 2",
    "Gold 3",
    "Platinum 1",
    "Platinum 2",
    "Platinum 3",
    "Diamond 1",
    "Diamond 2",
    "Diamond 3",
    "Champion 1",
    "Champion 2",
    "Champion 3",
    "Grand Champion 1",
    "Grand Champion 2",
    "Grand Champion 3",
    "Supersonic Legend",
]

totals_table = []
running_totals = []
for row in reversed(data):
    for i, entry in enumerate(row):
        if len(running_totals) > i:
            running_totals[i] += entry
        else:
            running_totals.append(entry)
    totals_table.append(running_totals.copy())

print("""#Percentile Data

**This will tell you that you are in the top (x)% of players**

|RANK TIER|DOUBLES|STANDARD|SOLO DUEL|RUMBLE|DROPSHOT|HOOPS|SNOW DAY|TOURNAMENT|
|:-|:-|:-|:-|:-|:-|:-|:-|:-|""")

for i, total in enumerate(reversed(totals_table)):
    print(ranks[i], end="")
    for num in total:
        print('|', end="")
        print(round(num, 6), end="%")

    print()
