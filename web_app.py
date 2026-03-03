import web_app as st

# Initialize session state
if "balance" not in st.session_state:
    st.session_state.balance = 100000.0

if "history" not in st.session_state:
    st.session_state.history = []

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False


st.title("🏦 ATM Simulator")

# -------- Authentication --------
if not st.session_state.authenticated:
    st.subheader("Login")
    pin = st.text_input("Enter PIN", type="password")

    if st.button("Login"):
        if pin == "1234":
            st.session_state.authenticated = True
            st.success("Login successful")
        else:
            st.error("Wrong PIN")

# -------- ATM MENU --------
else:
    st.subheader("ATM Menu")

    st.info(f"💰 Current Balance: ₹{st.session_state.balance}")

    amount = st.number_input("Enter amount", min_value=0.0, step=500.0)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Deposit"):
            if amount > 0:
                st.session_state.balance += amount
                st.session_state.history.append(f"Deposited ₹{amount}")
                st.success("Amount deposited successfully")
                st.success(f"Updated Balance: ₹{st.session_state.balance:,.2f}")
            else:
                st.error("Invalid amount")

    with col2:
        if st.button("Withdraw"):
            if amount > st.session_state.balance:
                st.error("Insufficient balance")
            elif amount <= 0:
                st.error("Invalid amount")
            else:
                st.session_state.balance -= amount
                st.session_state.history.append(f"Withdrawn ₹{amount}")
                st.success("Amount withdrawn successfully")
                st.success(f"Updated Balance: ₹{st.session_state.balance:,.2f}")

    st.divider()

    if st.button("Show Transaction History"):
        if not st.session_state.history:
            st.warning("No transactions yet")
        else:
            st.subheader("Transaction History")
            for tx in st.session_state.history:
                st.write("•", tx)

    if st.button("Logout"):
        st.session_state.authenticated = False
        st.success("Logged out successfully")
