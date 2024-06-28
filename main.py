def main():
    result = []
    a1 = int(input('Enter your first number: '))
    a2 = int(input('Enter your second number: '))
    N = int(input('Enter the number of sequences: '))
    
    for x in range (0,N):
        math = a1 + a2
        result.append(a1)
        a1 = a2
        a2 = math
        
    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result



if __name__ == '__main__':
    main()
