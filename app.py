import streamlit as st
from data.historical_data import get_historical_data
from data.gemini_api import get_real_time_price
from services.sentiment_analysis import analyze_sentiment

# Streamlit UI
st.title("Real-Time Stock and Sentiment Analysis Dashboard")

# Input for stock symbol
symbol = st.text_input("Enter stock symbol:", value="BTCUSD")

# Display Real-Time Stock Price
if symbol:
    st.header("Real-Time Stock Price")
    real_time_data = get_real_time_price(symbol)
    if real_time_data:
        st.write(f"Last Price: ${real_time_data['last']}")
        st.write(f"24hr Volume: {real_time_data['volume']['BTC']}")
    else:
        st.write("Error retrieving data from Gemini API.")

# Display Historical Stock Data
st.header("Historical Data")
historical_data = get_historical_data(symbol)
if historical_data:
    st.write("Historical Price Data:")
    for data in historical_data:
        st.write(f"Date: {data['date']}, Price: ${data['price']}")
else:
    st.write("No historical data found for this symbol.")

# Sentiment Analysis
st.header("Sentiment Analysis")
if historical_data:
    for data in historical_data:
        sentiment = analyze_sentiment(data['text'])
        st.write(f"Date: {data['date']}, Sentiment: {sentiment}")
