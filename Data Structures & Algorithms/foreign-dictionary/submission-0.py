class Solution:
    def check_invalid_prefix(self, left: str, right: str):
        m, n = len(left), len(right)
        m_idx, n_idx = 0, 0

        while m_idx < m and n_idx < n:
            if left[m_idx] != right[n_idx]:
                return False
            m_idx += 1
            n_idx += 1
        
        return len(left) > len(right)

    def find_edge(self, left: str, right: str):
        m, n = len(left), len(right)
        m_idx, n_idx = 0, 0

        while m_idx < m and n_idx < n:
            if left[m_idx] != right[n_idx]:
                return (left[m_idx], right[n_idx])
            m_idx += 1
            n_idx += 1
        
        if len(left) > len(right):
            return None

        return None
    
    def foreignDictionary(self, words: List[str]) -> str:
        alphabet = set()

        for word in words:
            for char in word:
                alphabet.add(char)

        neighbours = {x: [] for x in alphabet}
        in_degrees = {x: 0 for x in alphabet}
        n = len(words)
        
        for i in range(n - 1):
            if self.check_invalid_prefix(words[i], words[i + 1]):
                return ""

            edge = self.find_edge(words[i], words[i + 1])

            if edge:
                left, right = edge
                neighbours[left].append(right)
                in_degrees[right] += 1
        
        res = []
        queue = [x for x in in_degrees if in_degrees[x] == 0]

        while queue:
            next_queue = []

            for char in queue:
                res.append(char)

                for neighbour in neighbours[char]:
                    in_degrees[neighbour] -= 1
                    if in_degrees[neighbour] == 0:
                        next_queue.append(neighbour)
            
            queue = next_queue
        
        return "" if len(res) != len(alphabet) else "".join(res)



