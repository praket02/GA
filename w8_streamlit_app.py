import streamlit as st

glowing_text_style = '''
    <style>
        .glowing-text {
            font-family: 'Arial Black', sans-serif;
            font-size: 33px;
            text-align: center;
            animation: glowing 2s infinite;
        }
        
        @keyframes glowing {
            0% { color: #FF9933; } /* Saffron color */
            10% { color: #FFD700; } /* Gold color */
            20% { color: #FF1493; } /* Deep Pink */
            30% { color: #00FF00; } /* Lime Green */
            40% { color: #FF4500; } /* Orange Red */
            50% { color: #9400D3; } /* Dark Violet */
            60% { color: #00BFFF; } /* Deep Sky Blue */
            70% { color: #FF69B4; } /* Hot Pink */
            80% { color: #ADFF2F; } /* Green Yellow */
            90% { color: #1E90FF; } /* Dodger Blue */
            100% { color: #FF9933; } /* Saffron color */
        }
    </style>
'''


st.markdown(glowing_text_style, unsafe_allow_html=True)
st.markdown(f'<p class="glowing-text">Streamlit Demo</p>', unsafe_allow_html=True)

def main():
    st.title("Find the largest among the 3 given numbers (value greater than the other two).")

    a = st.number_input("Enter the first number:")
    b = st.number_input("Enter the second number:")
    c = st.number_input("Enter the third number:")

    if st.button("Find largest number"):
        st.text(f"The largest among the 3 given numbers is: {max(a, b, c)}")

if __name__ == "__main__":
    main()
