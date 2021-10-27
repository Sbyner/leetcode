class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = deque()
        val = 1
        while len(ans) < n:
            curr = 
            if val%3==0:
                curr += Fizz
            if val%5==0:
                curr += Buzz
            if not curr:
                curr += str(val)
            ans.append(curr)
            val += 1
        return list(ans)
