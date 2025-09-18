class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        students=deque(students)
        cnt=0
        i=0
        while students and cnt < len(students):
            if students[0]==sandwiches[i]:
                students.popleft()
                i+=1
                cnt=0
            else:
                students.append(students.popleft())
                cnt=cnt+1

        return (len(students))