package org.nitk.hackathon.trader;

public class TraderParent implements Trader {
    private Trader trader;
    public TraderParent(Trader trader) {
        this.trader = trader;
    }
    @Override
    public void update(String stock, double price) {
        trader.update(stock, price);
    }
}