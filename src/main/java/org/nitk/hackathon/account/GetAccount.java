package org.nitk.hackathon.account;

public static Account getAccount(String accountType, String accountNumber) {
    if(accountType.equals("Savings")) {
        return new Savings(accountNumber);
    } else if(accountType.equals("Current")) {
        return new Current(accountNumber);
    } else {
        return null;
    }
}