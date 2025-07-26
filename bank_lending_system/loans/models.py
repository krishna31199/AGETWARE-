from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)

class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    principal = models.FloatField()
    rate = models.FloatField()
    period = models.IntegerField()
    interest = models.FloatField()
    total_amount = models.FloatField()
    emi = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class Payment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='payments')
    amount = models.FloatField()
    type = models.CharField(max_length=10, choices=[('EMI', 'EMI'), ('LUMP', 'LUMP')])
    paid_at = models.DateTimeField(auto_now_add=True)
