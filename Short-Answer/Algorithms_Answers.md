#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The while loop will run (n^3) / (n^2) times, which is equal to n times. Therefore the time complexity will be O(n)


b) The outer loop will run n times, while the inner loop will run log(n) times. For nested for loops, the time complexity is equal to n^x where x is the time complexity of the inner for loop. Therefore the total time complexity is n^log(n).


c) The function will recurse n times because it is being decremented by 1 each time until it reaches the base case. Therefore the time complexity for this function is O(n)

## Exercise II

  If egg does break, repeat this process but with the new lowest floor equal 
  to the current lowest and the highest floor to the current floor, as we know
  it cannot be dropped from any higher floor and survive, but could survive 
  from a lower floor```

if(broken == True):
    return max_drop(lowest_floor, dropped_floor)

  If egg doesn't break, repeat this process but with the new lowest floor
  equal to the current dropped_floor and the new highest floor equal to
  the current highest floor, as we know it could be dropped from a 
  higher floor and still survive.

if(broken == True):
    return max_drop(dropped_floor, highest_floor)

  Repeat this process until the target floor is found and return it
