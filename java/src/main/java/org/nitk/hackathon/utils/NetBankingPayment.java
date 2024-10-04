package org.nitk.hackathon.utils;

public class NetBankingPayment implements Payment {
    private String gatewayName;
    private String accountNumber;
    private PaymentGateway paymentGateway;

    public NetBankingPayment(String gatewayName, String accountNumber) {
        this.gatewayName = gatewayName;
        this.accountNumber = accountNumber;        
    }

    @Override
    public void pay(double amount) {
        if(null == paymentGateway) {
            paymentGateway = new PaymentGateway(gatewayName, accountNumber);
        }
        paymentGateway.pay(amount);
        System.out.println("Paid " + amount + " via Net Banking");
    }

    @Override
    public Object copy() {
        return null;
    }
}