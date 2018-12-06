#密碼重複輸入程式，最多三次

time = 1

while time <= 3 :

    password = input('請輸入密碼(最多三次)')
    

    if password == 'a123456':
        print('密碼正確，請進入')
        break
    elif password != 'a123456' :
        print('密碼錯誤！')
        if time <= 2:
            print('你還有', 3 - time, '次機會')
        time = time + 1 
    if time == 4 :
        print('達次數上限，已鎖定程式')
        break
    
