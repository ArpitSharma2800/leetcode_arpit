from typing import List
def longestCommonPrefix(strs: List[str]) -> str:
        if len(strs) == 0:
            return ("")
        if len(strs) == 1:
            return( strs[0])

        prefix = strs[0]
        length = len(prefix)
        for s in strs[1:]: #remaining strings in list
            while prefix != s[0:length]: #if prefix and string similar
                prefix = prefix[0:length-1] #shortning length by 1
                length = length - 1
                if(length == 0 ):
                    return("")
        return(prefix)


        



longestCommonPrefix(strs = ["flower","flow","flight"])