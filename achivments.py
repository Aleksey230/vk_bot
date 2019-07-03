import vk_api
def achivments(novice_ac, lover_ac, master_ac, user_id):
    token = 'a05a0530ccb33113ba4f326de748a5d83b0a851a50ecbc23bbec5c5eeb7c839cc77387fa8e23ab41a300e'
    vk = vk_api.VkApi(token=token)
    if novice_ac == 50:
        vk.method('messages.send', {'user_id': user_id, 'message': 'Получено достижение', 'random_id': 0, 'attachment': 'photo359760458_456239278'})
    elif novice_ac == 100:
        vk.method('messages.send', {'user_id': user_id, 'message': 'Получено достижение', 'random_id': 0, 'attachment': 'photo359760458_456239282'})
    elif novice_ac == 500:
        vk.method('messages.send', {'user_id': user_id, 'message': 'Получено достижение', 'random_id': 0, 'attachment': 'photo359760458_456239285'})
    elif novice_ac == 1000:
        vk.method('messages.send', {'user_id': user_id, 'message': 'Получено достижение', 'random_id': 0, 'attachment': 'photo359760458_456239288'})
    elif lover_ac == 50:
        vk.method('messages.send', {'user_id': user_id, 'message': 'Получено достижение', 'random_id': 0, 'attachment': 'photo359760458_456239279'})
    elif lover_ac == 100:
        vk.method('messages.send', {'user_id': user_id, 'message': 'Получено достижение', 'random_id': 0, 'attachment': 'photo359760458_456239280'})
    elif lover_ac == 500:
        vk.method('messages.send', {'user_id': user_id, 'message': 'Получено достижение', 'random_id': 0, 'attachment': 'photo359760458_456239283'})
    elif lover_ac == 1000:
        vk.method('messages.send', {'user_id': user_id, 'message': 'Получено достижение', 'random_id': 0, 'attachment': 'photo359760458_456239286'})
    elif master_ac == 50:
        vk.method('messages.send', {'user_id': user_id, 'message': 'Получено достижение', 'random_id': 0, 'attachment': 'photo359760458_456239277'})
    elif master_ac == 100:
        vk.method('messages.send', {'user_id': user_id, 'message': 'Получено достижение', 'random_id': 0, 'attachment': 'photo359760458_456239281'})
    elif master_ac == 500:
        vk.method('messages.send', {'user_id': user_id, 'message': 'Получено достижение', 'random_id': 0, 'attachment': 'photo359760458_456239284'})
    elif master_ac == 1000:
        vk.method('messages.send', {'user_id': user_id, 'message': 'Получено достижение', 'random_id': 0, 'attachment': 'photo359760458_456239287'})
