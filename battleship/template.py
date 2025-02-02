# Коды результатов выстрела:
SHOT_RESULT_EMPTY: int = 0  # Промах
SHOT_RESULT_DAMAGE: int = 2  # Корабль соперника ранен (подбит)
SHOT_RESULT_KILL: int = 3  # Корабль соперника убит (подбиты все палубы)

last_shot_idx = 0


def set_parameters(set_count: int) -> None:
    """
    Вызывается один раз перед началом игры.
    Передаёт параметры, с которыми запущен турнир.

    :param set_count: максимальное количество сетов в игре
    """
    pass


def on_game_start() -> None:
    """Вызывается один раз в начале игры."""
    pass


def on_set_start() -> None:
    """Вызывается один раз в начале сета."""
    global last_shot_idx
    last_shot_idx = 0


def get_map() -> list[list[int]]:
    """
    Возвращает карту с расстановкой кораблей.
    Вызывается в начале каждого сета (каждый сет можно делать новую расстановку).

    Карта должна иметь размер 10х10 и быть заполнена следующим образом:
    - 0 - пустая клетка
    - 1 - клетка с палубой корабля

    На карте должно быть четыре 1-палубника, три 2-палубника, два 3-палубника и один 4-палубник.
    Корабли должны быть расположены строго вертикально или горизонтально (т.е., не иметь изгибов).
    Корабли не должны соприкасаться.

    :return: Карта с расстановкой кораблей для текущего сета
    """
    return [
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]


def shoot() -> tuple[int, int]:
    """
    Возвращает координаты клетки, в которую на текущем ходу стреляет бот.

    Координаты задаются массивом из двух целых чисел.
    Первая соответствует строке (координата по вертикали), вторая - столбцу (координата по горизонтали).
    Отсчёт ведётся с левого верхнего угла.
    Т.е., чтобы выстрелить в клетку map[i][j], необходимо вернуть [i, j].

    Результат выстрела будет гарантированно передан следующим вызовом через shot_result.

    :return: Координаты выстрела
    """
    global last_shot_idx

    result = last_shot_idx // 10, last_shot_idx % 10
    last_shot_idx = last_shot_idx + 1
    return result


def shot_result(result_code: int) -> None:
    """
    Вызывается сразу после shoot, чтобы передать результат выстрела.
    Возможные значения result_code:
    - 0 - Промах
    - 2 - Корабль соперника ранен (подбит)
    - 3 - Корабль соперника убит (подбиты все палубы)

    :param result_code: Код результата выстрела
    """
    pass


def on_opponent_shot(cell: tuple[int, int]) -> None:
    """
    Вызывается после выстрела соперника.
    :param cell: Координаты клетки, в которую выстрелил соперник
    """
    pass


def on_set_end() -> None:
    """Вызывается один раз в конце сета."""
    pass


def on_game_end() -> None:
    """Вызывается один раз в конце игры."""
    pass