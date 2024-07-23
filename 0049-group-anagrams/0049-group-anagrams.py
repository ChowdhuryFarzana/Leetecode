class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initializing 
        anagrams = {}
        # we first need to sort the string inside the array
        # Iterate over each string in the input list
        for s in strs:
        # Sort the string and use it as a key
           sorted_str = ''.join(sorted(s))
        
        # If the sorted key is not in the dictionary, initialize it with an empty list
           if sorted_str not in anagrams:
                anagrams[sorted_str] = []
        
        # Append the original string to the list corresponding to the sorted key
           anagrams[sorted_str].append(s)

    # Convert the dictionary values to a list of lists
        return list(anagrams.values())
      