from collections import deque
import heapq

class Twitter:

    def __init__(self):
        self.tweets = {}
        self.follows = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._ensure(userId)

        next_tweet_identifier = len(self.tweets[userId])
        self.tweets[userId].append((-self.timestamp, tweetId, userId, next_tweet_identifier))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self._ensure(userId)

        feed = []
        tweet_heap = []

        if self.tweets[userId]:
            heapq.heappush(tweet_heap, self.tweets[userId][-1])

        for user in self.follows[userId]:
            heapq.heappush(tweet_heap, self.tweets[user][-1])
        
        while len(feed) < 10 and tweet_heap:
            _, tweet_id, user_id, next_idx = heapq.heappop(tweet_heap)
            # print(tweet_id, user_id, next_id)
            feed.append(tweet_id)

            if next_idx > 0:
                heapq.heappush(tweet_heap, self.tweets[user_id][next_idx - 1])
        
        return feed
        



    def _ensure(self, id: int):
        if id in self.tweets:
            return
        
        self.tweets[id] = []
        self.follows[id] = set()

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        self._ensure(followerId)
        self._ensure(followeeId)

        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        self._ensure(followerId)
        self._ensure(followeeId)

        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)      
