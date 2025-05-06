# -*- coding: utf-8 -*-
"""
Created on Mon May  5 08:35:53 2025

@author: Qiong Wu
"""


"""
Q1. Camel Case
"""
def camelcase(s):
    # Write your code here
    uppercase_count = 0
    for char in s:
        if char.isupper():
            uppercase_count += 1
    
    total_words = uppercase_count + 1
    return total_words 

test_case1 = 'saveChangesInTheEditor'
expected_result1 = 5
assert(expected_result1 == camelcase(test_case1))

"""
Q2. Super Reduced String
"""
def superReducedString(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    result = ''.join(stack)
    
    if len(result) == 0:
        result = 'Empty String'
    
    return result

test_case2 = 'aaabccddd'
expected_result2 = 'abd'
assert(expected_result2 == superReducedString(test_case2))

"""
Q3. Strong Password
"""
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    # Define the character sets
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    special_characters = '[!@#$%^&*()-+]'
    has_special_characters = any(c in special_characters for c in password)
    
    # Count
    condition_not_meet = 0
    if not has_lower:
        condition_not_meet += 1
    if not has_upper:
        condition_not_meet += 1
    if not has_digit:
        condition_not_meet += 1    
    if not has_special_characters:
        condition_not_meet += 1
    
    min_chars_to_add = max(condition_not_meet, 6 - len(password))
    
    return min_chars_to_add

test_case3_n = 11
test_case3_password = '#HackerRank'
expected_result3 = 1
assert(expected_result3 == minimumNumber(test_case3_n, test_case3_password))

"""
Q4. Two Characters
"""
def alternate(s):
    # Write your code here
    if len(s) < 2:
        return 0
    
    # Get all unique characters in the string
    unique_chars = set(s)
    
    max_length = 0
    
    # Try all possible pairs of distinct characters
    for char1 in unique_chars:
        for char2 in unique_chars:
            if char1 == char2:
                continue  # Skip same characters
            
            # Filter string to include only char1 and char2
            filtered = [c for c in s if c == char1 or c == char2]
            
            # Check if the filtered string is alternating
            is_alternating = True
            for i in range(1, len(filtered)):
                if filtered[i] == filtered[i-1]:  # Two same characters adjacent
                    is_alternating = False
                    break
            
            # If alternating, update max_length if longer
            if is_alternating:
                max_length = max(max_length, len(filtered))
                
    return max_length

test_case4 = 'beabeefeab'
expected_result4 = 5
assert(expected_result4 == alternate(test_case4))

"""
Q5. Mars Exploration 
"""
def marsExploration(s):
    sos = 'SOS'
    count = 0
    for i in range(0, len(s), 3):
        substring = s[i: i+3]
    
        for j in range(3):
            if substring[j] != sos[j]:
                count += 1
    
    return count    

test_case5 = 'SOSSPSSQSSOR'
expected_result5 = 3
assert(expected_result5 == marsExploration(test_case5))

"""
Q6. HackerRank is a string!
"""
def hackerrankInString(s):
    target_string = 'hackerrank'
    index = 0
    for char in s:
        if index < len(s) and char == target_string[index]:
            index += 1
        if index == len(target_string):
            return 'YES'
   
    if index == len(target_string):
        result = 'YES'
    else:
        result = 'NO'
    
    return result

test_case6 = 'hereiamstackerrank'
expected_result6 = 'YES'
assert(expected_result6 == hackerrankInString(test_case6))

"""
Q7. Caesar Cipher
"""
def caesarCipher(s, k):
    # Write your code here
    k = k % 26
    result = []
    
    for char in s:
        if char.isalpha():
            base = 97 if char.islower() else 65
            shifted = (ord(char) - base + k) % 26
            result.append(chr(shifted + base))
        else:
            result.append(char)
    return ''.join(result)  

test_case7_s = 'abcdefghijklmnopqrstuvwxyz'
test_case7_k = 3
expected_result7 = 'defghijklmnopqrstuvwxyzabc'
assert(expected_result7 == caesarCipher(test_case7_s, test_case7_k))
    
"""
Q8. Weighted Uniform String
"""
def weightedUniformStrings(s, queries):
    # Write your code here
    weights = set()
    current_char = s[0]
    count = 1
    char_weight = ord(current_char) - 96
    weights.add(char_weight)
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            current_char = s[i]
            count = 1
            char_weight = ord(current_char) - 96
        
        weights.add(char_weight * count)        
    
    # Process queries
    result = []
    for query in queries:
        result.append("Yes" if query in weights else "No")
    
    return result

    

            
    







