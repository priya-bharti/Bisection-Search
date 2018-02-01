# Bisection-Search
This repository explains the concept of bisection search

Algorithm:
  1. Start
  2. Initialize low = 1
  3. Initialize high = number
  4. mid = (low + high)/2
  5. Repeat steps 6 and 7 until value of mid is equal to the element to be searched
  6. If value of mid is matched with the value to be searched, return mid. Else do:
    (i) If mid is less than the value to be search, then low = mid
    (ii) If mid is greater than the value to be searched, then high = mid
  7. Computer again, mid = (low + high)/2
  8. Stop
