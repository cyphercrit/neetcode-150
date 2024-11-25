from typing import List

'''
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

    - The operands may be integers or the results of other operations.
    - The operators include '+', '-', '*', and '/'.
    - Assume that division between integers always truncates toward zero.

'''

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                x, y = stack.pop(), stack.pop()
                stack.append(int(y / x))
            else:
                stack.append(int(char))

        return stack.pop()
