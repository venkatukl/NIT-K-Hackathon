package org.nitk.hackathon.account;

import java.util.ArrayList;
import java.util.List;

public class NewAccount implements Account {
    private List<Account> accounts;

    public NewAccount() {
        this.accounts = new ArrayList<>();
    }

    public NewAccount(List<Account> accounts) {
        this.accounts = accounts;
    }

    public void addAccount(Account account) {
        accounts.add(account);
    }

    @Override
    public String getAccountNumber() {
        return "New-Acct-Num";
    }

    @Override
    public void deposit(double amount) {
        for (Account account : accounts) {
            account.deposit(amount);
        }
    }

    @Override
    public void withdraw(double amount) {
        for (Account account : accounts) {
            account.withdraw(amount);
        }
    }

    @Override
    public double getBalance() {
        double balance = 0;
        for (Account account : accounts) {
            balance += account.getBalance();
        }
        return balance;
    }
}