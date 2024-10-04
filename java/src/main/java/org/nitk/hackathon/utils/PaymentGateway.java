package org.nitk.hackathon.utils;

public class PaymentGateway implements Payment {
    private string gatewayName;
    private string accountNumber;
    public PaymentGateway(string gatewayName, string accountNumber) {
        this.gatewayName = gatewayName;
        this.accountNumber = accountNumber;
    }

    @Override
    public Object copy() {
        return new PaymentGateway(this.gatewayName, this.accountNumber);
    }
    
    @Override
    public void pay(double amount) {
        //logic
    }
}