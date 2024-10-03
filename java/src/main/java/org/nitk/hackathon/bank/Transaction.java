package org.nitk.hackathon.bank;

import org.nitk.hackathon.account.Account;

public interface Transaction {
    void execute(Account account, double amount);
}
