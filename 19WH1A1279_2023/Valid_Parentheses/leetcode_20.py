# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Input: s = "(]"
# Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        o=['{','[','(']
        for i in s:
            if i in o:
                st.append(i)
            else:
                if(len(st)>0):
                    if((i==")" and st[-1]=="(") or (i=="}" and st[-1]=="{") or (i=="]" and st[-1]=="[")):
                        st.pop()
                    else:
                        return False
                else:return False
        return(len(st)==0)
