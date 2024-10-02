package org.nitk.hackathon.bank;

import org.nitk.hackathon.account.Account;

public class LedgerSystem implements Account {
    private LedgerBook ledger;

    public LedgerSystem(LedgerBook ledger) {
        this.ledger = ledger;
    }

    public void deposit(double amount) {
        ledger.updateLedger(amount, "DEPOSIT");
    }

    public void withdraw(double amount) {
        ledger.updateLedger(-amount, "WITHDRAWAL");
    }

    public double getBalance() {
        return ledger.getBalance();
    }

    public String getAccountNumber() {
        return "LEDGER";
    }
}