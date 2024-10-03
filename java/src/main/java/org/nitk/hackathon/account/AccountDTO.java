package org.nitk.hackathon.account;

public class AccountDTO {

private String accountNumber;
private String name;
private String accountType;
private String email;

private AccountDTO() {

}

public static AccountDTOCreator ceator() {
    return new AccountDTOCreator();
}

public static class AccountDTOCreator {
    private String accountNumber;
    private String name;
    private String accountType;
    private String email;

    public AccountDTOCreator accountNumber(String accountNumber) {
        this.accountNumber = accountNumber;
        return this;
    }

    public AccountDTOCreator name(String name) {
        this.name = name;
        return this;
    }

    public AccountDTOCreator accountType(String accountType) {
        this.accountType = accountType;
        return this;
    }

    public AccountDTOCreator email(String email) {
        this.email = email;
        return this;
    }

    public AccountDTO create() {
        return new AccountDTO(this);
    }
}

}