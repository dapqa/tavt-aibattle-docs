unit bot;

interface

const
    ROCK: integer = 1; // Камень
    PAPER: integer = 2; // Бумага
    SCISSORS: integer = 3; // Ножницы

{
    Вызывается один раз перед началом игры.

    Передаёт параметры, с которыми запущен турнир:
    - setCount: максимальное количество сетов в игре
    - winsPerSet: требуемое количество побед в сете
}
procedure setParameters(setCount: integer; winsPerSet: integer);

{
    Вызывается один раз в начале игры.
}
procedure onGameStart();

{
    Функция должна вернуть число от 1 до 3, соответствующее фигуре, которую выбрал бот
    (1 - Камень, 2 - Бумага, 3 - Ножницы).

    Передаваемый параметр previousOpponentChoice - число от 1 до 3, выбор противника на предыдущем ходу.
    Самый первый раз за игру, при первом вызове choose, previousOpponentChoice равен 0
    (т.к. предыдущих ходов ещё не было).
}
function choose(previousOpponentChoice: integer): integer;

{
    Вызывается один раз в конце игры.
}
procedure onGameEnd();


implementation

procedure setParameters(setCount: integer; winsPerSet: integer);
begin
end;

procedure onGameStart();
begin
end;

function choose(previousOpponentChoice: integer): integer;
begin
    result := ROCK;
end;

procedure onGameEnd();
begin
end;

end.