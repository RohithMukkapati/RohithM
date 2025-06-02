from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(r):
            if r == n:
                sol = ["".join(row) for row in board]
                ans.append(sol)
                return

            for c in range(n):
                if c in placedCol or r + c in placedPos or r - c in placedNeg:
                    continue

                board[r][c] = "Q"
                placedCol.add(c)
                placedPos.add(r + c)
                placedNeg.add(r - c)

                backtrack(r + 1)

                board[r][c] = "."
                placedCol.remove(c)
                placedPos.remove(r + c)
                placedNeg.remove(r - c)

        board = [["."] * n for _ in range(n)]
        placedCol = set()
        placedPos = set()
        placedNeg = set()
        ans = []
        backtrack(0)
        return ans


if __name__ == "__main__":
    try:
        n = int(input("Enter the value of N (number of queens): "))
        if n <= 0:
            print("N must be a positive integer.")
        else:
            solution = Solution()
            results = solution.solveNQueens(n)
            print(f"\nNumber of solutions for {n}-Queens: {len(results)}\n")
            for i, solution in enumerate(results, 1):
                print(f"Solution {i}:")
                for row in solution:
                    print(row)
                print()
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
