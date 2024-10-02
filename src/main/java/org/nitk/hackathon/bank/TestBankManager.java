package org.nitk.hackathon.bank;

import org.nitk.hackathon.account.Account;

public class TestBankManager {
    private TestBank bank;

    public TestBankManager(TestBank bank) { 
        this.bank = bank;
    }

    public void depositAccount(Account account, double amount) {
        bank.addTransaction(account, amount, new DepositAmount());
    }

    public void withdrawAccount(Account account, double amount) {
        bank.addTransaction(account, amount, new WithdrawAmount());
    }

    public void getBalance(Account account) {
        bank.getBalance(account);
    }
}