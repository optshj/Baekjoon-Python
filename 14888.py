# ���� 14888�� ������ �����ֱ�
# SILVER 1
# ���� ���� : ���Ʈ���� �˰���,��Ʈ��ŷ
# �޸� : 30840 KB, �ð� : 96 ms, ��� Python3, �ڵ���� 778B

N = int(input())
li = list(map(int,input().split()))
tac = list(map(int,input().split()))
max = -1000000000
min = 1000000000

def dfs(plus,minus,multiple,divide,start,result) :
    global max 
    global min
    if start == N:
        if result < min :
            min = result
        if result > max :
            max = result
        return
    if tac[0] != plus :
        dfs(plus+1,minus,multiple,divide,start+1,result+li[start])
            
    if tac[1] != minus :
        dfs(plus,minus+1,multiple,divide,start+1,result-li[start])

    if tac[2] != multiple :
        dfs(plus,minus,multiple+1,divide,start+1,result*li[start])

    if tac[3] != divide :
        dfs(plus,minus,multiple,divide+1,start+1,int(result/li[start]))

dfs(0,0,0,0,1,li[0])
print(max)
print(min)