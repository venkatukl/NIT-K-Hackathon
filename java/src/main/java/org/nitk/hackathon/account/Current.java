package org.nitk.hackathon.account;

public class Current implements Account {
    private String accountNumber;
    private double balance;

    public Current(String accountNumber) {
        this.accountNumber = accountNumber;
        this.balance = 0;
    }

    @Override
    public String getAccountNumber() {
        return accountNumber;
    }

    @Override
    public void deposit(double amount) {
        balance += amount;
    }

    @Override
    public void withdraw(double amount) {
        balance -= amount;
    }

    @Override
    public double getBalance() {
        return balance;
    }

}