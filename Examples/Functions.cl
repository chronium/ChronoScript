import * from System.Streams

foo(x) = x * 3

bar(x, y) =
    if x < 10 do
        z = foo(x)
    else
        z = 5

    if y != 0 do
        y += foo(z)
        string(y) >> stdout

bar(5, 10)

factorial(0) = 1
factorial(n) = n * factorial(n - 1)