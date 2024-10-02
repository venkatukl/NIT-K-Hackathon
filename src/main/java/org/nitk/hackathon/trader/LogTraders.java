package org.nitk.hackathon.trader;

public class LogTraders extends TraderParent {
    public LogTraders(Trader trader) {
        super(trader);
    }

    @Override
    public void update(String stock, double price) {
        super.update(stock, price);
        logUpdate(stock, price);
    }

    private void logUpdate(String stock, double price) {
        System.out.println("Trader " + trader.getClass().getSimpleName() + " updated " + stock + " to " + price);
    }
}