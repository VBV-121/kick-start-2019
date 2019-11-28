#input for the file
test_case=int(input("Number of test case"))

for i in range(0,test_case):
    ip=input("Enter total number of player and number of player need to be selected ")
    ip=ip.split()
    total_student=int(ip[0])
    student_selected=int(ip[1])

    skills=input("Enter the skill set of student")
    skills=skills.split()
    skills=list(map(int,skills))

    # function processing
    def cluster(skills):
        p1=min(skills)
        p2=max(skills)

        cp1=[]
        cp2=[]
        for i in range(0,len(skills)):
            if abs(p1-skills[i])<=abs(p2-skills[i]):
                cp1.append(skills[i])
            else:
                cp2.append(skills[i])
        return cp1,cp2

    def difference(student_selected,cp1,cp2):
        if len(cp1)==1:
            v=process(cp2,cp1,student_selected)
            return v
        elif len(cp2)==1:
            v=process(cp1,cp2,student_selected)
            return v
        else:
            if (max(cp1)-min(cp1))<(max(cp2)-min(cp2)):
                v=process(cp1,cp2,student_selected)
            else:
                v=process(cp2,cp1,student_selected)
            return v

    def process(cp1,cp2,student_selected):
        if len(cp1)!=student_selected:
            diff=len(cp1)-student_selected
            if diff<=0:
                for i in range(0,abs(diff)):
                    cp1.append(cp2.pop(cp2.index(min(cp2))))
                    return cp1
            else:
                new1,new2=cluster(cp1)
                temp=difference(student_selected,new1,new2)
                return temp
        else:
            return cp1

    #actual process
    cp1,cp2=cluster(skills)
    d=difference(student_selected,cp1,cp2)

    d.sort()
    sum=0
    for i in range(0,len(d)-1):
        sum+=(abs(d[i]-d[len(d)-1]))

    print(sum)
