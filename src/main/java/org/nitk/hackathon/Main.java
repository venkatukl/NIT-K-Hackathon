package org.nitk.hackathon;

import org.nitk.hackathon.account.AccountDTO;
import org.nitk.hackathon.bank.TestBank;
import org.nitk.hackathon.stock.StocksList;
import org.nitk.hackathon.trader.LogTraders;
import org.nitk.hackathon.trader.NotifyTraders;
import org.nitk.hackathon.trader.Trader;
import org.nitk.hackathon.trader.Trader2;

public class Main {
    public static void main(String[] args) {
        System.out.println("NIT-K Hackathon");

        TestBank testBank = TestBank.getTestBank();
        testBank.sendMessages();

        Trader trader = new Trader2();
        Trader logBrokerTraders = new LogTraders(trader);
        Trader notifyTraders = new NotifyTraders(logBrokerTraders);

        StocksList stocksList = StocksList.getObject();
        stocksList.registerTrader(notifyTraders);
        stocksList.updatePrice("XYZ", 50.0);
        

        AccountDTO account = AccountDTO.ceator().accountNumber("123").accountType("Savings").name("Test Name").email("dLbX9@example.com").create();
        System.out.println("Account created - "+ account);
    }
}