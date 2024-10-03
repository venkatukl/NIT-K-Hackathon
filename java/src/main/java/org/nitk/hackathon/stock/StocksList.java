package org.nitk.hackathon.stock;

import org.nitk.hackathon.trader.Trader;

import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;

public class StocksList {

    private static StocksList instance;
    private List<Trader> traders = new ArrayList<>();
    private Map<String, Double> stocks = new HashMap<>();

    private StocksList() {
        // Initialize stocks with some initial values
        stocks.put("ABC", 100.0);
        stocks.put("XYZ", 50.0);
    }

    public static StocksList getObject() {    
        if (instance == null) {
            instance = new StocksList();
        }
        return instance;
    }

    public void registerTrader(Trader trader) {
        traders.add(trader);
    }

    public void updatePrice(String stock, double price) {
        stocks.put(stock, price);
        notifyTraders(stock, price);
    }

    private void notifyTraders(String stock, double price) {
        for (Trader trader : traders) {
            trader.update(stock, price);
        }
    }

}