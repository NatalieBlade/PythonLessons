#name = input ("Как тебя зовут?")
#gender = input ("Твой пол: ж/м")

#if gender is "ж":
    #print ("Привет, красавица " + name)
#elif gender is "м":
    #print ("Привет, красавчик " + name)
#else:
    #print ("Кто ты?")

name = input ("Как вас зовут?")
age = int(input ("Сколько вам лет?"))

if age > 0 and age < 18:
    print ("Вы еще так молоды, " + name)
elif age >= 18 and age < 55:
    print ("Вы нам подходите, " + name)
elif age >= 55:
    print("Простите, вы нам не подходите, " + name)
else:
    print ("Уточните ваш возраст, пожалуйста")