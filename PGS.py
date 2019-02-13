#!python3
# Sky Chrastina
# 190212

# should be able to pull character tables from:
# http://symmetry.jacobs-university.de/

import os
import sys
import numpy as np
import json

class PointGroup:

    def __init__(self, name, operators, irreps, table, functions):
        self.name = name
        self.ops = operators
        self.O = []
        self.N = []
        for (count, op) in operators:
            self.O.append(op)
            self.N.append(count)
        self.N = np.matrix([self.N])
        self.I = irreps
        self.T = np.matrix(table)
        self.F = functions
        (self.linear, self.quadratic, self.cubic) = functions

    def decompose(self, G):
        #print(f"Decomposing reducible representation {G} in {self.name}")
        N = np.sum(self.N)
        c = np.multiply(np.dot(np.multiply(self.T, self.N),G),1/N)
        for cint in np.nditer(c):
            if cint != int(cint):
                print("Non-integer encountered, invalid representation")
                return 1
        out = []
        for i in range(len(self.I)):
            if c[:,i] == 1:
                out.append(f"{self.I[i]}")
            elif c[:,i] > 0:
                out.append(f"{int(c[:,i])} {self.I[i]}")
        out = " + ".join(out)
        return out

    def __str__(self):
        s = ""
        s += f"Name: {self.name}\n"
        s += f"Operators: {self.ops}\n"
        s += f"Irreps:"
        for i in range(len(self.I)):
            s += f"\n{self.I[i]}\t"
            s += f"{str(self.T[i,:])}\t"
            s += f"{self.linear[i]}\t"
            s += f"{self.quadratic[i]}\t"
            s += f"{self.cubic[i]}"
        return s

# Load character tables
cwd = os.getcwd()
folder = "charactertables"
tables = {}
for file in os.listdir(cwd + "/" + folder):
    if str(file).find('.json') >= 0:
        data = None
        #print(f"Loading file {file}")
        with open(cwd + "/" + folder + "/" + file) as f:
            data = json.load(f)
        tables[data["name"]] = PointGroup(data["name"], data["operators"], data["irreps"], data["table"], (data["linear"], data["quadratic"], data["cubic"]))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("For help, call with './PGS.py -h'")
    elif sys.argv[1].find("-h") >= 0:
        print("\nDecompose representation with: PGS.py [PointGroup] [Representation]")
        print('Examples:\n./PGS.py Td 4,1,0,0,2\n./PGS.py C4v "5, 1, 1, 3, 1"')
        print("\nGet details of character table with: PGS.py [PointGroup]")
        print("Example:\n./PGS.py Td")
        print("\nCharacter tables available:")
        print(", ".join([key for key in tables.keys()]))
    elif len(sys.argv) == 2:
        pointgroup = sys.argv[1]
        print(tables[pointgroup])
    elif len(sys.argv) == 3:
        pointgroup = sys.argv[1]
        rep = sys.argv[2].split(",")
        representation = []
        for coeff in rep:
            representation.append(int(coeff))
        print(f"Decomposing {representation} in {pointgroup}")
        print(tables[pointgroup].decompose(representation))
