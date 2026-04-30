import requests

def get_exchange_rate(base_currency, target_currency):
    # Example using a public API (You would need an API key for most)
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    
    try:
        response = requests.get(url)
        data = response.json()
        rate = data['rates'][target_currency]
        return rate
    except Exception as e:
        return f"Error fetching data: {e}"

# Execution
base = "USD"
target = "INR"
rate = get_exchange_rate(base, target)
print(f"Current rate: 1 {base} = {rate} {target}")
