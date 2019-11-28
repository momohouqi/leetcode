
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        inDegree =[0] * numCourses
        adjList =[[] for i in range(numCourses)]
        for (dst, src) in prerequisites:
            inDegree[dst] += 1
            adjList[src].append(dst)


        zero_in_q = [i for i in range(numCourses) if inDegree[i]==0]

        ans = []
        while zero_in_q:
            node = zero_in_q.pop()
            for dst in adjList[node]:
                inDegree[dst] -= 1
                if inDegree[dst] == 0:
                    zero_in_q.append(dst)
            ans.append(node)

        return ans

    @staticmethod
    def test_case():
        s = Solution()
        ans = s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
        print("Done:{}".format(ans))

class BagSolution(object):
    @staticmethod
    def test_case():
        num = 5
        weights = [2, 2, 6, 5, 4]
        values = [6, 3, 5, 4, 6]
        ans = BagSolution().find(num, weights, values, 10)
        print(ans)

    def find(self, num, weights, values, max_weight):
        """
        s[num][capaicity]:
        :param num:
        :param weights:
        :param values:
        :return:
        """
        m = [[0]*max_weight for i in range(num + 1)]
        for n in range(1, num + 1):
            for cap in range(1, max_weight + 1):
                if weights[n] > cap:
                    m[n][cap] = m[n-1][cap]
                else:
                    m[n][cap] = max(m[n-1][cap-weights[n]] + values[n], m[n-1][cap])
        return m

def main():
    """
    s = Solution()
    ans = s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
    print("Done:{}".format(ans))
    """
    b = BagSolution()
    b.test_case()


if __name__ == '__main__':
    main()