# Bank Lending System - Output Summary

## 🚀 System Status: RUNNING

The Django development server is running on `http://127.0.0.1:8000/`

## 📊 Database Contents

### Customers
- **ID 1**: John Doe
- **ID 2**: Jane Smith

### Loans
- **Loan ID 1**: 
  - Customer: John Doe
  - Principal: $10,000.00
  - Interest Rate: 8.5%
  - Period: 2 years
  - Total Amount: $11,700.00
  - Monthly EMI: $487.50

### Payments
- **Payment ID 1**:
  - Loan: 1
  - Amount: $500.00
  - Type: EMI
  - Date: 2025-07-26T07:18:58.734979Z

## 🔗 Available API Endpoints

### 1. Create Loan
- **URL**: `POST /api/lend/`
- **Sample Request**:
```json
{
    "customer_id": 1,
    "loan_amount": 10000,
    "loan_period": 2,
    "rate": 8.5
}
```
- **Sample Response**:
```json
{
    "loan_id": 1,
    "total_amount": 11700.0,
    "emi": 487.5
}
```

### 2. Make Payment
- **URL**: `POST /api/payment/`
- **Sample Request**:
```json
{
    "loan_id": 1,
    "amount": 500,
    "type": "EMI"
}
```
- **Sample Response**:
```json
{
    "message": "Payment successful"
}
```

### 3. Get Loan Ledger
- **URL**: `GET /api/ledger/<loan_id>/`
- **Sample Response**:
```json
{
    "transactions": [
        {
            "amount": 500.0,
            "type": "EMI",
            "date": "2025-07-26T07:18:58.734979Z"
        }
    ],
    "emi_amount": 487.5,
    "emi_left": 22,
    "balance": 11200.0
}
```

### 4. Get Account Overview
- **URL**: `GET /api/account/<customer_id>/`
- **Sample Response**:
```json
[
    {
        "loan_id": 1,
        "principal": 10000.0,
        "total_amount": 11700.0,
        "interest": 1700.0,
        "emi": 487.5,
        "amount_paid": 500.0,
        "emi_left": 22
    }
]
```

## 🌐 Web Interfaces

### 1. API Documentation (Swagger)
- **URL**: `http://127.0.0.1:8000/swagger/`
- Interactive API documentation with testing interface

### 2. Django Admin
- **URL**: `http://127.0.0.1:8000/admin/`
- Database management interface

## 📈 Test Results

### ✅ Loan Creation Test
- Successfully created a $10,000 loan for John Doe
- 2-year term at 8.5% interest rate
- Total amount: $11,700
- Monthly EMI: $487.50

### ✅ Payment Processing Test
- Successfully processed $500 EMI payment
- Payment recorded in database

### ✅ Ledger Generation Test
- Current balance: $11,200
- EMIs remaining: 22
- Transaction history displayed

### ✅ Account Overview Test
- Complete loan details retrieved
- Payment history and remaining balance calculated

## 🛠️ System Features

1. **Loan Management**: Create loans with principal, interest rate, and period
2. **Payment Processing**: Record EMI and lump sum payments
3. **Ledger Generation**: Track all transactions and calculate remaining balance
4. **Account Overview**: Complete customer loan portfolio view
5. **RESTful API**: JSON-based API for all operations
6. **Documentation**: Swagger UI for API testing
7. **Admin Interface**: Django admin for database management

## 🔧 Technical Stack

- **Backend**: Django 4.x with Django REST Framework
- **Database**: SQLite3
- **API Documentation**: drf-yasg (Swagger)
- **Authentication**: None (for demo purposes)
- **Server**: Django Development Server

## 📝 Usage Instructions

1. **Start Server**: `python manage.py runserver`
2. **Test API**: Run `python test_api.py`
3. **View Documentation**: Visit `http://127.0.0.1:8000/swagger/`
4. **Manage Data**: Visit `http://127.0.0.1:8000/admin/`

## 🎯 Key Calculations

- **Interest**: Principal × Rate × Period / 100
- **Total Amount**: Principal + Interest
- **Monthly EMI**: Total Amount / (Period × 12)
- **Remaining Balance**: Total Amount - Sum of all payments
- **EMIs Left**: Remaining Balance / Monthly EMI

The system is fully functional and ready for use! 🎉 