# ���� 1459�� �ȱ�
# SILVER 5
# �˰��� �з� : ����, ���� ���� �б�
# �޸� : 30840 KB, �ð� : 72 ms, ��� Python3, �ڵ���� 241B

X,Y,W,S = map(int,input().split())

min = min(X,Y)
gap = abs(X-Y)
c = gap%2
if 2*W < S :
    t = 2*W*min
else :
    t = S*min
if c == 0 and W > S :
    t += gap*S
elif c != 0 and W > S :
    t += (gap-c)*S + c*W
else :
    t += gap*W
print(t)