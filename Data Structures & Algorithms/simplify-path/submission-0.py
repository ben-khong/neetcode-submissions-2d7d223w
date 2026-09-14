class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []

        for cmd in path:
            if cmd == '.' or cmd == "":
                continue
            elif cmd == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(cmd)
        
        return '/' + '/'.join(stack)
