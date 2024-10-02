package org.nitk.hackathon.bank;

import org.nitk.hackathon.account.Account;

public class WithdrawAmount implements Transaction {
    @Override
    public void execute(Account account, double amount) {
        account.withdraw(amount);
    }
}