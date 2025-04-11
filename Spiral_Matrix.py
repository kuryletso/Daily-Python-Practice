# Excercise: https://leetcode.com/problems/spiral-matrix/
#
#
# Solution:

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        hs, ws = 0, 0
        he, we = len(matrix), len(matrix[0])
        output = []
        step = 0

        while he > hs and we > ws:
            if step%4 == 0:
                output.extend(matrix[hs][ws:we])
                hs += 1
                step += 1
            elif step%4 == 1:
                output.extend([matrix[i][we-1] for i in range(hs,he)])
                we -= 1
                step += 1
            elif step%4 == 2:
                output.extend(matrix[he-1][::-1][ws+1:we+1])
                he -= 1
                step += 1
            else:
                output.extend([matrix[i][ws] for i in range(he-1, hs-1, -1)])
                ws += 1
                step += 1

        return output
            



if __name__ == "__main__":
    mySol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(mySol.spiralOrder(matrix))