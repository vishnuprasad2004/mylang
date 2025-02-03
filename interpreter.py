import sys

def remove_quotes(s):
    return s[1:-1]

class Interpreter:
    """
    This class is responsible for interpreting the code.
    used the following yt video as a reference: https://www.youtube.com/watch?v=Q2UDHY5as90
    """
    def __init__(self):
        self.variables = {} 

    def prec(self, c):
        if c == '^':
            return 3
        elif c == '/' or c == '*':
            return 2
        elif c == '+' or c == '-':
            return 1
        elif c in {'>', '<', '>=', '<='}:  # Added comparative operators
            return 0.5
        else:
            return -1


    def infix_to_postfix(self,s):
        st = []
        result = ""
        i = 0
        s = s.split()

        for i in range(len(s)):
            c = s[i]
            # print(c, end=" ")
            # if i + 1 < len(s) and (s[i:i+2] in {'>=', '<='}):
            #     c = s[i:i+2]
            #     i += 1

            if c.isalnum():
                result += " "
                result += c
            elif c == '(':
                st.append('(')
            elif c == ')':
                while st[-1] != '(':
                    result += " "
                    result += st.pop()
                st.pop()
            else:
                while st and (self.prec(c) < self.prec(st[-1]) or self.prec(c) == self.prec(st[-1])):
                    result += " "
                    result += st.pop()
                st.append(c)
            i += 1
            
        
        # Pop all the remaining elements from the stack
        while st:
            result += " "
            result += st.pop()

        return result


    def evaluate(self, code):
        try:
            
            lines = [x for x in code.split("\n") if x.strip() != ""]
            pc = 0

            while pc < len(lines):
                line = lines[pc]

                match line.split(maxsplit=1)[0]:
                    case "\'":
                        pc += 1
                    case "while": 
                        if self.eval_expr(line.split(maxsplit=1)[1]) == 1: pc += 1
                        else: 
                            while lines[pc].split(maxsplit=1)[0] != "end": pc += 1
                            pc += 1

                    case "end": 
                        while lines[pc].split(maxsplit=1)[0] != "while": pc -= 1
                    
                    case "if":
                        # implement if statement
                        if self.eval_expr(line.split(maxsplit=1)[1]) == 1: pc += 1
                        else:
                            while lines[pc].split(maxsplit=1)[0] != "endif": pc += 1
                            pc += 1
                    case "endif":
                        pc += 1
                    case "print":
                        if line.split(maxsplit=1)[1][0] == "\"":
                            print(line.split(maxsplit=1)[1].split("\"")[1], end="")

                        elif line.split(maxsplit=1)[1][0] == "\'":
                            print(line.split(maxsplit=1)[1].split("\'")[1], end="")
                            
                        else:
                            print(self.eval_expr(line.split(maxsplit=1)[1]), end="")
                            
                        pc += 1

                    case "println":
                        if line.split(maxsplit=1)[1][0] == "\"":
                            print(line.split(maxsplit=1)[1].split("\"")[1])

                        elif line.split(maxsplit=1)[1][0] == "\'":
                            print(line.split(maxsplit=1)[1].split("\'")[1])
                            
                        else:
                            print(self.eval_expr(line.split(maxsplit=1)[1]))
                        pc += 1
                    case _: 
                        # this case is for variable assignment in the format of "name = expression"
                        (name, _, exp) = line.split(maxsplit=2)
                        # if the expression is an input, then we prompt the user for input
                        if exp.split()[0] == "input":
                            # format {variable_name = input data_type prompt_string(optional)}
                            (_, data_type, prompt) = exp.split(maxsplit=2)
                            if len(exp.split()) > 1:
                                data_type = exp.split()[1]
                                prompt = prompt[1:-1]
                                print(prompt, end="")
                                if data_type == "int":
                                    self.variables[name] = int(input())
                                elif data_type == "float":
                                    self.variables[name] = float(input())
                                elif data_type == "string":
                                    self.variables[name] = input()
                                elif data_type == "boolean":
                                    self.variables[name] = int(bool(input()))
                                else:
                                    raise Exception("Invalid data type")
                            else:
                                raise Exception("Syntax Error: Please provide data type and prompt string")
                            # self.variables[name] = int(input())
                        # otherwise, we evaluate the expression and store the result in the variable
                        else: 
                            self.variables[name] = self.eval_expr(exp)
                        pc += 1
        except Exception as e:
            print(e) 


    def eval_expr(self, expr):
        stack = []
        expr = self.infix_to_postfix(expr)
        toks = expr.split()
        for tok in toks:
            if tok.isalpha():
                if tok in self.variables: 
                    stack.append(self.variables[tok])
                else:
                    raise Exception(f"NameError: Variable {tok} not found")
            elif tok.isdigit(): stack.append(int(tok))
            else:
                rhs = stack.pop()
                lhs = stack.pop()
                if tok == "+": stack.append(lhs + rhs)
                elif tok == "*": stack.append(lhs * rhs)
                elif tok == "-": stack.append(lhs - rhs)
                elif tok == "/": stack.append(lhs / rhs)
                elif tok == ">=": stack.append(1 if lhs >= rhs else 0)
                elif tok == ">": stack.append(1 if lhs > rhs else 0)
                elif tok == "<=": stack.append(1 if lhs <= rhs else 0)
                elif tok == "<": stack.append(1 if lhs < rhs else 0)

        return stack[0]

if __name__ == "__main__":
    Interpreter().evaluate(open(sys.argv[1]).read())