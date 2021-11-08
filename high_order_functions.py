from functools import reduce

def run():
   # Filter 
    my_list = [1, 2, 3, 4, 5]
    new_list = list(filter(lambda x: x % 2 == 0, my_list))
    
    print(new_list)

   # Map
    squares = list(map(lambda x: x ** 2, my_list))

    print(squares)

   # Reduce
    exit_list = [2, 2, 2, 2 ,2]
    other_list = reduce(lambda a, b: a + b, exit_list)
    
    print(other_list)


if __name__ == "__main__":
    run()