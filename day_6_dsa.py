#Q) You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi.
#  Return the destination city, that is, the city without any path outgoing to another city. 


class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        curr = []
        next = []
        for i in range(len(paths)):
            curr.append(paths[i][0])
            next.append(paths[i][1])
        c = paths[0][0]
        while(next[curr.index(c)] in curr):
            c = next[curr.index(c)]
        return next[curr.index(c)]