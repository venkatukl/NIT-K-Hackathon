package org.nitk.hackathon.bank;

import org.nitk.hackathon.account.Account;
import org.nitk.hackathon.utils.Notification;

import java.util.ArrayList;
import java.util.List;

public class TestBank {

    private static TestBank instance;
    private List<Account> accounts;
    private List<Notification> notifyList;
    private final ControlPanel controlPanel;

    private TestBank() {
        accounts = new ArrayList<>();
        notifyList = new ArrayList<>();
        controlPanel = new ControlPanel(this);
    }

    public static TestBank getTestBank() {
        if (instance == null) {
            instance = new TestBank();
        }
        return instance;
    }

    public void addAccount(Account account) {
        accounts.add(account);
    }

    public void addTransaction(Account account, double amount,Transaction txn) {
        if(controlPanel.allowRequest()) {
            try{
                txn.execute(account, amount);
                sendMessage(account);
                controlPanel.recordSuccess();
            } catch (Exception e) {
                controlPanel.recordFailure();
                System.out.println("Transaction failed: " + e.getMessage());
            }
        } else {
            System.out.println("Transaction rejected");
        }
    }

    public void addNotification(Notification notification) {
        notifyList.add(notification);
    }

    public void removeNotification(Notification notification) {
        notifyList.remove(notification);
    }

    public void sendNotification(String message) {
        for (Notification notification : notifyList) {
            notification.send(message);
        }
    }

    public double getBalance(Account account) {
        return account.getBalance();
    }

    private void sendMessage(Account account) {
        sendNotification("Balance updated for account " + account.getAccountNumber() + ": $" + account.getBalance());
    }

    public void sendMessages(){
        for (Account account : accounts) {
            sendMessage(account);
        }
    }

}