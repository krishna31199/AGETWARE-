import React, { useState } from 'react';
import { CreditCard, CheckCircle } from 'lucide-react';
import { useCart } from '../../contexts/CartContext';

export function CartSummary() {
  const { totalPrice, totalItems, clearCart } = useCart();
  const [isProcessingCheckout, setIsProcessingCheckout] = useState(false);
  const [checkoutComplete, setCheckoutComplete] = useState(false);

  const shipping = totalPrice > 50 ? 0 : 9.99;
  const tax = totalPrice * 0.1;
  const finalTotal = totalPrice + shipping + tax;

  const handleCheckout = async () => {
    setIsProcessingCheckout(true);
    
    // Simulate checkout process
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    setIsProcessingCheckout(false);
    setCheckoutComplete(true);
    
    // Clear cart after successful checkout
    setTimeout(() => {
      clearCart();
      setCheckoutComplete(false);
    }, 3000);
  };

  if (checkoutComplete) {
    return (
      <div className="bg-white rounded-xl border border-gray-100 p-6 text-center">
        <div className="flex flex-col items-center space-y-4">
          <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center">
            <CheckCircle className="h-8 w-8 text-green-600" />
          </div>
          <h3 className="text-xl font-semibold text-gray-900">Order Confirmed!</h3>
          <p className="text-gray-600">Thank you for your purchase. Your order is being processed.</p>
          <div className="text-sm text-gray-500">
            Order Total: ${finalTotal.toFixed(2)}
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-xl border border-gray-100 p-6 sticky top-24">
      <h2 className="text-lg font-semibold text-gray-900 mb-4">Order Summary</h2>
      
      <div className="space-y-3 mb-6">
        <div className="flex justify-between text-sm">
          <span className="text-gray-600">Subtotal ({totalItems} items)</span>
          <span className="font-medium">${totalPrice.toFixed(2)}</span>
        </div>
        
        <div className="flex justify-between text-sm">
          <span className="text-gray-600">Shipping</span>
          <span className="font-medium">
            {shipping === 0 ? (
              <span className="text-green-600">Free</span>
            ) : (
              `$${shipping.toFixed(2)}`
            )}
          </span>
        </div>
        
        <div className="flex justify-between text-sm">
          <span className="text-gray-600">Tax</span>
          <span className="font-medium">${tax.toFixed(2)}</span>
        </div>
        
        <div className="border-t border-gray-200 pt-3">
          <div className="flex justify-between text-lg font-semibold">
            <span>Total</span>
            <span className="text-blue-600">${finalTotal.toFixed(2)}</span>
          </div>
        </div>
      </div>

      {totalPrice > 0 && totalPrice < 50 && (
        <div className="bg-amber-50 border border-amber-200 rounded-lg p-3 mb-4">
          <p className="text-sm text-amber-800">
            Add ${(50 - totalPrice).toFixed(2)} more for free shipping!
          </p>
        </div>
      )}

      <button
        onClick={handleCheckout}
        disabled={totalItems === 0 || isProcessingCheckout}
        className="w-full bg-blue-600 text-white py-3 px-4 rounded-xl font-medium hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors duration-200 flex items-center justify-center space-x-2"
      >
        {isProcessingCheckout ? (
          <>
            <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white"></div>
            <span>Processing...</span>
          </>
        ) : (
          <>
            <CreditCard className="h-4 w-4" />
            <span>Proceed to Checkout</span>
          </>
        )}
      </button>

      <p className="text-xs text-gray-500 text-center mt-3">
        This is a demo checkout. No actual payment will be processed.
      </p>
    </div>
  );
}