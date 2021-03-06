import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import goroskop
from боты.config import VK_TOKEN, group_id


def main():
    vk_session = vk_api.VkApi(
        token=str(VK_TOKEN))


    date = '00.00.0000'
    longpoll = VkBotLongPoll(vk_session, int(group_id))

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])

            print('Текст:', event.obj.message['text'])
            vk = vk_session.get_api()
            if 'начать' in event.obj.message['text'].lower():
                user = vk.users.get(user_id=event.obj.message['from_id'], fields="bdate")
                user = user[0]
                vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f'Привет, {user["first_name"]} {user["last_name"]}.'
                                             f'Ваш год рождения {user["bdate"]}?',
                                     random_id=random.randint(0, 2 ** 64))
                date = user["bdate"]
            elif 'дата:' in event.obj.message['text'].lower():
                print('ответ на сообщение')
                date = event.obj.message['text'].split()[1]
                print(f'текущая дата {date}')
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f'Вы уверенны?',
                                 random_id=random.randint(0, 2 ** 64))
            elif 'да' in event.obj.message['text'].lower():
                date = date.split('.')
                m, d = int(date[1]), int(date[0])
                goros = goroskop.z_s(goroskop.zodiac_sign(m, d))
                for i in goros.keys():
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f'{i}:{goros[i]}',
                                     random_id=random.randint(0, 2 ** 64))
            elif 'нет' in event.obj.message['text'].lower():
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f'напишите ваш год рождения ответом на это сообщение в формате\n'
                                         f'дата: день-месяц-год',
                                 random_id=random.randint(0, 2 ** 64))

            else:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f'напишите да, нет или начать',
                                 random_id=random.randint(0, 2 ** 64))





if __name__ == '__main__':
    main()



