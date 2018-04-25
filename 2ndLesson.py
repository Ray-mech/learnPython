#3人の身長・体重データ
#身長(cm)
height = [163, 176, 169]
#体重(kg)
weight = [59, 65, 52]


BMI=[0] * len(height)
for i in range(len(height)):
    BMI[i] = weight[i] / (height[i]/100)**2

print(BMI)

heightAvg = sum(height)/len(height)
print (heightAvg)

weightAvg = sum(weight)/len(weight)
print (weightAvg)
