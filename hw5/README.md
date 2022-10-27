# Python_BI_2022
Repository for bioinformatics institute

## RedBluePill (Tool for working with numpy arrays and matrices)


### System properties

The script was run on the GNU Linux **Ubuntu 20.04** LTS, with **Python** version **3.9.13**
I used **pip** version **22.0.4**


### Fast description

In this tool you can define between points in k-dimension space and multiplicate matrices.
Tool can check is the matrices matches for multiplication or not, multiplicate two or more matrices, compute minimal distance between two or more points in two- or more-dimentional space.


### Commands

#### matrix_multiplication

```python
matrix_multiplication(matrix1, matrix2)
```
> Functional

This command multiplicate matrices if they are resemble the rules (the number of columns in first matrix is equal to the number of rows in second matrix).

> Input data

Two numpy arrays.

> Output data

One matrix, as result of matrix multiplication

> Conditions, warnings and errors

If the number of columns in first matrix is not equal to the number of rows in second matrix, tool returns typical error. Example is given below:

```python
matrix_multiplication(np.array([[1],[2],[3]]), np.array([[1,2,3], [4,5,6]]))

ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 2 is different from 1)
```

#### multiplication_check

```python
multiplication_check(list_of_matrices)
```

> Functional

This command checks if matrices in list can be multiplicated in the lists order.

> Input data

Python list with numpy arrays.

> Output dara

Boolean: True if multiplication is possible, False if at least one multiplication is impossible.

> Conditions, warnings and errors

For succesfull multiplication matrices need to follow condition: number of first matrix columns needs ti be equal to number of second matrix rows.


#### multiply_matrices

```python
multiply_matrices(list_of_matrices)
```

> Functional

Command multiplicate 2+ matrices in the list oreder if it is possible.

> Input data

Python list with numpy arrays

> Output data

Resulting matrix if all multiplications completed succesfully or "None" in other cases.

> Conditions, warnings and errors

For succesfull multiplication matrices need to follow condition: number of first matrix columns needs ti be equal to number of second matrix rows.


#### compute_2d_distance

```python
compute_2d_distance(coords1, coords2)
```

> Functional

Predicated a distance between two points in 2-dimentional space.

> Input data

Two arrays with pair of numbers.

> Output data

Float that is equal a shortest distance between this to points.


#### compute_multidimensional_distance

```python
compute_multidimensional_distance(coords1, coords2)
```

> Functional

Predicated a distance between two points in multidimentional space.

> Input data

Two numpy arrays with equal number of numbers.

> Output data

Float that is equal a shortest distance between this to points.


#### compute_pair_distances

```python
compute_pair_distances(d2_matrix)
```

> Functional

Computes distance between all units of observations (rows in a 2-dim numpy matrix).

> Input data

Numpy 2d matrix with units of observations as rows and characteristics as columns.


> Output data

Numpy matrix with distances between each pair of observations.

> Conditions, warnings and errors

Can't work with more than 2-dimentional matrices.
