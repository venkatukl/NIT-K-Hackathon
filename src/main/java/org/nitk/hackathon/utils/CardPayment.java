package org.nitk.hackathon.utils;

public class CardPayment implements Payment {
    private String cardNumber;
    private String expiryDate;
    private String cvv;

    public CardPayment(String cardNumber, String expiryDate, String cvv) {
        this.cardNumber = cardNumber;
        this.expiryDate = expiryDate;
        this.cvv = cvv;
    }

    @Override
    public void pay(double amount) {
        System.out.println("Paying " + amount + " using card " + cardNumber + " with expiry date " + expiryDate + " and cvv " + cvv);
    }

    @Override
    public Object copy() {
        return new CardPayment(cardNumber, expiryDate, cvv);
    }
}