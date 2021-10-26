class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l = [int(st) for st in s.split() if st.isdigit()]
        return all(l[i] < l[i+1] for i in range(len(l)-1))
