# BMI=体重/（身高**2）
user_weight=float(input("请输入你的体重（单位：kg）："))
user_height=float(input("请输入你的身高（单位：m）："))
user_BMI=user_weight/(user_height)**2
print("你的BMI是："+str(user_BMI))

# 偏瘦：user_BMI <= 18.5
# 正常：18.5 <user_BMI <= 25
# 偏胖：25 <user_BMI <= 30
# 肥胖：user_BMI > 30
if user_BMI <= 18.5:
    print("你的BMI属于偏瘦范围")
elif 18.5<user_BMI<=25:
    print("你的BMI属于正常范围")
elif 25<user_BMI<=30:
    print("你的BMI值属于偏胖范围")
else:
    print("你的BMI值属于肥胖范围")