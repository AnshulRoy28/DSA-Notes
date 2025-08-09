def groupAnagrams(strs):
    """
    Input:
        strs (List[str]): A list of strings to be grouped by anagrams.

    Output:
        List[List[str]]: A list of lists where each sublist contains strings that are anagrams of each other.

    Purpose:
        Group the given strings so that all anagrams are grouped together.
        The function sorts each string to use as a key and groups all strings with the same sorted key.
    """
    map={}

    for word in strs:
        sorted_word="".join(sorted(word)) #Sort each word 

        if sorted_word not in map:
            map[sorted_word]=[] #add the sorted word to the dictionary
        
        map[sorted_word].append(word) #Add each word to its sorted variant 

    return list(map.values()) #Return the values 


"""
Java Implementation
class Solution {
    public List < List < String >> groupAnagrams(String[] strs) {
        HashMap < String, ArrayList < String >> map = new HashMap < > ();
        for (String word: strs) {
            char[] charArr = word.toCharArray();
            Arrays.sort(charArr);
            String newStr = new String(charArr);
            if (!map.containsKey(newStr)) {
                map.put(newStr, new ArrayList < String > ());
            }
            map.get(newStr).add(word);
        }
        return new ArrayList < > (map.values());
    }
}
"""
