import streamlit as st
import random
import base64
from web3 import Web3
import json
import os
from dotenv import load_dotenv
load_dotenv('SECRETS.env')

CHRISTMAS_CONTRACT_ADDRESS = os.getenv("CHRISTMAS_CONTRACT_ADDRESS")
THANKSGIVING_CONTRACT_ADDRESS = os.getenv("THANKSGIVING_CONTRACT_ADDRESS")
SUMMER_CONTRACT_ADDRESS = os.getenv("SUMMER_CONTRACT_ADDRESS")
# Set the page config to make the background black and the layout wider
st.set_page_config(page_title=" Blockchain Community Board", layout="wide")

# Connect to a local Ethereum node
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# Check if the connection is successful
if w3.isConnected():
    st.write('Connected to Ethereum network')
else:
    st.write('Failed to connect to Ethereum network')
    
def load_contract(contract_address): 
  # Smart contract details
  # contract_address = '0xac940a821FF5B8fEfDD0977861ee53E297918289'
  contract_abi_path = 'contract_abi.json'  # Replace with the actual path
#  account_address = '0xYourAccountAddress'  # The Ethereum address interacting with the contract

  # Read the contract ABI from the compiled file
  with open(contract_abi_path, 'r') as abi_file:
      contract_abi = json.load(abi_file)

  # Create contract instance
  contract = w3.eth.contract(address=contract_address, abi=contract_abi)
  return contract

# Load the contract address from your Ganache accounts
ganache_accounts = w3.eth.accounts

# Streamlit UI
st.title("Interact with Ethereum Contract")

contract1=load_contract(CHRISTMAS_CONTRACT_ADDRESS)
contract2=load_contract(THANKSGIVING_CONTRACT_ADDRESS)
contract3=load_contract(SUMMER_CONTRACT_ADDRESS)   

# # Streamlit UI
# st.title("Vote using Streamlit")

# # Replace 'your_choice' with the actual choice you want to vote for
# vote_choice = st.number_input("Enter your vote choice:", min_value=0, max_value=255, value=0, step=1)

# if st.button("Vote"):
#     result = vote(vote_choice)
#     st.write(result)
    
# Custom CSS to enhance the appearance
st.markdown(
    """
    <style>
    .stApp { background-color: black; }
    .video-frame, .proposal-box {
        border: 3px solid; border-image-slice: 1; border-width: 5px;
        border-image-source: linear-gradient(to left, #743ad5, #d53a9d); border-radius: 10px; margin: 10px;
        background-color: #1e1e1e; color: white; box-shadow: 0 4px 8px 0 rgba(255, 255, 255, 0.2);
    }
    .block-container { padding-top: 5rem; padding-bottom: 5rem; }
    .css-12w0qpk { padding-top: 0; padding-bottom: 0; }
    .st-bj { flex: none; }
    .stVideo { box-shadow: 0 4px 8px 0 rgba(255, 255, 255, 0.2), 0 6px 20px 0 rgba(255, 255, 255, 0.19); }
    h3, h4, h5, h6, .label, .white-text, .proposal-text { color: #D4AF37; }
    h1{ color: #D4AF37; text-align: center; }
    h2, .label, .white-text, .proposal-text { color: #FFFFFF; }
    body, .stMarkdown { 
        color: #FFFFFF !important; /* Force white text color */
    }
    button, .connect-wallet {
        background-color: #FFFFFF; color: white; border: none; padding: 10px 20px;
        font-size: 16px; margin: 4px 2px; cursor: pointer; transition-duration: 0.4s;
    }
    button:hover, .connect-wallet:hover { background-color: #555; }
    img:hover { opacity: 0.7; }
    .stSelectbox .css-2b097c-container { width: 50%; margin: 0 auto; }
    .connect-wallet {
        position: absolute; top: 10px; right: 10px; font-size: 16px;
        border-radius: 5px; background-color: #D4AF37; color: black;
    }
    # Custom CSS for Dropdown Styles
     <style>
    .stSelectbox .css-2b097c-container {
        border: 2px solid #743ad5; /* Border color */
        border-radius: 10px; /* Rounded borders */
        background-color: #FFFFFF; /* Background color */
        color: white; /* Text color */
    }
    .stSelectbox .css-yk16xz-control {
        border-radius: 10px;
        border: none; /* Remove default border */
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* Box shadow for depth */
    }
    .stSelectbox .css-1uccc91-singleValue {
        color: white; /* Color of selected item */
    }
    </style>
    <button class="connect-wallet">Connect Wallet</button>
    """,
    unsafe_allow_html=True
)

# Logo path
logo_path = "https://turquoise-persistent-swordtail-499.mypinata.cloud/ipfs/QmSdYfoiE7R1faws5EdMvzAtW5GcY1wX51zjGDJAVvsXzB?_gl=1*1hvt56s*_ga*OTA4Mjc1NTIuMTY5OTU5MDYwMA..*_ga_5RMPXG14TE*MTcwMDExMjQ2My43LjEuMTcwMDExMjk3Mi41NC4wLjA."

# Centering the logo in a full-width column
st.container()
col1, col2, col3, col4 = st.columns([1, 3, 1, 1])
with col1:
    st.image(logo_path, width=75)  # Adjust width as needed

    # Mission Statement
st.markdown(
    """
    <div class="white-text">
        <h3>Our Mission</h3>
        <p>Our mission is to revolutionize homeowners' association (HOA) governance by integrating cutting-edge blockchain technology. We empower homeowners with NFT-based voting rights, ensuring transparent and secure decision-making for community proposals. By owning a home, residents receive a unique NFT, symbolizing their stake and voice in the HOA. This innovative approach fosters community engagement, promotes equitable participation, and upholds the integrity of the voting process. We are committed to building a harmonious, forward-thinking community where every homeowner's vote is valued and impactful in shaping the future of their neighborhood.</p>
    </div>
    """,
    unsafe_allow_html=True
)


# Title (centered)
st.title("HOA NFT Gallery")

# Display videos
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.video("https://turquoise-persistent-swordtail-499.mypinata.cloud/ipfs/QmYvMPG7mDbwTSaoXMB2h4v9b25mvARjVXfUfFtaj2hCsZ?_gl=1*1cfg10*_ga*OTA4Mjc1NTIuMTY5OTU5MDYwMA..*_ga_5RMPXG14TE*MTcwMDExMjQ2My43LjEuMTcwMDExMzI1Mi4xMi4wLjA")
with col2:
    st.video("https://turquoise-persistent-swordtail-499.mypinata.cloud/ipfs/QmUWL6hWeLeLmtnL2jDRDD62FJAthYZszVqtSjUYWjHSTT?_gl=1*2h3vhr*_ga*OTA4Mjc1NTIuMTY5OTU5MDYwMA..*_ga_5RMPXG14TE*MTcwMDExMjQ2My43LjEuMTcwMDExMzI0My4yMS4wLjA")
with col3:
    st.video("https://turquoise-persistent-swordtail-499.mypinata.cloud/ipfs/QmRVcK1w3CnR1Bz2UbRmngySoUf5f2LQs72EuQD6hBE9cU?_gl=1*1boj1t8*_ga*OTA4Mjc1NTIuMTY5OTU5MDYwMA..*_ga_5RMPXG14TE*MTcwMDExMjQ2My43LjEuMTcwMDExMzIwOS41NS4wLjA")
with col4:
    st.video("https://turquoise-persistent-swordtail-499.mypinata.cloud/ipfs/QmUNveENrMQteNXpArkxFe4DvuffjqLXzvz4avhwbgHN5T?_gl=1*mp1nwr*_ga*OTA4Mjc1NTIuMTY5OTU5MDYwMA..*_ga_5RMPXG14TE*MTcwMDExMjQ2My43LjEuMTcwMDExMzIwNi41OC4wLjA")
#with col5:
#    st.video("path/to/video5.mp4")

# Function to encode video file for embedding
def get_video_html(path):
    with open(path, 'rb') as video_file:
        video_bytes = video_file.read()
    base64_video = base64.b64encode(video_bytes).decode('utf-8')
    return f'<video loop autoplay class="custom-box"><source src="data:video/mp4;base64,{base64_video}" type="video/mp4"></video>'
  
# contract_address_options = [
#     web3.eth.accounts
#     ]
# selected_wallet_address = st.selectbox("Select Wallet Address", contract_address_options)

contract_address_options = st.selectbox("Select Contract Address", ganache_accounts)

contract_abi_path = 'contract_abi.json'

# Custom CSS for styling, including proposal boxes
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
    }
    .proposal-box {
        border: 2px solid;
        border-image-slice: 1;
        border-image-source: linear-gradient(to left, #D4AF37, #ecd540 ); /* Change colors here */
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
        background-color: #1e1e1e;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Proposal in a styled box
st.markdown(
    """
    <div class="proposal-box">
        <h2>Community Christmas Party Proposal</h2>
        <p>Description: Join us for a festive Christmas party at our Community Clubhouse! Planned activities include live music, a catered dinner, a children's play area, and a special visit from Santa Claus.</p>
        <p>Date: December 24th | Time: 6 PM - 10 PM</p>
         <p><strong>How to Vote:</strong><ol>
            <li>Log into the HOA Voting Platform.</li>
            <li>Select 'Proposals'.</li>
            <li>Find the 'Community Christmas Party' proposal.</li>
            <li>Use your NFT to authenticate and vote.</li>
    </div>
    """,
    unsafe_allow_html=True
)
# Dropdown for voting on the Christmas party proposal
christmas_party_vote = st.selectbox(
    "Vote for the Community Christmas Party Proposal",
    ["Approve", "Reject", "Abstain"],
    key="christmas_party_vote"
)

# Button to vote
if st.button("Click Here To Vote", key="vote1"):
    # Call the vote function in the smart contract
    vote_option = christmas_party_vote.lower()  # Convert to lowercase to match the Solidity function parameter
    try:
        # Ensure that the voting is done from the selected address
        sender_address = selected_wallet_address

        # Call the vote function in the smart contract
        transaction = contract1.functions.vote(vote_option).transact({'from': sender_address})
        
        # build transaction
        # sign transaction w/ pkey
        # send raw transaction

        st.write(f"Vote submitted from address: {sender_address}")
    except Exception as e:
        st.write(f"Error: {str(e)}")
        
# Community Christmas Party Proposal
st.markdown('<div class="proposal-box"><h2>Community Christmas Party Proposal</h2><p>Christmas Party Proposal Voting Results.</p></div>', unsafe_allow_html=True)
# fake_vote_count_christmas = random.randint(0, 100)
# st.progress(fake_vote_count_christmas)
# optionId_mapping=contract1.functions.optionId().call()
# optionId_mapping={'approve': 0, 'deny': 0, 'abstain': 0}
unique_options_count=contract1.functions.view_unique_options_count().call()
for each_option_idx in range(unique_options_count): 
    current_option=contract1.functions._unique_options(each_option_idx).call()
    st.write(f'Option 1: {current_option} - {contract1.functions.optionId(current_option).call()}')
    
# st.write(f"Current vote count: {fake_vote_count_christmas}, You voted on the Christmas Party Celebration Proposal")

# Proposal2 in a styled box
st.markdown(
    """
    <div class="proposal-box">
        <h2>Autumn Harvest Festival Proposal</h2>
        <p>Description: Celebrate the beauty of fall at our Autumn Harvest Festival! Activities include a pumpkin patch, hayrides, and a pie-baking contest.</p>
        <p>Date: October 22nd | Time: 3 PM - 8 PM</p>
         <p><strong>How to Vote:</strong><ol>
            <li>Log into the HOA Voting Platform.</li>
            <li>Select 'Proposals'.</li>
            <li>Choose 'Autumn Harvest Festival' proposal.</li>
            <li>Use your NFT to authenticate and vote.</li>
    </div>
    """,
    unsafe_allow_html=True
)
# Dropdown for voting on the Fall Party proposal
fall_party_vote = st.selectbox(
    "Vote for the Autumn Harvest Festival Proposal",
    ["Approve", "Reject", "Abstain"],
    key="fall_party_vote"
)

# Button to vote
if st.button("Click Here To Vote", key="vote2"):
    # Call the vote function in the smart contract
    vote_option = fall_party_vote.lower()  # Convert to lowercase to match the Solidity function parameter
    try:
        # Ensure that the voting is done from the selected address
        sender_address = selected_wallet_address

        # Call the vote function in the smart contract
        transaction = contract2.functions.vote(vote_option).transact({'from': sender_address})

        st.write(f"Vote submitted from address: {sender_address}, You voted on the Autumn Harvest Festival Proposal")
    except Exception as e:
        st.write(f"Error: {str(e)}")
        
# Autumn Harvest Festival Proposal
st.markdown('<div class="proposal-box"><h2>Autumn Harvest Festival Proposal</h2><p>Autumn Harvest Festival Voting Results.</p></div>', unsafe_allow_html=True)
fake_vote_count_autumn = random.randint(0, 100)
st.progress(fake_vote_count_autumn)
st.write(f"Current vote count: {fake_vote_count_autumn}%")


# Proposal3 in a styled box
st.markdown(
    """
    <div class="proposal-box">
        <h2>Summer Party Celebration Proposal</h2>
        <p>Description: Join us for a vibrant Summer Party at the Community Pool Area! Expect a barbecue cookout, live DJ, and pool games. Fun for everyone!</p>
        <p>Date: July 15th | Time: 4 PM - 9 PM</p>
         <p><strong>How to Vote:</strong><ol>
            <li>Log into the HOA Voting Platform.</li>
            <li>Select 'Proposals'.</li>
            <li>Choose Select 'Summer Party Celebration' proposal.</li>
            <li>Vote using your NFT.</li>
    </div>
    """,
    unsafe_allow_html=True
)
# Dropdown for voting on the Summer Party proposal
summer_party_vote = st.selectbox(
    "Vote for the Summer Party Celebration Proposal",
    ["Approve", "Reject", "Abstain"],
    key="summer_party_vote"
)

if st.button("Click Here To Vote", key="vote3"):
    # Call the vote function in the smart contract
    vote_option = summer_party_vote.lower()  # Convert to lowercase to match the Solidity function parameter
    try:
        # Ensure that the voting is done from the selected address
        sender_address = selected_wallet_address

        # Call the vote function in the smart contract
        transaction = contract3.functions.vote(vote_option).transact({'from': sender_address})

        st.write(f"Vote submitted from address: {sender_address}, You voted on the Summer Party Celebration Proposal")
    except Exception as e:
        st.write(f"Error: {str(e)}")
        
# Summer Party Celebration Proposal
st.markdown('<div class="proposal-box"><h2>Summer Party Celebration Proposal</h2><p>Summer Party proposal Voting Results.</p></div>', unsafe_allow_html=True)
fake_vote_count_summer = random.randint(0, 100)
st.progress(fake_vote_count_summer)
st.write(f"Current vote count: {fake_vote_count_summer}%")

st.markdown('</div>', unsafe_allow_html=True)


st.title("HOA Voting Platform Dashboard")
#Display key metrics such as the total number of proposals, average participation, total token supply, unique token holders, and metrics like quorum and support met.
# Custom CSS for Metrics Color
# Custom CSS for Metrics Color
st.markdown(
    """
    <style>
    .metric .css-1aq6y4n { color: #D4AF37; } /* Change metric value color */
    .metric .css-1s0hp1k { color: #D4AF37; } /* Change metric label color */
    </style>
    """,
    unsafe_allow_html=True
)
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Proposals", "3")
col2.metric("Avg Participation", "7.25%")
col3.metric("Total Token Supply", "10,051")
col4.metric("Unique Token Holders", "1,000")
col5.metric("Met Quorum", "65%")


st.subheader("Tokens")
st.write("Ballot Token: 1,000 holders, 48.84% unique holders")

st.header("About Our Team")

# Example team members
team_members = [
    {"name": "Malinovsky", "role": "Financial Analyst/ Developer", "description": "Malinovsky is an Experienced software developer with 7 years of experience with crypto currency and blockchain technology.", "image": "Images/H3.png"},
    {"name": "Martinez", "role": "Financial Analyst/ Developer", "description": "Martinez is an expert in blockchain technology and has worked on numerous high-profile projects.", "image": "Images/H3.png"},
    {"name": "Nieves", "role": "Financial Analyst/ UX/UI Designer", "description": "Nieves has over 15 years of experience in project management, specializes in creating intuitive and engaging user interfaces.", "image": "Images/H3.png"},
    {"name": "Rosan", "role": "Financial Analyst/ Developer", "description": "Rosan has a strong background in marketing and public relations and is an expert in blockchain technology and has worked on numerous high-profile projects.", "image": "Images/H3.png"}
]

# Create columns
cols = st.columns(4)

# Display team members in each column
for i, member in enumerate(team_members):
    with cols[i]:
        st.image(member["image"], width=150)  # Adjust width as needed
        st.subheader(member["name"])
        # Inline HTML for custom text color for the role
        st.markdown(f"<p style='color: #FFFFFF;'>Role: {member['role']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #FFFFFF;'>{member['description']}</p>", unsafe_allow_html=True)

# Community Section
st.header("Join Our Community")
st.write("Be part of our growing HOA community of digital NFT.")
st.button("Join on Discord")
st.button("Follow on Twitter")