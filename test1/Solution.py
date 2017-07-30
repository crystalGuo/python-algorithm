class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        return self.getResult(s,p)

    @classmethod
    def createBucket(cls):
        bucket = {}
        for i in range(26):
            bucket[chr(i+97)] = 0
        return bucket

    @classmethod
    def initBucket(cls, init):
        bucket = cls.createBucket()
        for i in range(len(init)):
            bucket[init[i]] += 1

        return bucket

    @classmethod
    def initialS(cls, s, lenP):
        return cls.initBucket(s[0:lenP])

    @classmethod
    def move(cls, bucket, s, index, lenP):
        bucket[s[index]] -= 1
        bucket[s[index+lenP]] += 1
        return bucket

    @classmethod
    def judgeBucket(cls, bucketS, bucketP):
        for i in range(26):
            if bucketS[chr(i+97)]!=bucketP[chr(i+97)]:
                return False
        return True

    @classmethod
    def getResult(cls, S, P):
        bucketP = cls.initBucket(P)
        bucketS = cls.initialS(S, len(P))
        result = []
        for i in range(len(S)-len(P) + 1):
            if cls.judgeBucket(bucketP, bucketS):
                result.append(i)
            if (i + len(P) < len(S)):
                bucketS = cls.move(bucketS, S, i, len(P))
        return result


