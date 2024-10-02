package org.nitk.hackathon.bank;

import org.nitk.hackathon.account.Account;

public class DefaultAccount implements Transaction {
    @Override
    public void execute(Account account, double amount) {
        account.deposit(amount);
    }
}