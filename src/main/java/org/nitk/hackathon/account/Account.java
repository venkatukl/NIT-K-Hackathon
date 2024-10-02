package org.nitk.hackathon.account;

public interface Account {
    void deposit(double amount);
    void withdraw(double amount);
    double getBalance();
    String getAccountNumber();
}