package org.nitk.hackathon.utils;

public class UPIPayment implements Payment {
    private String upiId;
    public UPIPayment(String upiId) {
        this.upiId = upiId;
    }

    @Override
    public void pay(double amount) {
        //logic
    }

    @Override
    public Payment copy() {
        return new UPIPayment(upiId);
    }

    public void setUpiId(String upiId) {
        this.upiId = upiId;
    }

}