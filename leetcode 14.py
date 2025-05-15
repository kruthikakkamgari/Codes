class Solution:
    def longestCommonPrefix(self,strs:list[str])->str:
        pref=strs[0]
        x=len(pref)
        for i in strs[1:]:
            while pref!=i[0:x]:
                x-=1
                if x==0:
                    return""
                pref=pref[0:x]
        return pref