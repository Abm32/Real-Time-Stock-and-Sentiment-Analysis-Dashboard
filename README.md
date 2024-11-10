# Real-Time Stock and Sentiment Analysis Dashboard

This project is a dashboard for real-time stock and sentiment analysis using Streamlit, Gemini API, MongoDB Atlas, and TextBlob. It enables users to view real-time stock prices, retrieve historical data, and perform sentiment analysis on market sentiment.

## Setup Instructions

1. **Install Requirements**: Run `pip install -r requirements.txt`.
2. **Configure Environment Variables**:
   - Create a `.env` file with your API keys.
   - Example:
     ```
     GEMINI_API_KEY=your_gemini_api_key
     MONGODB_URI=your_mongodb_connection_uri
     ```

3. **Run the App**: Launch the app with:
   ```bash
   streamlit run app.py
