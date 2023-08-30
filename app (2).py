pip install streamlit


import streamlit as st

def find_largest_number(a, b, c):
    return max(a, b, c)

def main():

    st.title("Find the Largest Number")
    
    st.write("Enter three numbers to find the largest among them.")

    a = st.number_input("Enter the first number:")
    b = st.number_input("Enter the second number:")
    c = st.number_input("Enter the third number:")

    if st.button("Find Largest"):
        largest = find_largest_number(a, b, c)
        st.success(f"The largest number among {a}, {b}, and {c} is: {largest}")

if __name__ == "__main__":
    main()

