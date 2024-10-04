package org.nitk.hackathon.trader;

public class TraderGroup1 implements Trader {
    @Override
    public void update(String stock, double price) {
        System.out.println("TraderGroup1 updated " + stock + " to " + price);
    }
}