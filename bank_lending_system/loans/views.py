from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer, Loan, Payment
from django.shortcuts import get_object_or_404

def calculate_loan(principal, rate, period):
    interest = principal * rate * period / 100
    total = principal + interest
    emi = total / (period * 12)
    return interest, total, emi

class LendView(APIView):
    def post(self, request):
        customer_id = request.data["customer_id"]
        P = float(request.data["loan_amount"])
        N = int(request.data["loan_period"])
        R = float(request.data["rate"])

        interest, total, emi = calculate_loan(P, R, N)
        loan = Loan.objects.create(
            customer_id=customer_id,
            principal=P,
            rate=R,
            period=N,
            interest=interest,
            total_amount=total,
            emi=emi
        )
        return Response({"loan_id": loan.id, "total_amount": total, "emi": emi})

class PaymentView(APIView):
    def post(self, request):
        loan = get_object_or_404(Loan, id=request.data["loan_id"])
        amt = float(request.data["amount"])
        ptype = request.data["type"]
        Payment.objects.create(loan=loan, amount=amt, type=ptype)
        return Response({"message": "Payment successful"})

class LedgerView(APIView):
    def get(self, request, loan_id):
        loan = get_object_or_404(Loan, id=loan_id)
        payments = loan.payments.all()
        paid = sum(p.amount for p in payments)
        remaining = loan.total_amount - paid
        emi_left = max(int(remaining / loan.emi), 0)

        return Response({
            "transactions": [{"amount": p.amount, "type": p.type, "date": p.paid_at} for p in payments],
            "emi_amount": loan.emi,
            "emi_left": emi_left,
            "balance": remaining
        })

class AccountOverview(APIView):
    def get(self, request, customer_id):
        loans = Loan.objects.filter(customer_id=customer_id)
        overview = []

        for loan in loans:
            paid = sum(p.amount for p in loan.payments.all())
            remaining = loan.total_amount - paid
            emi_left = max(int(remaining / loan.emi), 0)
            overview.append({
                "loan_id": loan.id,
                "principal": loan.principal,
                "total_amount": loan.total_amount,
                "interest": loan.interest,
                "emi": loan.emi,
                "amount_paid": paid,
                "emi_left": emi_left
            })

        return Response(overview)
