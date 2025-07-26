import requests
import json

# Base URL for the API
BASE_URL = "http://127.0.0.1:8000/api"

def test_lend_api():
    """Test the lending API endpoint"""
    print("=== Testing Lend API ===")
    
    # Sample loan data
    loan_data = {
        "customer_id": 1,
        "loan_amount": 10000,
        "loan_period": 2,  # 2 years
        "rate": 8.5  # 8.5% interest rate
    }
    
    try:
        response = requests.post(f"{BASE_URL}/lend/", json=loan_data)
        if response.status_code == 200:
            result = response.json()
            print("✅ Loan created successfully!")
            print(f"Loan ID: {result['loan_id']}")
            print(f"Total Amount: ${result['total_amount']:.2f}")
            print(f"Monthly EMI: ${result['emi']:.2f}")
            return result['loan_id']
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Make sure Django server is running.")
    return None

def test_payment_api(loan_id):
    """Test the payment API endpoint"""
    print("\n=== Testing Payment API ===")
    
    # Sample payment data
    payment_data = {
        "loan_id": loan_id,
        "amount": 500,
        "type": "EMI"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/payment/", json=payment_data)
        if response.status_code == 200:
            result = response.json()
            print("✅ Payment successful!")
            print(f"Message: {result['message']}")
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server.")

def test_ledger_api(loan_id):
    """Test the ledger API endpoint"""
    print(f"\n=== Testing Ledger API for Loan {loan_id} ===")
    
    try:
        response = requests.get(f"{BASE_URL}/ledger/{loan_id}/")
        if response.status_code == 200:
            result = response.json()
            print("✅ Ledger retrieved successfully!")
            print(f"EMI Amount: ${result['emi_amount']:.2f}")
            print(f"EMIs Left: {result['emi_left']}")
            print(f"Balance: ${result['balance']:.2f}")
            print("\nTransactions:")
            for transaction in result['transactions']:
                print(f"  - ${transaction['amount']:.2f} ({transaction['type']}) on {transaction['date']}")
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server.")

def test_account_overview_api(customer_id):
    """Test the account overview API endpoint"""
    print(f"\n=== Testing Account Overview for Customer {customer_id} ===")
    
    try:
        response = requests.get(f"{BASE_URL}/account/{customer_id}/")
        if response.status_code == 200:
            result = response.json()
            print("✅ Account overview retrieved successfully!")
            for loan in result:
                print(f"\nLoan ID: {loan['loan_id']}")
                print(f"Principal: ${loan['principal']:.2f}")
                print(f"Total Amount: ${loan['total_amount']:.2f}")
                print(f"Interest: ${loan['interest']:.2f}")
                print(f"EMI: ${loan['emi']:.2f}")
                print(f"Amount Paid: ${loan['amount_paid']:.2f}")
                print(f"EMIs Left: {loan['emi_left']}")
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server.")

def main():
    print("🚀 Bank Lending System API Test")
    print("=" * 50)
    
    # Test all API endpoints
    loan_id = test_lend_api()
    if loan_id:
        test_payment_api(loan_id)
        test_ledger_api(loan_id)
        test_account_overview_api(1)  # Customer ID 1
    
    print("\n" + "=" * 50)
    print("📋 Available API Endpoints:")
    print("POST /api/lend/ - Create a new loan")
    print("POST /api/payment/ - Make a payment")
    print("GET /api/ledger/<loan_id>/ - Get loan ledger")
    print("GET /api/account/<customer_id>/ - Get account overview")
    print("GET /swagger/ - API documentation")
    print("GET /admin/ - Django admin interface")

if __name__ == "__main__":
    main() 