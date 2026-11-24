class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res_s = []
        for i in tokens:
            if i in {"+", "-", "*", "/"}:
                b = res_s.pop()
                a = res_s.pop()
                if i == '+':
                    res_s.append(a + b)
                elif i == '-':
                    res_s.append(a - b)
                elif i == '*':
                    res_s.append(a * b)
                else:
                    res_s.append(int(a / b))
            else:
                res_s.append(int(i))
        return res_s[-1]
