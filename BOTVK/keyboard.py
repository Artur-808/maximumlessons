from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def keyboard():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button("курс", color= VkKeyboardColor.PRIMARY)
    keyboard.add_button("погода", color= VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("команды", color=VkKeyboardColor.DEFAULT)
    keyboard.add_button("мем", color=VkKeyboardColor.DEFAULT)
    return keyboard.get_keyboard()