package org.nitk.hackathon.utils;

public class Cart {
    private PaymentManager paymentManager;
    public Cart(PaymentManager paymentManager) {
        this.paymentManager = paymentManager;
    }
    public void checkout(double amount) {
        paymentManager.pay(amount);
    }
}