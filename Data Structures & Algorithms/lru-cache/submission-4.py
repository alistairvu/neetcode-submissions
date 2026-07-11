class LogEntry:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.log_head = None
        self.log_tail = None
        self.cache = {}

    def handle_log(self, log_entry: LogEntry):
        prev_entry = log_entry.prev
        next_entry = log_entry.next
    
        # Remove from linked list
        if prev_entry == None:
            self.log_head = next_entry
        else:
            prev_entry.next = next_entry
        
        if next_entry:
            next_entry.prev = prev_entry
        else:
            self.log_tail = prev_entry
        
        log_entry.prev = self.log_tail

        if self.log_tail:
            self.log_tail.next = log_entry
        
        if not self.log_head:
            self.log_head = log_entry
        
        log_entry.next = None
        self.log_tail = log_entry


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        value, log_entry = self.cache[key]
        self.handle_log(log_entry)
        return value

    def put(self, key: int, value: int) -> None:        
        if key in self.cache:
            _, log_entry = self.cache[key]
            self.handle_log(log_entry)
            self.cache[key] = (value, log_entry)
            return
        
        log_entry = LogEntry(key)

        if self.log_tail == None:
            self.log_head = log_entry
        else:
            self.log_tail.next = log_entry
            log_entry.prev = self.log_tail
        
        self.log_tail = log_entry
        self.cache[key] = (value, log_entry)


        if len(self.cache) > self.capacity:
            head_entry = self.log_head
            
            if head_entry.next:
                head_entry.next.prev = None

            self.log_head = self.log_head.next
            del self.cache[head_entry.val]
