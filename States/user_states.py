from aiogram.fsm.state import State, StatesGroup

class CreatePosts(StatesGroup):
    CreateP = State() #нажатие на кнопку создать пост

    AwaitPost = State() #ожидание отправки пользователем контента
