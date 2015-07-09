Title: Python matrix initialization
Date: 14:55 Thu 09 Jul 2015
Tags: python,code,bug
Category: dev
Author: pdt
Summary: init a matrix in python


# Problem
Yesterday I was doing some data analysis where there's a intermediary step I had to store the result in a matrix of fixed size that
we know a priori. When it finished the calculation, I looked up to see it had given an very unexpected result. After
spending sometime trying to track the issue down, it turned out that there's a line where I initialized the matrix
like follows:

```python
NROWS, NCOLS = (3, 5)
mat = [[0.0]*NCOLS]*NROWS

```

what's wrong with this line is that it translates equivalently to

```python
NROWS, NCOLS = (3, 5)
row = [0.0]*NCOLS
mat = []
for i in range(NROWS):
    mat.append(row)
```
so we got a matrix in which all the rows refer to the same list. To illustrate the problem:
```python
>>> mat
[[0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0]]
>>> mat[0][1] = 2
>>> mat
[[0.0, 2, 0.0, 0.0, 0.0], [0.0, 2, 0.0, 0.0, 0.0], [0.0, 2, 0.0, 0.0, 0.0]]
```
Apparently, this behavior it's pretty well-known among python dev.

# How to fix this?
There're several ways actually. For example we can use list comprehension like so:

```python
>>> NROWS, NCOLS = (3, 5)
>>> mat = [[0.0]*NCOLS for i in range(NROWS)]
>>> mat
[[0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0]]
>>> mat[0][1] = 2.5
>>> mat
[[0.0, 2.5, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0]]
>>> 
```

I ended up using the `numpy.zeros()` function which I should have had done in the first place since the matrix would
eventually be converted into `numpy.array`



