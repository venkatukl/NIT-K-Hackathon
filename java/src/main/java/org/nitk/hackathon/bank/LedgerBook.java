package org.nitk.hackathon.bank;

public class LedgerBook {
    private double amount;
    private String accountNumber;

    public LedgerBook(String accountNumber) {
        this.accountNumber = accountNumber;
        this.amount = 0;
    }

    public void updateLedger(double amount, String accountNumber) {
        //logic
    }

    public double getBalance() {
        return amount;
    }
    
    public String getAccountNumber() {
        return accountNumber;
    }
}