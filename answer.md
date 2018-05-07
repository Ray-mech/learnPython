# 練習問題の答え（解答例）
* * *

1. 3人の身長と体重がそれぞれ与えられるので，「3人それぞれのBMI」「身長の平均」「体重の平均」を表示するプログラムをつくってください

- コード

```python
#身長(cm)
al = 163
bl = 176
cl = 169
#体重(kg)
aw = 59
bw = 65
cw = 52

aBMI = aw / (al/100)**2
bBMI = bw / (bl/100)**2
cBMI = cw / (cl/100)**2

lAvg = (al + bl + cl) / 3
wAvg = (aw + bw + cw) / 3

print("BMI:", aBMI, bBMI, cBMI)
print("身長の平均:", lAvg)
print("体重の平均:", wAvg)
```

- 実行結果 

```Markdown
BMI: 22.20633068613798 20.983987603305785 18.20664542558034
身長の平均: 169.33333333333334
体重の平均: 58.666666666666664
```

2. 10人の身長と体重がそれぞれリストで与えられるので，「身長の平均」「体重の平均」を表示するプログラムをつくってください  
```python
#10人の身長・体重データ
#身長(cm)
height = [163, 176, 169, 185, 170, 173, 164, 166, 172, 158]
#体重(kg)
weight = [59, 65, 52, 70, 63, 57, 64, 52, 58, 50]

avgH = sum(height)/len(height)
avgW = sum(weight)/len(weight)
print("身長平均:"+str(avgH)+"　体重平均:"+str(avgW))

bmi = []
for n in range(len(height)):
    bmi.append( weight[n] / (height[n]/100)**2 )   
print(bmi)
```
