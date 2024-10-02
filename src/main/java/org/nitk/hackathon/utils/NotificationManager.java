package org.nitk.hackathon.utils;

public class NotificationManager implements Notification {
    private String name;
    public NotificationManager(String name) {
        this.name = name;
    }
    @Override
    public void send(String message) {
        System.out.println(name + ": got message : " + message);
    }
}