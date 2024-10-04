package org.nitk.hackathon.bank;

import org.nitk.hackathon.account.Account;

public class TxnManager {
    private Transaction transaction;
    public void setTransaction(final Transaction transaction) {
        this.transaction = transaction;
    }
    public void executeTransaction(Account account, double amount) {
        transaction.execute(account, amount);
    }
}