package org.nitk.hackathon.trader;

public class NotifyTraders extends TraderParent {
    public NotifyTraders(Trader trader) {
        super(trader);
    }

    @Override
    public void update(String stock, double price) {
        trader.update(stock, price);
        notifyUpdate(stock, price);
    }

    private void notifyUpdate(String stock, double price) {
        System.out.println("Trader " + trader.getClass().getSimpleName() + " updated " + stock + " to " + price);
    }
}