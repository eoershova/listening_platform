from django.shortcuts import render
from .models import *

def index(request):
    context = {}
    return render(request, 'vars/index.html', context)


#def var1(request):
    #return render(request, 'vars/var1.html')

def var2(request):
    return render(request, 'vars/var2.html')

def var3(request):
    return render(request, 'vars/var3.html')

def var4(request):
    return render(request, 'vars/var4.html')

def var5(request):
    return render(request, 'vars/var5.html')

def var6(request):
    return render(request, 'vars/var6.html')

def var7(request):
    return render(request, 'vars/var7.html')

def var8(request):
    return render(request, 'vars/var8.html')

def var9(request):
    return render(request, 'vars/var9.html')

def var10(request):
    return render(request, 'vars/var10.html')

def var11(request):
    return render(request, 'vars/var11.html')

def var12(request):
    return render(request, 'vars/var12.html')

def results(request):
    return render(request, 'vars/results.html')



from .forms import AnswersForm


def var1(request):
    ans = []
    info = []
    if request.method == "POST":
        form = AnswersForm(request.POST)
        name = request.POST.get("name").lower()
        surname = request.POST.get("surname").lower()
        group = request.POST.get("group").lower()
        a1 = request.POST.get("ans1").lower()
        a2 = request.POST.get("ans2").lower()
        a3 = request.POST.get("ans3").lower()
        a4 = request.POST.get("ans4").lower()
        a5 = request.POST.get("ans5").lower()
        a6 = request.POST.get("ans6").lower()
        a7 = request.POST.get("ans7").lower()
        a8 = request.POST.get("ans8").lower()
        a9 = request.POST.get("ans9").lower()
        a10 = request.POST.get("ans10").lower()
        a11 = request.POST.get("ans11").lower()
        a12 = request.POST.get("ans12").lower()
        a13 = request.POST.get("ans13").lower()
        a14 = request.POST.get("ans14").lower()
        a15 = request.POST.get("ans15").lower()
        a16 = request.POST.get("ans16").lower()
        a17 = request.POST.get("ans17").lower()
        a18 = request.POST.get("ans18").lower()
        a19 = request.POST.get("ans19").lower()
        a20 = request.POST.get("ans20").lower()
        a21 = request.POST.get("ans21").lower()
        a22 = request.POST.get("ans22").lower()
        a23 = request.POST.get("ans23").lower()
        a24 = request.POST.get("ans24").lower()
        a25 = request.POST.get("ans25").lower()
        a26 = request.POST.get("ans26").lower()
        a27 = request.POST.get("ans27").lower()
        a28 = request.POST.get("ans28").lower()
        a29 = request.POST.get("ans29").lower()
        a30 = request.POST.get("ans30").lower()
        a31 = request.POST.get("ans31").lower()
        a32 = request.POST.get("ans32").lower()
        a33 = request.POST.get("ans33").lower()
        a34 = request.POST.get("ans34").lower()
        a35 = request.POST.get("ans35").lower()
        a36 = request.POST.get("ans36").lower()
        a37 = request.POST.get("ans37").lower()
        a38 = request.POST.get("ans38").lower()
        a39 = request.POST.get("ans39").lower()
        a40 = request.POST.get("ans40").lower()

        ans.append(a1)
        ans.append(a2)
        ans.append(a3)
        ans.append(a4)
        ans.append(a5)
        ans.append(a6)
        ans.append(a7)
        ans.append(a8)
        ans.append(a9)
        ans.append(a10)
        ans.append(a11)
        ans.append(a12)
        ans.append(a13)
        ans.append(a14)
        ans.append(a15)
        ans.append(a16)
        ans.append(a17)
        ans.append(a18)
        ans.append(a19)
        ans.append(a20)
        ans.append(a21)
        ans.append(a22)
        ans.append(a23)
        ans.append(a24)
        ans.append(a25)
        ans.append(a26)
        ans.append(a27)
        ans.append(a28)
        ans.append(a29)
        ans.append(a30)
        ans.append(a31)
        ans.append(a32)
        ans.append(a33)
        ans.append(a34)
        ans.append(a35)
        ans.append(a36)
        ans.append(a37)
        ans.append(a38)
        ans.append(a39)
        ans.append(a40)
        info.append(name)
        info.append(surname)
        info.append(group)

        right = RightAnswers.objects.filter(id=1).values()

        list_of_rv = []
        points_for_task = []  # в базу данных
        for i in right:
            for value in i.values():
                list_of_rv.append(str(value).split(','))
        for n in range(len(ans)):
            if ans[n].replace(' ', '') in list_of_rv[2:][n]:
                points_for_task.append(1)
            else:
                points_for_task.append(0)

        res = ''
        num = 0
        for r in points_for_task:
            num += r
        res += 'Your result: ' + str(num) + '/40'  # на страницу с результатами

        task1_result = ''
        t1_count = 0
        for t1 in points_for_task[:10]:
            t1_count += t1
        task1_result += 'Task 1: ' + str(t1_count) + '/10'

        task2_result = ''
        t2_count = 0
        for t2 in points_for_task[10:20]:
            t2_count += t2
        task2_result += 'Task 2: ' + str(t2_count) + '/10'

        task3_result = ''
        t3_count = 0
        for t3 in points_for_task[20:30]:
            t3_count += t3
        task3_result += 'Task 3: ' + str(t3_count) + '/10'

        task4_result = ''
        t4_count = 0
        for t4 in points_for_task[30:40]:
            t4_count += t4
        task4_result += 'Task 4: ' + str(t4_count) + '/10'

        query = Answers(name=name,
                             surname=surname,
                             group=group,
                             var=1,
                             a1=a1,
                             a2=a2,
                             a3=a3,
                             a4=a4,
                             a5=a5,
                             a6=a6,
                             a7=a7,
                             a8=a8,
                             a9=a9,
                             a10=a10,
                             a11=a11,
                             a12=a12,
                             a13=a13,
                             a14=a14,
                             a15=a15,
                             a16=a16,
                             a17=a17,
                             a18=a18,
                             a19=a19,
                             a20=a20,
                             a21=a21,
                             a22=a22,
                             a23=a23,
                             a24=a24,
                             a25=a25,
                             a26=a26,
                             a27=a27,
                             a28=a28,
                             a29=a29,
                             a30=a30,
                             a31=a31,
                             a32=a32,
                             a33=a33,
                             a34=a34,
                             a35=a35,
                             a36=a36,
                             a37=a37,
                             a38=a38,
                             a39=a39,
                             a40=a40,
                             points=points_for_task,
                             result=num,
                             task1=t1_count,
                             task2=t2_count,
                             task3=t3_count,
                             task4=t4_count
                             )
        query.save()



        return render(request, "vars/results.html", {"form":ans, "right":right, "res":res, "task1_result":task1_result, "task2_result":task2_result, "task3_result":task3_result, "task4_result":task4_result})
    else:
        answers = Answers()
        return render(request, "vars/var1.html", {"form": answers})


