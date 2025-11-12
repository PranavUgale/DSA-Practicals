# 6. Given: l A text string text of length n. l A pattern string pattern of length m. Objective: 
# Find all starting indices i in the text such that the substring text[i:i+m] is exactly equal to the 
# pattern pattern, using the Naive String Matching Algorithm approach. Constraints: l 0 ≤ m ≤ n l 
# Characters in text and pattern can be any valid characters (e.g., a–z, A–Z, digits, etc.

def naiveStringMatch(text, pattern):
    n = len(text)
    m = len(pattern)
    print("Pattern found at positions:", end=" ")
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            print(i, end=" ")
    print()

# ---- Main ----
text = input("Enter text: ")
pattern = input("Enter pattern: ")
naiveStringMatch(text, pattern)
