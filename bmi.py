#创建计算BMI指数的模块
def fun_bmi(person, height, weight):
    '''
        功能：根据身高、体重计算BMI指数
        person: 姓名
        heigth: 身高，单位：米
        weigth: 体重，单位：千克
    '''
    print(person + "的身高为：" + str(height) + "米\t体重：" + str(weight) + "千克")
    # 计算BMI，并显示
    bmi = weight / (height * height)
    print("您的BMI指数为：" + str(bmi))
def fun_bmi_upgrade(*person):
    '''
        功能：根据身高、体重计算BMI指数
        *person: 可变参数，该参数中需要传递带3个元素的列表，
                分别是姓名、身高（单位：米）、体重（单位：千克）
    '''