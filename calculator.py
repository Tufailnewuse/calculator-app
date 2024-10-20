import streamlit as st
import math
import numpy as np

st.title('Scientific Calculator')

# Input
expression = st.text_input('Enter your mathematical expression:')

# Define a function to evaluate mathematical expressions
def evaluate_expression(expr):
    try:
        # Use eval for safe mathematical evaluation
        result = eval(expr, {"__builtins__": None}, {
            "sin": math.sin, "cos": math.cos, "tan": math.tan,
            "asin": math.asin, "acos": math.acos, "atan": math.atan,
            "sinh": math.sinh, "cosh": math.cosh, "tanh": math.tanh,
            "asinh": math.asinh, "acosh": math.acosh, "atanh": math.atanh,
            "log": math.log, "log10": math.log10, "log2": math.log2,
            "sqrt": math.sqrt, "exp": math.exp, "pow": math.pow,
            "pi": math.pi, "e": math.e, "degrees": math.degrees, "radians": math.radians,
            "factorial": math.factorial, "abs": abs, "ceil": math.ceil, "floor": math.floor,
            "mod": np.mod, "gcd": math.gcd, "lcm": np.lcm
        })
        return result
    except Exception as e:
        return f"Error: {e}"

# Display result if expression is entered
if expression:
    result = evaluate_expression(expression)
    st.write(f"Result: {result}")

st.write("""
## Supported Functions:
- Trigonometry: sin, cos, tan, asin, acos, atan, sinh, cosh, tanh, asinh, acosh, atanh
- Logarithmic: log, log10, log2
- Exponential: exp, pow
- Roots and powers: sqrt
- Constants: pi, e
- Degrees and radians conversion: degrees, radians
- Factorial: factorial
- Misc: abs, ceil, floor, mod, gcd, lcm
""")
