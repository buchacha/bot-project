import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

def main():
    """ Пример создания клавиатуры для отправки ботом """

    vk_session = vk_api.VkApi(token='17fa5a630542a07af7cc2dfafe25e803519b13eb8fc2d08747b840e4e73ec48ad965faa2915f1b92832e6')
    vk = vk_session.get_api()

    keyboard = VkKeyboard(one_time=True)

    keyboard.add_button('Белая кнопка', color=VkKeyboardColor.DEFAULT)
    keyboard.add_button('Зелёная кнопка', color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()  # Переход на вторую строку
    keyboard.add_location_button()

    keyboard.add_line()
    keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=74030368&aid=6222115")

    keyboard.add_line()
    keyboard.add_vkapps_button(app_id=6979558,
                               owner_id=-181108510,
                               label="Отправить клавиатуру",
                               hash="sendKeyboard")

    vk.messages.send(
        peer_id=123456,
        random_id=get_random_id(),
        keyboard=keyboard.get_keyboard(),
        message='Пример клавиатуры'
    )


if __name__ == '__main__':
    main()
