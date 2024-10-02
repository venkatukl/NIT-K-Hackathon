package org.nitk.hackathon.account;

public class Savings implements Account {

    private String accountNumber;
    private double balance;

    public Savings(String accountNumber) {
        this.accountNumber = accountNumber;
        this.balance = 0;
    }

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