# 1. Palindrome: a string equal to its own reverse
def is_palindrome(s):
    return s == s[::-1]

# 2. Min and max: return both as tuple
def min_max(lst):
    return min(lst), max(lst)

# 3. Remove duplicates, keep order: add to result only if not seen before
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# 4. Second largest: use a set to drop repeats, sort, take second from end
def second_largest(lst):
    unique = sorted(set(lst))
    if len(unique) < 2:
        return None
    return unique[-2]

# 5. Reverse a tuple and find its sum
def reverse_and_sum(t):
    return t[::-1], sum(t)

# 6. Common elements: intersection of two sets
def common_elements(a, b):
    return set(a) & set(b)

# 7. Word frequency: count each word using get() with a default of 0
def word_frequency(sentence):
    freq = {}
    for word in sentence.split():
        freq[word] = freq.get(word, 0) + 1
    return freq

# 8. Topper: key with the highest value
def topper(marks):
    return max(marks, key=marks.get)

# 9. Squares of even numbers from 1 to 10 
def even_squares():
    return[x ** 2 for x in range(1, 11) if x % 2 == 0]

# 10. Anagram: same letters when sorted
def is_anagram(a, b):
    return sorted(a) == sorted(b)

# Test with sample inputs
print(is_palindrome("madam"))
print(min_max([4, 9, 2, 7]))
print(remove_duplicates([1, 2, 2, 3, 1, 4]))
print(second_largest([10, 40, 30, 20]))
print(reverse_and_sum((1, 2, 3, 4, 5)))
print(common_elements([1, 2, 3, 4], [3, 4, 5]))
print(word_frequency("the cat and the hat"))
print(topper({"A": 82, "B": 91, "C": 75}))
print(even_squares())
print(is_anagram("listen", "silent"))

# Edge cases
print(second_largest([5, 5, 5]))
print(remove_duplicates([]))
print(is_anagram("abc", "abd"))