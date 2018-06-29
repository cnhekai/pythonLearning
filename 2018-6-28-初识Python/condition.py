bodyWeight = input('请输入体重(kg)：')
height = input('请输入身高(cm)：')

def calculation():
  global height
  global bodyWeight
  if height.isdigit() and bodyWeight.isdigit():
    height = int(height)
    bodyWeight = int(bodyWeight)
    bmi = bodyWeight / ((height / 100) ** 2)
    print('*********************************************')
    if bmi < 18.5:
      print("您的体重为：",bodyWeight,"\n您的身高为：",height,"\n您的BMI为：{0:.1f}".format(bmi),"\n您的BMI指数为：过轻")
    elif bmi >= 18.5 and bmi < 25:
      print("您的体重为：",bodyWeight,"\n您的身高为：",height,"\n您的BMI为：{0:.1f}".format(bmi),"\n您的BMI指数为：正常")
    elif bmi >= 25 and bmi < 28:
      print("您的体重为：",bodyWeight,"\n您的身高为：",height,"\n您的BMI为：{0:.1f}".format(bmi),"\n您的BMI指数为：过重")
    elif bmi >= 28 and bmi < 32:
      print("您的体重为：",bodyWeight,"\n您的身高为：",height,"\n您的BMI为：{0:.1f}".format(bmi),"\n您的BMI指数为：肥胖")
    else:
      print("您的体重为：",bodyWeight,"\n您的身高为：",height,"\n您的BMI为：{0:.1f}".format(bmi),"\n您的BMI指数为：严重肥胖")
  else:
    if not height.isdigit():
      height = input('您输入的身高不是数字，请重新输入身高(cm)：')
    if not bodyWeight.isdigit():
      bodyWeight = input('您输入的体重不是数字，请重新输入体重(kg)：')
    calculation()

calculation()