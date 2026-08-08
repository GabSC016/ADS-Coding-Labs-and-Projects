def square_root_bisection(number, tolerance=1e-7, maximum_iterations=50):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    elif number == 0:
        print("The square root of 0 is 0")
        return 0
    
    elif number == 1:
        print("The square root of 1 is 1")
        return 1
    
    else:
        attemps = 0
        
        if number > 1:
            low = 0
            high = number
        
        else:
            low = 0
            high = 1

        while not attemps == maximum_iterations:

            mid = (low + high)/2

            if number**0.5 - tolerance < mid < number**0.5 + tolerance:
                attemps +=1
                print(f'The square root of {number} is approximately {mid}')
                return mid
            
            elif mid**2 > number:
                high = mid
                attemps += 1
            
            else:
                low = mid
                attemps += 1