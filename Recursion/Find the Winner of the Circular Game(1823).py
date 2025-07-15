# Recursive Solution

class Solution(object):
    def findTheWinner(self, n, k):
        k -= 1  
        index = 0
        people = list(range(1, n + 1))

        def simulate(people, k, index):
            if len(people) == 1:
                return people[0]

            index = (index + k) % len(people)
            people.pop(index)
            return simulate(people, k, index)

        return simulate(people, k, index)

#Time complexity : O(N*2)
#Space complexity : O(N)


# Iterative Solution (Not my own solution)

class Solution(object):
    def findTheWinner(self, n, k):
        winner = 0  # 0-based index
        for i in range(2, n + 1):
            winner = (winner + k) % i
        return winner + 1  # Convert to 1-based index

#Time complexity : O(N)
#Space complexity : O(1)



