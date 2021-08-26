#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
 

#Example 1:

#Input: s = "()"
#Output: true
#Example 2:

#Input: s = "()[]{}"
#Output: true
#Example 3:

#Input: s = "(]"
#Output: false
#Example 4:

#Input: s = "([)]"
#Output: false
#Example 5:

#Input: s = "{[]}"
#Output: true
 

#Constraints:

#1 <= s.length <= 104
#s consists of parentheses only '()[]{}'.
def isValid(s: str) -> bool:
    result = True
    paranthesisStack = []
    closeDict = dict()
    closeDict[')'] = '('
    closeDict[']'] = '['
    closeDict['}'] = '{'
    for i in range(0,len(s)):
        if(s[i] not in closeDict):
            paranthesisStack.append(s[i])
        else:
            if(len(paranthesisStack) > 0 and paranthesisStack[len(paranthesisStack)-1] == closeDict[s[i]]):
                paranthesisStack.pop()
            else:
                result = False
                break
    if(len(paranthesisStack) > 0):
        result = False

    return result

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([)]"))
print(isValid("{[]}"))
print(isValid("})"))
        