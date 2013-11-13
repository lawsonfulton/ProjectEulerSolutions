def is_palindrome(x):
    s = str(x)
    n = len(s)
    
    for i in xrange(n):
        if s[i] != s[n - 1 - i]:
            return False
    
    return True
    
def largest_palindrome_product():
    l = []
    
    for i in xrange(999, 99, -1):
            for j in xrange(999, 99, -1):
                if is_palindrome(i*j):
                    l.append(i*j)
    
    return max(l)
                    
if __name__ == "__main__":
    print largest_palindrome_product()
    
