import streamlit as st

def main():
    st.title("Find the largest among the 3 given numbers (value greater than the other two).")

    a = st.number_input("Enter the first number:")
    b = st.number_input("Enter the second number:")
    c = st.number_input("Enter the third number:")

    if st.button("Find largest number"):
        st.text(f"The largest among the 3 given numbers is: {max(a, b, c)}")

if __name__ == "__main__":
    main()
