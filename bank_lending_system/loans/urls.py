from django.urls import path
from .views import LendView, PaymentView, LedgerView, AccountOverview

urlpatterns = [
    path("lend/", LendView.as_view()),
    path("payment/", PaymentView.as_view()),
    path("ledger/<int:loan_id>/", LedgerView.as_view()),
    path("account/<int:customer_id>/", AccountOverview.as_view()),
]
