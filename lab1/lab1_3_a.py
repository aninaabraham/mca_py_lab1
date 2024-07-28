def print_pattern(n):
    for i in range(n):
        # Print leading spaces
        print(' ' * (n - i - 1), end='')

       
        for j in range(i + 1):
            print(chr(65 + j), end=' ')

        #  next line
        print()


n = 5#no of lines
print_pattern(n)
