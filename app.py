import streamlit as st

st.title("Incentive Calculator")

# 1. Numerical input (2 decimal places)
num_input = st.number_input(
    "Deal Volume",
    min_value=0.00,
    step=0.01,
    format="%.2f"
)

# Calculate incentive cap
cap = 25000
if num_input < 2500000:
    cap = 7500
elif 2500000 <= num_input <= 5000000:
    cap = 11000
elif 5000000 < num_input <= 10000000:
    cap = 13500
elif 10000000 < num_input <= 15000000:
    cap = 16000
elif 15000000 < num_input <= 20000000:
    cap = 21000


# 2. Select option (3 choices)
option_2 = st.selectbox(
    "Goal Attainment",
    ["0-50%", r"50%-100%", ">100%"]
)

# 3. Select option (12 choices)
option_3 = st.selectbox(
    "Margin Difference vs Target",
    [">=10%",">=8%",">=6%",">=4%",">=2%","Target",">=-2",">=-4",">=-6",">=-8",">=-10","<-10%"]
)

# 4. Select option (5 choices)
option_4 = st.selectbox(
    "Cash Coverage %",
    [">120%",r">115%-120%",r">110%-115%","=>105-110%","<105%"]
)

# 5. Select option (2 choices)
option_5 = st.selectbox(
    "Compass Included",
    ["Yes", "No"]
)

# Example mapping values for calculation
map2 = {"0-50%": .01, r"50%-100%": .012, ">100%": .015}
map3 = {">=10%": 1.25,">=8%": 1.2,">=6%": 1.15,">=4%": 1.1,">=2%": 1.05,"Target": 1,">=-2": 0.95,">=-4": 0.9,">=-6": 0.85,">=-8": 0.8,">=-10": 0.75,"<-10%": 0.7}
map4 = {">120%": 1.25,r">115%-120%": 1.2,r">110%-115%": 1.15,"=>105-110%": 1.1,"<105%": 1}
map5 = {"Yes": 1.5, "No": 1}

# Calculation logic (customize as needed)
if st.button("Calculate"):
    final_value = num_input * map2[option_2] * map3[option_3] * map4[option_4] * map5[option_5]
    st.text("Incentive Value:")
    incentive = min(cap, final_value)
    st.write('$' + incentive.__format__(',.2f'))
