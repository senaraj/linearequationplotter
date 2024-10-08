import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import re


st.title("Linear Equation Plotter")
st.subheader("Made by Senaraj")
st.image("bar-graph.png", width=150)
equation = st.text_input("Enter a linear equation (in the form y = mx + b):", value="y = 2x + 1")


if equation:
    try:
        
        equation = equation.replace("y =", "").strip()

        
        pattern = r'(?P<m>[-+]?\d*\.?\d*)x\s*(?P<b>[-+]?\s*\d*\.?\d*)?'
        match = re.match(pattern, equation)
        
        if match:
            
            m = match.group('m').replace(" ", "")  
            b = match.group('b').replace(" ", "") if match.group('b') else "0"  

            if m == '' or m == '+':
                m = 1
            elif m == '-':
                m = -1
            else:
                m = float(m)
            
            b = float(b)  

            x = np.linspace(-10, 10, 400)
            
            y = m * x + b
            
            plt.figure(figsize=(6, 4))
            plt.plot(x, y, label=f"y = {m}x + {b}")
            plt.title("Graph of Linear Equation")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(0, color='black', linewidth=0.5)
            plt.grid(True)
            plt.legend()

            
            st.pyplot(plt)
        
        else:
            st.error("Error: Invalid equation format. Please enter in the form y = mx + b.")
    
    except Exception as e:
        st.error(f"Error: {e}")
