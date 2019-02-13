# PGS
Point Group Symmetry tool

Built for Inorganic Chemistry (CHEM 4011 @ CU Boulder)


## Decomposition
```
./PGS.py Td 4,1,0,0,2
```
```
A1 + T2
```

## Point group inspection
```
./PGS.py C3v
```
```
Name: C3v
Operators: [[1, 'E'], [2, 'C3'], [3, 'sv']]
Irreps:
A1      [[1 1 1]]       ['z']   ['x^2+y^2', 'z^2']      ['z^3', 'x(x^2-3y^2)', 'z(x^2+y^2)']
A2      [[ 1  1 -1]]    ['Rz']  []      ['y(3x^2-y^2)']
E       [[ 2 -1  0]]    ['(x, y)', '(Rx, Ry)']  ['(x^2-y^2, xy)', '(xz, yz)']   ['(xz^2, yz^2)', '(xyz, z(x^2-y^2))', '(x(x^2+y^2), y(x^2+y^2))']
```


# Future work
* Use split-type matrices to print symmetry group information
* Finish point group info
* Add more point groups
* Expand class functions
* 3d plotting/animation
* Point group detection from list of points
