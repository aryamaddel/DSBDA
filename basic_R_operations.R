# -------------------------------
# Basic Data Types in R
# -------------------------------

num_var <- 10.5
char_var <- "R Programming"
logical_var <- TRUE
complex_var <- 3 + 4i

print(num_var)
print(typeof(num_var))

print(char_var)
print(typeof(char_var))

print(logical_var)
print(typeof(logical_var))

print(complex_var)
print(typeof(complex_var))


# -------------------------------
# Vector Operations
# -------------------------------

v1 <- c(1, 2, 3)
v2 <- c(4, 5, 6)

print(v1 + v2)
print(v1 * v2)
print(sum(v1))


# -------------------------------
# Matrix Operations
# -------------------------------

matrix1 <- matrix(c(1,2,3,4,5,6,7,8,9), nrow = 3, byrow = TRUE)
matrix2 <- matrix(c(9,8,7,6,5,4,3,2,1), nrow = 3, byrow = TRUE)

print(matrix1)
print(matrix2)

# Matrix Addition
print(matrix1 + matrix2)

# Matrix Subtraction
print(matrix1 - matrix2)
