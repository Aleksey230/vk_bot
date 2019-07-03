from fractions import Fraction
from vk_api.longpoll import VkLongPoll, VkEventType
from generator import novice_gen, lover_gen, master_gen
from achivments import achivments
from pymongo import MongoClient
from settings import svod
from keyboard import kb
import vk_api

client = MongoClient('localhost', 27017)
db = client.history
collection = db.messages

def do_vk():
    token = 'a05a0530ccb33113ba4f326de748a5d83b0a851a50ecbc23bbec5c5eeb7c839cc77387fa8e23ab41a300e'
    vk = vk_api.VkApi(token = token)
    longpoll = VkLongPoll(vk)
    for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                    if event.to_me:
                            if event.text.lower () == 'начать':
                                vk.method('messages.send', {'user_id':event.user_id,'message': 'Приветствую, можешь начинать', 'random_id':0, 'keyboard': kb})
                            elif event.text.lower() == 'баланс':
                                example2 = collection.find({'user_id': event.user_id, 'to_me': True}).sort('time', -1).limit(1)[0]
                                if example2 == []:
                                    vk.method('messages.send', {'user_id':event.user_id,'message': 'Ваш баланс 0 mathcoins', 'random_id':0, 'keyboard': kb})
                                else:
                                    vk.method('messages.send', {'user_id':event.user_id,'message':'Ваш баланс ' + str(example2['balance']) + ' mathcoins', 'random_id':0, 'keyboard': kb})
                            elif event.text.lower() == 'сдаюсь':
                                example = collection.find({'user_id': event.user_id, 'by_me': True}).sort('time', -1).limit(1)[0]
                                answer = example['answer']
                                vk.method('messages.send', {'user_id':event.user_id,'message': answer, 'random_id':0, 'keyboard': kb})
                            elif event.text.lower() == 'новичок':
                                example2 = collection.find({'user_id': event.user_id, 'to_me': True}).sort('time', -1).limit(1)[0]
                                hard = 1
                                gen = novice_gen(hard)
                                answer = gen[1]
                                s = {'time': event.timestamp, 'user_id': event.user_id, 'message': event.text, 'hard' : 1, 'EXP': 0, 'to_me': True, 'user_hard': 'новичок', 'balance': example2['balance'], 'novice': example2['novice'], 'lover': example2['lover'], 'master': example2['master'], 'novice_ac': example2['novice_ac'], 'lover_ac': example2['lover_ac'], 'master_ac': example2['master_ac']}
                                collection.insert_one(s)
                                a = {'time': event.timestamp, 'user_id': event.user_id, 'message': gen[0], 'answer': answer, 'by_me': True}
                                collection.insert_one(a)
                                vk.method('messages.send', {'user_id':event.user_id,'message': 'Выбран уровень сложности: новичок', 'random_id':0})
                                vk.method('messages.send', {'user_id':event.user_id,'message': gen[0], 'random_id':0})
                            elif event.text.lower() == 'мастер':
                                example2 = collection.find({'user_id': event.user_id, 'to_me': True}).sort('time', -1).limit(1)[0]
                                hard = 1
                                gen = master_gen(hard)
                                answer = gen[1]                                
                                s = {'time': event.timestamp, 'user_id': event.user_id, 'message': event.text, 'hard' : 1, 'EXP': 0, 'to_me': True, 'user_hard': 'мастер', 'balance': example2['balance'], 'novice': example2['novice'], 'lover': example2['lover'], 'master': example2['master'], 'novice_ac': example2['novice_ac'], 'lover_ac': example2['lover_ac'], 'master_ac': example2['master_ac']}
                                collection.insert_one(s)
                                a = {'time': event.timestamp, 'user_id': event.user_id, 'message': gen[0], 'answer': str(answer), 'by_me': True}
                                collection.insert_one(a)
                                vk.method('messages.send', {'user_id':event.user_id,'message': 'Выбран уровень сложности: мастер', 'random_id':0})
                                vk.method('messages.send', {'user_id':event.user_id,'message': gen[0], 'random_id':0})
                            elif event.text.lower() == 'любитель':
                                example2 = collection.find({'user_id': event.user_id, 'to_me': True}).sort('time', -1).limit(1)[0]
                                hard = 1
                                gen = lover_gen(hard)
                                answer = gen[1]
                                s = {'time': event.timestamp, 'user_id': event.user_id, 'message': event.text, 'hard' : 1, 'EXP': 0, 'to_me': True, 'user_hard':'любитель', 'balance': example2['balance'], 'novice': example2['novice'], 'lover': example2['lover'], 'master': example2['master'], 'novice_ac': example2['novice_ac'], 'lover_ac': example2['lover_ac'], 'master_ac': example2['master_ac']}
                                collection.insert_one(s)
                                a = {'time': event.timestamp, 'user_id': event.user_id, 'message': gen[0], 'answer': str(answer), 'by_me': True}
                                collection.insert_one(a)
                                vk.method('messages.send', {'user_id':event.user_id,'message': 'Выбран уровень сложности: любитель', 'random_id':0})
                                vk.method('messages.send', {'user_id':event.user_id,'message': gen[0], 'random_id':0})
                            elif event.text.lower() == 'помощь':
                                example2 = collection.find({'user_id': event.user_id, 'to_me': True})
                                if example2 == []:
                                    vk.method('messages.send', {'user_id':event.user_id,'message': svod % (1), 'random_id':0})
                                else:
                                    example2 = example2.sort('time', -1).limit(1)[0]
                                    vk.method('messages.send', {'user_id':event.user_id,'message': svod % str(len(str(example2['hard']))), 'random_id':0})
                            elif event.text.lower() == 'дай пример':
                                user_hard = 'новичок'
                                hard = 1
                                checkTrue = 0
                                gen = novice_gen(hard)
                                answer = gen[1]
                                s = {'time': event.timestamp, 'user_id': event.user_id, 'message': event.text,
                                     'hard' : hard, 'EXP': checkTrue, 'to_me': True, 'user_hard': user_hard,
                                     'balance': 0, 'novice': 500, 'lover': 1000, 'master': 2000,
                                     'novice_ac': 0, 'lover_ac': 0, 'master_ac': 0}
                                collection.insert_one(s)
                                a = {'time': event.timestamp, 'user_id': event.user_id, 'message': gen[0], 'answer': answer, 'by_me': True,}
                                collection.insert_one(a)
                                vk.method('messages.send', {'user_id':event.user_id,'message': gen[0], 'random_id':0})
                            else:
                                example = collection.find({'user_id': event.user_id, 'by_me': True}).sort('time', -1).limit(1)[0]
                                example2 = collection.find({'user_id': event.user_id, 'to_me': True}).sort('time', -1).limit(1)[0]
                                answer = example['answer']
                                balance = example2['balance']
                                novice = example2['novice']
                                lover = example2['lover']
                                master = example2['master']
                                user_hard = example2['user_hard']
                                coins = 0
                                if (user_hard == 'любитель') and ('/' in event.text):
                                    event.text = Fraction(event.text)
                                    answer = Fraction(answer)
                                elif (user_hard == 'мастер') and (float(answer) == int(float(answer))):
                                    answer = str(abs(int(float(answer))))
                                if str(event.text) == str(answer):
                                        if example2['EXP'] >= 9:
                                                example2['hard'] *= 10
                                                example2['EXP'] = 0
                                                vk.method('messages.send', {'user_id':event.user_id,'message': 'Правильно!', 'random_id':0})
                                                if example2['user_hard'] == 'новичок':
                                                    example2['novice_ac'] += 1
                                                    coins = novice / 100 * len(str(example2['hard']))
                                                    balance += novice / 100 * len(str(example2['hard']))
                                                    novice -= novice / 100 * len(str(example2['hard']))
                                                    gen = novice_gen(example2['hard'])
                                                    my_message = gen[0]
                                                    answer = gen[1]
                                                elif example2['user_hard'] == 'любитель':
                                                    example2['lover_ac'] += 1
                                                    coins = lover / 100 * len(str(example2['hard']))
                                                    balance += lover / 100 * len(str(example2['hard']))
                                                    lover -= lover / 100 * len(str(example2['hard']))
                                                    gen = lover_gen(example2['hard'])
                                                    my_message = gen[0]
                                                    answer = gen[1]   
                                                elif example2['user_hard'] == 'мастер':
                                                    example2['master_ac'] += 1
                                                    coins = master / 100 * len(str(example2['hard']))
                                                    balance += master / 100 * len(str(example2['hard']))
                                                    master -= master / 100 * len(str(example2['hard']))
                                                    gen = master_gen(example2['hard'])
                                                    my_message = gen[0]
                                                    answer = gen[1]
                                                a = {'time': event.timestamp, 'user_id': event.user_id, 'message': my_message, 'answer': str(answer), 'by_me': True}
                                                collection.insert_one(a)
                                                vk.method('messages.send', {'user_id':event.user_id,'message': 'Получен ' + str(len(str(example2['hard']))) + ' уровень!!!', 'random_id':0})
                                                vk.method('messages.send', {'user_id':event.user_id,'message':'Получено ' + str(coins) + ' mathcoins', 'random_id':0})
                                                achivments(example2['novice_ac'], example2['lover_ac'], example2['master_ac'], event.user_id)
                                                vk.method('messages.send', {'user_id':event.user_id,'message': my_message, 'random_id':0})
                                                s = {'time': event.timestamp, 'user_id': event.user_id, 'message': str(event.text), 'hard' : example2['hard'], 'EXP': example2['EXP'], 'to_me': True, 'user_hard':user_hard, 'balance': balance, 'novice': novice, 'lover': lover, 'master': master, 'novice_ac': example2['novice_ac'], 'lover_ac': example2['lover_ac'], 'master_ac': example2['master_ac']}
                                                collection.insert_one(s)
                                        else:
                                                example2['EXP'] += 1
                                                vk.method('messages.send', {'user_id':event.user_id,'message': 'Правильно!', 'random_id':0})
                                                if example2['user_hard'] == 'новичок':
                                                    example2['novice_ac'] += 1
                                                    coins = novice / 100 * len(str(example2['hard']))
                                                    balance += novice / 100 * len(str(example2['hard']))
                                                    novice -= novice / 100 * len(str(example2['hard']))
                                                    gen = novice_gen(example2['hard'])
                                                    my_message = gen[0]
                                                    answer = gen[1]
                                                elif example2['user_hard'] == 'любитель':
                                                    example2['lover_ac'] += 1
                                                    coins = lover / 100 * len(str(example2['hard']))
                                                    balance += lover / 100 * len(str(example2['hard']))
                                                    lover -= lover / 100 * len(str(example2['hard']))
                                                    gen = lover_gen(example2['hard'])
                                                    my_message = gen[0]
                                                    answer = gen[1]
                                                elif example2['user_hard'] == 'мастер':
                                                    example2['master_ac'] += 1
                                                    coins = master / 100 * len(str(example2['hard']))
                                                    balance += master / 100 * len(str(example2['hard']))
                                                    master -= master / 100 * len(str(example2['hard']))
                                                    gen = master_gen(example2['hard'])
                                                    my_message = gen[0]
                                                    answer = gen[1]
                                                a = {'time': event.timestamp, 'user_id': event.user_id, 'message': my_message, 'answer': str(answer), 'by_me': True}
                                                collection.insert_one(a)
                                                vk.method('messages.send', {'user_id':event.user_id,'message': str(example2['EXP']) + '/10 EXP', 'random_id':0})
                                                vk.method('messages.send', {'user_id':event.user_id,'message':'Получено ' + str(coins) + ' mathcoins', 'random_id':0})
                                                achivments(example2['novice_ac'], example2['lover_ac'], example2['master_ac'], event.user_id)
                                                vk.method('messages.send', {'user_id':event.user_id,'message': my_message, 'random_id':0})
                                                s = {'time': event.timestamp, 'user_id': event.user_id, 'message': str(event.text), 'hard' : example2['hard'], 'EXP': example2['EXP'], 'to_me': True, 'user_hard':user_hard, 'balance': balance, 'novice': novice, 'lover': lover, 'master': master, 'novice_ac': example2['novice_ac'], 'lover_ac': example2['lover_ac'], 'master_ac': example2['master_ac']}
                                                collection.insert_one(s)
                                else:
                                        vk.method('messages.send', {'user_id':event.user_id,'message': 'Неправильно!!!', 'random_id':0})
                                        answer = example['answer']
                                        if example2['EXP'] >= 2:
                                                example2['EXP'] -= 2 
                                                vk.method('messages.send', {'user_id':event.user_id,'message': str(example2['EXP']) + '/10 EXP', 'random_id':0})
                                                s = {'time': event.timestamp, 'user_id': event.user_id, 'message': str(event.text), 'hard' : example2['hard'], 'EXP': example2['EXP'], 'to_me': True, 'user_hard':user_hard, 'balance': balance, 'novice': novice, 'lover': lover, 'master': master, 'novice_ac': example2['novice_ac'], 'lover_ac': example2['lover_ac'], 'master_ac': example2['master_ac']}
                                                collection.insert_one(s)
                                        else:
                                                example2['EXP'] = 0
                                                vk.method('messages.send', {'user_id':event.user_id,'message': str(example2['EXP']) + '/10 EXP', 'random_id':0})
                                                s = {'time': event.timestamp, 'user_id': event.user_id, 'message': str(event.text), 'hard' : example2['hard'], 'EXP': example2['EXP'], 'to_me': True, 'user_hard':user_hard, 'balance': balance, 'novice': novice, 'lover': lover, 'master': master, 'novice_ac': example2['novice_ac'], 'lover_ac': example2['lover_ac'], 'master_ac': example2['master_ac']}
                                                collection.insert_one(s)
