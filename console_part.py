from generator import novice_gen, lover_gen, master_gen, task_gen
from fractions import Fraction
from settings import svod

def do_console():
    coins = {'balance': 0, 'novice': 500, 'lover': 1000, 'master':2000, 'task':2500}
    hard = 1
    answer = 0
    CheckTrue = 0
    user_hard = 'новичок'    
    while True:
        UserMessage = input('введите сообщение ')
        if UserMessage.lower() == 'баланс':
            print('Ваш баланс ' + str(coins['balance']) + ' mathcoins')
        elif UserMessage.lower() == 'сдаюсь':
            print(answer)
        elif UserMessage.lower() == 'новичок':
            user_hard = 'новичок'
            hard = 1
            CheckTrue = 0
            gen = novice_gen(hard)
            print('Выбран уровень сложности: новичок')
            print(gen[0])
            answer = gen[1]
        elif UserMessage.lower() == 'любитель':
            user_hard = 'любитель'
            hard = 1
            CheckTrue = 0
            gen = lover_gen(hard)
            print('Выбран уровень сложности: любитель')
            print(gen[0])
            answer = gen[1]
        elif UserMessage.lower() == 'мастер':
            user_hard = 'мастер'
            hard = 1
            CheckTrue = 0
            gen = master_gen(hard)
            print('Выбран уровень сложности: мастер')
            print(gen[0])
            answer = gen[1]
        elif UserMessage.lower() == 'задача':
            user_hard = 'задача'
            hard = 1
            CheckTrue = 0
            gen = novice_gen(hard)
            print('Выбран уровень сложности: задачи')
            print(gen[0])
            answer = gen[1]
        elif UserMessage.lower() == 'помощь':
            print(svod % (str(len(str(hard)))))
        elif UserMessage.lower() == 'дай пример':
            user_hard = 'новичок'
            hard = 1
            CheckTrue = 0
            coins = {'balance': 0, 'novice': 500, 'lover': 1000, 'master': 2000}
            gen = novice_gen(hard)
            print(gen[0])
            answer = gen[1]                                            
                                     
        else:
            if (user_hard == 'любитель') and ('/' in UserMessage):
                UserMessage = Fraction(UserMessage)
                answer = Fraction(answer)
            elif (user_hard == 'мастер') and (float(answer) == int(float(answer))):
                answer = str(abs(int(float(answer))))
            if str(UserMessage) == str(answer):
                if  CheckTrue >= 9:
                    hard *= 10
                    CheckTrue = 0
                    print( 'Правильно!' )
                    print("Получен " + str(len(str(hard))) + " уровень")
                    print(str(CheckTrue) + '/10 EXP' )
                    if user_hard == 'новичок':
                        print('Получено ' + str(coins['novice'] / 100 * len(str(hard))) + ' mathcoins')
                        coins['balance'] += coins['novice'] / 100 * len(str(hard))
                        coins['novice'] -= coins['novice'] / 100 * len(str(hard))
                        gen = novice_gen(hard)
                        print(gen[0])
                        answer = gen[1]
                    elif user_hard == 'любитель':
                        print('Получено ' + str(coins['lover'] / 100 * len(str(hard))) + ' mathcoins')
                        coins['balance'] += coins['lover'] / 100 * len(str(hard))
                        coins['lover'] -= coins['lover'] / 100 * len(str(hard))
                        gen = lover_gen(hard)
                        print(gen[0])
                        answer = gen[1]                      
                    elif user_hard == 'мастер':
                        print('Получено ' + str(coins['master'] / 100 * len(str(hard))) + ' mathcoins')
                        coins['balance'] += coins['master'] / 100 * len(str(hard))
                        coins['master'] -= coins['master'] / 100 * len(str(hard))
                        gen = master_gen(hard)
                        print(gen[0])
                        answer = gen[1]
                    elif user_hard == 'задача':
                        print('Получено ' + str(coins['task'] / 100 * len(str(hard))) + ' mathcoins')
                        coins['balance'] += coins['task'] / 100 * len(str(hard))
                        coins['task'] -= coins['task'] / 100 * len(str(hard))
                        gen = novice_gen(hard)
                        print(gen[0])
                        answer = gen[1]
                else:
                    CheckTrue += 1
                    print('Правильно!')
                    print(str(CheckTrue) + '/10 EXP' )
                    if user_hard == 'новичок':
                        print('Получено ' + str(coins['novice'] / 100 * len(str(hard))) + ' mathcoins')
                        coins['balance'] += coins['novice'] / 100 * len(str(hard))
                        coins['novice'] -= coins['novice'] / 100 * len(str(hard))
                        gen = novice_gen(hard)
                        print(gen[0])
                        answer = gen[1]
                    elif user_hard == 'любитель':
                        print('Получено ' + str(coins['lover'] / 100 * len(str(hard))) + ' mathcoins')
                        coins['balance'] += coins['lover'] / 100 * len(str(hard))
                        coins['lover'] -= coins['lover'] / 100 * len(str(hard))
                        gen = lover_gen(hard)
                        print(gen[0])
                        answer = gen[1]
                    elif user_hard == 'мастер':
                        print('Получено ' + str(coins['master'] / 100 * len(str(hard))) + ' mathcoins')
                        coins['balance'] += coins['master'] / 100 * len(str(hard))
                        coins['master'] -= coins['master'] / 100 * len(str(hard))
                        gen = master_gen(hard)
                        print(gen[0])
                        answer = gen[1]
                    elif user_hard == 'задача':
                        print('Получено ' + str(coins['task'] / 100 * len(str(hard))) + ' mathcoins')
                        coins['balance'] += coins['task'] / 100 * len(str(hard))
                        coins['task'] -= coins['task'] / 100 * len(str(hard))
                        gen = novice_gen(hard)
                        print(gen[0])
                        answer = gen[1]
            else:
                print('Неправильно!!!')
                if CheckTrue >= 2:
                    CheckTrue -= 2 
                    print(str(CheckTrue) + '/10 EXP' )
                else:
                    CheckTrue = 0
                    print(str(CheckTrue) + '/10 EXP' )
