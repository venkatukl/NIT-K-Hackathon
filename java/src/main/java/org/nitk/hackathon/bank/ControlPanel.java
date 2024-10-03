package org.nitk.hackathon.bank;

public class ControlPanel {
    private enum State { CLOSED, OPEN, HALF_OPEN}

    private State state = State.CLOSED;

    private int failureCount = 0;
    private int failureThreshold = 3;
    private long openStateTimeout = 1000;
    private long lastFailureTime = 0;

    public synchronized boolean allowRequest() {
        if (state == State.OPEN) {
            if(System.currentTimeMillis() - lastFailureTime > openStateTimeout) {
                state = State.HALF_OPEN;
                return true;
            }
            return false;
        }
        return true;
    }

    public synchronized void recordSuccess() {
       state = State.CLOSED;
       failureCount = 0;
    }

    public synchronized void recordFailure() {
        failureCount++;
        if(failureCount >= failureThreshold) {
            state = State.OPEN;
            lastFailureTime = System.currentTimeMillis();
        }
    }
}
