package org.nitk.hackathon.utils;

public class PaymentProcessor {
    public Payment processPayment(String type, double amount) {
        Payment paymentChannel = null;
        if(type.equals("credit")) {
            System.out.println("Processing credit payment for amount "+ amount);
            paymentChannel = new CardPayment("1234-5678-9012-3456", "12/24", "123");
            paymentChannel.pay(amount);
        } else if(type.equals("debit")) {
            System.out.println("Processing debit payment for amount "+ amount);
            paymentChannel = new CardPayment("9876-5421-8524-6523", "11/25", "893");
            paymentChannel.pay(amount);
        } else if(type.equals("netbanking")) {
            System.out.println("Processing netbanking payment for amount "+ amount);
            paymentChannel = new NetBankingPayment("HDFC", "1234567890");
            paymentChannel.pay(amount);
        } else if(type.equals("upi")) {
            System.out.println("Processing UPI payment for amount "+ amount);
            paymentChannel = new UPIPayment("customer@upi");
            paymentChannel.pay(amount);
            UPIPayment newPayment = (UPIPayment) paymentChannel.copy();
            newPayment.setUpiId("dummy@upi");
            newPayment.pay(amount*0.02);
        } else {
            System.out.println("Unknown Payment option");
        }
    }
}