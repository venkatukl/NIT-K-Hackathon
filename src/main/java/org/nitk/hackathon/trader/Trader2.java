package org.nitk.hackathon.trader;

public class Trader2 implements Trader {

    @Override
    public void update(String stock, double price) {
        System.out.println("Trader 2 updated " + stock + " to " + price);
    }
}
