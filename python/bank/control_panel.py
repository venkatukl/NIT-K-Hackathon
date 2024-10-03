
import time


class State:
    CLOSED, OPEN, HALF_OPEN = range(3)

class ControlPanel:
    def __init__(self):
        self.state = State.CLOSED
        self.failure_count = 0
        self.failure_threshold = 3
        self.open_state_timeout = 1000  # milliseconds
        self.last_failure_time = 0

    def allow_request(self):
        if self.state == State.OPEN:
            if (time.time() - self.last_failure_time) * 1000 > self.open_state_timeout:
                self.state = State.HALF_OPEN
                return True
            return False
        return True

    def record_success(self):
        self.state = State.CLOSED
        self.failure_count = 0

    def record_failure(self):
        self.failure_count += 1
        if self.failure_count >= self.failure_threshold:
            self.state = State.OPEN
            self.last_failure_time = time.time()
