ROCK = 1  # Камень
PAPER = 2  # Бумага
SCISSORS = 3  # Ножницы


def set_parameters(set_count: int, wins_per_set: int) -> None:
    """
    Вызывается один раз перед началом игры.
    Передаёт параметры, с которыми запущен турнир.

    :param set_count: Максимальное количество сетов в игре
    :param wins_per_set: Требуемое количество побед в сете
    """
    pass


def on_game_start() -> None:
    """ Вызывается один раз в начале игры. """
    pass


def choose(previous_opponent_choice: int) -> int:
    """
    Функция должна вернуть число от 1 до 3, соответствующее фигуре, которую выбрал бот
    (1 - Камень, 2 - Бумага, 3 - Ножницы).

    Передаваемый параметр previous_opponent_choice - число от 1 до 3, выбор противника на предыдущем ходу.
    Самый первый раз за игру, при первом вызове choose, previous_opponent_choice равен 0
    (т.к. предыдущих ходов ещё не было).

    :param previous_opponent_choice: Код фигуры, выбранной противником на предыдущем ходу
    :return: Код фигуры, которую выбирает бот
    """
    return ROCK


def on_game_end() -> None:
    """ Вызывается один раз в конце игры. """
    pass