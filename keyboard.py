from vk_api.keyboard import VkKeyboard


kb = VkKeyboard()
kb.add_button("Дай пример", 'negative')
kb.add_button("Помощь", 'secondary')
kb.add_button("Баланс", 'primary')
kb.add_line()

kb.add_button("Новичок", 'positive')
kb.add_button("Любитель", 'primary')
kb.add_button("Мастер", 'negative')

kb = kb.get_keyboard()
