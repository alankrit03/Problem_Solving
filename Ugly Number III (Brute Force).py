class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        starts = [1, 1, 1]
        a, b, c = sorted([a, b, c])
        numbers = []
        k = 0
        print(a, b, c)
        while k < n:
            x = starts[0]
            y = starts[1]
            z = starts[2]

            new_num = min(a * x, b * y, c * z)

            if not new_num % a:
                starts[0] += 1

            if not new_num % b:
                starts[1] += 1

            if not new_num % c:
                starts[2] += 1

            numbers.append(new_num)
            k += 1
        print(numbers)
        return numbers[-1]

Solution().nthUglyNumber(25,2,4,7)