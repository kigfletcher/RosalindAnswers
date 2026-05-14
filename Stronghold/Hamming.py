import argparse

#Add argument parsing due to long seq text
parser = argparse.ArgumentParser(
    description="Calculate Hamming Distance between two DNA strings"
)

parser.add_argument(
    "input_file", help="Path to input file"
)

args = parser.parse_args()

with open(args.input_file, "r") as file:
    s1 = file.readline().strip()
    s2 = file.readline().strip()

#Initial definition
count = 0
diff = 0

#Should not reuse names as in first soltuion
#Do not need to zip outside of the loop
for base1, base2 in zip(s1, s2):
    count = count + 1 # count not necessary for problem but nice to have
    if s1 != s2:
        diff += 1
print(diff)

#Cool alternative: diff = sum(base1 != base2 for base1, base2 in zip(s1, s2))