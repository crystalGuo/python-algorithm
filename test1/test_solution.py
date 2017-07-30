from unittest import TestCase
from Solution import Solution
class TestSolution(TestCase):
    def test_should_create_bucket(self):
        bucket = Solution.createBucket()
        self.assertEqual(len(bucket.keys()), 26)
        self.assertEqual(bucket['a'], 0)
        self.assertEqual(bucket['z'], 0)

    def test_should_init_p_bucket(self):
        bucket = Solution.initBucket("abcc")
        self.assertEqual(bucket['a'], 1)
        self.assertEqual(bucket['b'], 1)
        self.assertEqual(bucket['c'], 2)

    def test_should_init_s_0(self):
        s = "accd"
        lenP = 3
        bucket = Solution.initialS(s, lenP)
        self.assertEqual(bucket['a'], 1)
        self.assertEqual(bucket['c'], 2)

    def test_should_move_s_to_next(self):
        s = "abcce"
        lenP = 2
        bucketS = Solution.createBucket()
        bucketS['b'] = 1
        bucketS['c'] = 1
        idx = 1
        Solution.move(bucketS, s, idx, lenP)
        self.assertEqual(bucketS['b'], 0)
        self.assertEqual(bucketS['c'], 2)
    def test_should_return_true_if_two_bucket_are_same(self):
        bucketS = Solution.createBucket()
        bucketP = Solution.createBucket()
        bucketS['a'] = 2
        bucketP['a'] = 2
        result = Solution.judgeBucket(bucketS, bucketP);
        self.assertTrue(result)
    def test_should_return_result(self):
        S = 'abab'
        P = 'ab'
        expectResult = [0, 1, 2]
        result = Solution.getResult(S, P)
        self.assertEqual(result, expectResult)
    def test_should_return_result1(self):
        S = 'cbaebabacd'
        P = 'abc'
        expectResult = [0, 6]
        result = Solution.getResult(S, P)
        self.assertEqual(result, expectResult)



