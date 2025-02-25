class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
    
        # Dictionary to keep count of characters in t
        char_count = {}
        for char in t:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Number of unique characters in t
        required = len(char_count)
        
        # Variables to track the sliding window
        left, right = 0, 0
        formed = 0  # Number of unique characters in t that are satisfied in current window
        
        # Dictionary to keep track of characters in current window
        window_counts = {}
        
        # Variables to track the answer
        min_len = float('inf')
        result_start = 0
        
        while right < len(s):
            # Add the current character to window_counts
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Check if adding the character helped satisfy a character in t
            if char in char_count and window_counts[char] == char_count[char]:
                formed += 1
            
            # Try to contract the window from the left
            while left <= right and formed == required:
                char = s[left]
                
                # Update the result if a smaller valid window is found
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result_start = left
                
                # Remove the leftmost character from the window
                window_counts[char] -= 1
                
                # Check if removing the character breaks the window's validity
                if char in char_count and window_counts[char] < char_count[char]:
                    formed -= 1
                
                left += 1
            
            # Expand the window
            right += 1
        
        # Return the minimum window substring or empty string if no valid window found
        return "" if min_len == float('inf') else s[result_start:result_start + min_len]