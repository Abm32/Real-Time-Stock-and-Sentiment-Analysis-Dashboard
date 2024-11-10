def format_price(price):
    # Format price to 2 decimal places
    return f"${price:,.2f}"

def format_date(date_string):
    # Example date formatting function
    from datetime import datetime
    return datetime.strptime(date_string, "%Y-%m-%d").strftime("%b %d, %Y")
