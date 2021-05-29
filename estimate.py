import math
import unittest
import random

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
            
            
def wallis(n):
    i = 1
    val = 1
    tot = 1
    while i <= n:
        val = (4 * i * i) / ((4 * i * i) - 1)
        tot = tot*val
        i = i + 1
    return 2*tot
def monte_carlo(n):
    i=1
    inspoint = 0
    while i<=n:
        x= random.random()
        y= random.random()
        distance = math.sqrt((x** 2) + (y** 2))
        if distance<1:
            inspoint = inspoint+1
        i = i + 1
    val=4*(inspoint/n)
    return val
        
        
           
        
    
if __name__ == "__main__":
    unittest.main()
