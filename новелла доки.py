import random
import time
import os
import sys

characters = {
    "sayori": "Сайори",
    "natsuki": "Нацуки",
    "yuri": "Юри",
    "monika": "Моника",
    "player": "Игрок"
}

affection = {
    "sayori": 0,
    "natsuki": 0,
    "yuri": 0,
    "monika": 0
}

poem_words = {
    "sayori": ["солнце", "радость", "дружба", "улыбка", "мечта", "счастье"],
    "natsuki": ["кексы", "манга", "мило", "розовый", "сладкий", "аниме"],
    "yuri": ["книга", "тайна", "философия", "чай", "тишина", "размышление"],
    "monika": ["музыка", "будущее", "ум", "пианино", "лидер", "амбиции"]
}

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_affection():
    slow_print("\n--- Уровень привязанности ---")
    for char, points in affection.items():
        slow_print(f"{characters[char]}: {points} очков")
    print()

def poem_minigame():
    slow_print("\nПришло время писать стихотворения!")
    slow_print("Выбери слова, которые понравятся девушкам:")
    available_words = []
    for words in poem_words.values():
        available_words.extend(words)
    random.shuffle(available_words)

    player_words = []
    for i in range(5):
        slow_print(f"\nСлово {i+1}/5: {available_words[i]}")
        choice = input("Добавить это слово в стихотворение? (1 - да, 2 - нет): ").strip()
        if choice == "1":
            player_words.append(available_words[i])

    slow_print("\nТвое стихотворение:")
    poem = " ".join(player_words)
    slow_print(f"«{poem}»\n")

    for char, words in poem_words.items():
        matches = len(set(player_words) & set(words))
        if matches >= 2:
            affection[char] += matches
            slow_print(f"{characters[char]}: Мне нравится твое стихотворение! (+{matches} очков)")
    time.sleep(2)

def task_sayori():
    clear_screen()
    slow_print("СЦЕНА С САЙОРИ")
    slow_print(f"{characters['sayori']}: Привет! Поможешь мне украсить класс к фестивалю?")
    print("\n1. Конечно, с радостью!")
    print("2. Может, попозже?")
    choice = input("\nТвой выбор: ").strip()
    if choice == "1":
        slow_print(f"\n{characters['player']}: Давай сделаем наш класс самым красивым!")
        slow_print(f"\n{characters['player']}: Ты мне часто говорила о данном клубе, но никогда не рассказывала о том как ты в него вступила")
        slow_print(f"{characters['sayori']}: На самом деле ничего такого. Я просто нуууу люблю читать всякие книги и при поиске подходящего занятия случайно нашла объявление. Тогда мы были только втроем: Я, Моника и Юри; Нацуки вступи позднее меня. Не знаю мне просто нравится делиться с девочками эмоциями о прочитанных книгах, а они порой помогают это выражать на бумаге")
        slow_print(f"\n{characters['player']}:Все таки вы все такие разные: Моника-амбициозная и целеустремленная; Юри-тихая и скромная; Нацуки-олицетворение взрывной бомбы, не тяжело ли бывает? ")
        slow_print(f"{characters['sayori']}:Безусловно мы иногда ссоримся, но как правило это на почве интересов. А так своих девочек я люблю они у меня лучшие")
        slow_print(f"\n{characters['player']}:*Оттряхивая руки* Все украсил вроде, еще помощь нужна?")
        slow_print(f"{characters['sayori']}: Ура, спасибо огромное, больше ничего не нужно! Ты лучший друг!")
        affection["sayori"] += 3
        slow_print("+3 очка к привязанности Сайори")
    else:
        slow_print(f"\n{characters['sayori']}: Хорошо, я подожду...")
        affection["sayori"] += 1
        slow_print("+1 очко к привязанности Сайори")
    time.sleep(2)

def task_natsuki():
    clear_screen()
    slow_print("СЦЕНА С НАЦУКИ")
    slow_print(f"{characters['natsuki']}: Эй, поможешь мне испечь кексы для клуба?")
    print("\n1. С удовольствием!")
    print("2. Я не очень хорошо готовлю...")
    choice = input("\nТвой выбор: ").strip()
    if choice == "1":
        slow_print(f"\n{characters['player']}: Люблю твои кексы, давай вместе попробуем!")
        slow_print(f"\n{characters['player']}: А что за случай с мангой в кладовке?")
        slow_print(f"{characters['natsuki']}: Ага еще чего, стану я тебе рассказывать!")
        slow_print(f"{characters['natsuki']}: Ну ладно, так уж и быть")
        slow_print(f"{characters['natsuki']}: Просто я частенько во время перемен ходила в школьную кладовку, чтобы подальше от всех этих глупцов, почитать новый выпуск манги. Девочки увидели один раз и до сих пор смеются над этим *недовольно фыркнула*")
        slow_print(f"\n{characters['player']}: Ха-ха-ха какие серьезные действия ради обычной манги")
        slow_print(f"{characters['natsuki']}: ЭТО ДЛЯ ВАС ЭТО ПРОСТО МАНГА, ПРОСТО 'КНИЖКА С КАРТИНКАМИ', а для меня это настоящее искусство, выраженное не только в словах, но и в визуальном представлении!!! Вот что для меня литература-чувства, выраженные на бумаге.")
        slow_print(f"\n{characters['player']}: Не знал, что все настолько серьезно. Ну что ж кексы готовы!")
        slow_print(f"{characters['natsuki']}:Можешь взять попробовать. НО МНЕ ХОТЬ ПАРУ ШТУЧЕК ОСТАВЬ!!!^")
        affection["natsuki"] += 3
        slow_print("+3 очка к привязанности Нацуки")
    else:
        slow_print(f"\n{characters['natsuki']}: Ну и ладно! Больше кексов мне!")
        affection["natsuki"] += 1
        slow_print("+1 очко к привязанности Нацуки")
    time.sleep(2)

def task_yuri():
    clear_screen()
    slow_print(" СЦЕНА С ЮРИ ")
    slow_print(f"{characters['yuri']}: ...Я принесла новый сборник стихов. Хочешь почитать вместе?")
    print("\n1. Да, с удовольствием")
    print("2. Я не очень разбираюсь в поэзии")
    choice = input("\nТвой выбор: ").strip()
    if choice == "1":
        slow_print(f"\n{characters['player']}: Интересно, о чем эта книга...")
        slow_print(f"{characters['yuri']}: О-нна о философии в природе")
        slow_print(f"\n{characters['player']}: Не знал, что тебе такое нравится. Ты всегда мало говоришь")
        slow_print(f"{characters['yuri']}: *немного застенчиво* не знаю это с детства, просто стесняюсь в компаниях боюсь как-то привлечь к себе внимание")
        slow_print(f"\n{characters['player']}: Не знаю... Ты очень красивая девушка еще и с прекрасным голосом, главное говори погромче! ")
        slow_print(f"{characters['yuri']}:*мягко улыбнувшись* хи-хи обязательно")
        slow_print(f"{characters['player']}: мне нравятся эти стихи, посоветуешь что-то еще?)")
        slow_print(f"{characters['yuri']}:обязательно! главное приходи к нам почаще")
        affection["yuri"] += 3
        slow_print("+3 очка к привязанности Юри")
    else:
        slow_print(f"\n{characters['yuri']}: Понимаю... Может, в другой раз...")
        affection["yuri"] += 1
        slow_print("+1 очко к привязанности Юри")
    time.sleep(2)

def task_monika():
    clear_screen()
    slow_print("СЦЕНА С МОНИКОЙ")
    slow_print(f"{characters['monika']}: Наш клуб растет! Поможешь мне организовать встречу для новых членов?")
    print("\n1. Конечно, президент!")
    print("2. Я помогу, чем смогу")
    choice = input("\nТвой выбор: ").strip()
    if choice == "1":
        slow_print(f"\n{characters['player']}: Всегда рад помочь клубу!")
        slow_print(f"{characters['monika']}: Спасибо! Ты очень надежный!")
        slow_print(f"\n{characters['player']}: Тяжеловато наверное быть главой, хоть небольшого, но клуба")
        slow_print(f"\n{characters['player']}:Мне нет, мне всегда нравилось заниматься различной организационной работой. Поэтому я клуб и создала, чтобы чем-то подобным заниматься, при этом в рамках моих любимых вещей-книг")
        slow_print(f"\n{characters['player']}: А чем ты еще занимешься помимо всей организации и книг")
        slow_print(f"\n{characters['player']}:*слегка смущаясь* Честно признаться я обожаю музыку. С самых ранних лет я играю на пианино-инструменте который меня заворажиивает до глубины души")
        slow_print(f"\n{characters['player']}: А вот и возможно новые ребята, пойдем с ниими познакомимся")
        affection["monika"] += 3
        slow_print("+3 очка к привязанности Моники")
    else:
        slow_print(f"\n{characters['monika']}: Спасибо за помощь в любом случае!")
        affection["monika"] += 2
        slow_print("+2 очка к привязанности Моники")
    time.sleep(2)

def peaceful_ending():
    clear_screen()
    slow_print("ПОЗДРАВЛЯЕМ!")
    slow_print("Литературный клуб процветает!")
    slow_print("Все девушки счастливы и продолжают заниматься творчеством.\n")
    max_affection = max(affection.values())
    best_girls = [char for char, points in affection.items() if points == max_affection]
    if len(best_girls) == 1:
        girl = best_girls[0]
        slow_print(f"Особенно крепкая дружба у тебя сложилась с {characters[girl]}!")
    else:
        slow_print("У тебя сложились прекрасные дружеские отношения со всеми!")
    slow_print("\nСпасибо, что стал частью нашего клуба!")
    show_affection()

def main_game():
    clear_screen()
    slow_print("ДОБРО ПОЖАЛОВАТЬ В ЛИТЕРАТУРНЫЙ КЛУБ!")
    slow_print("Это мирная версия игры, где все счастливы!")
    player = input("Привет, для начала прохождения новеллы введи свое имя: ").strip()
    characters["player"] = player
    slow_print(f"Приятно познакомиться, {player}, приступим к прохождению!")
    slow_print("/на улице стоял теплый солнечный день/")
    slow_print("/Я уже стою в ожидании своей давней школьной подруги-Саери/")
    slow_print("/С Саери мы знакомы еще с младшей школы и у нас даже появилась небольшая традиция: каждый день я встречаю ее на углу-около фонарного столба и она как обычно всегда опаздывает/")
    slow_print("/И в этот раз тоже.../")
    slow_print(f"{characters['sayori']}: *выдыхает после своей пробежки* Приветик!!! Я не сильно опоздала?(")
    slow_print("Саери совсем не меняется, все те же розовые волосы длиной до подбородка, срезанные и слегка завитые на концах, но в последнее время на левой стороне ее головы у нее был большой красный бант, а рядом с чёлкой у неё две заметные пряди волос. Глаза же ярко-голубого цвета и она все такая же низкая как и раньше...")
    slow_print(f"{player}: Все как обычно. Ровно на 15 минут.")
    slow_print(f"{characters['sayori']}: Извинии, просто вся эта подготовка убивает мой сон")
    slow_print(f"{player}: Какая подготовка?...")
    slow_print(f"{characters['sayori']}: Ну как же подготовка к весеннему фестивалю в нашем литературном клубе!!!")
    slow_print(f"{player}: О боже опять твой дурацкий клуб *тяжело вздыхает*")
    slow_print(f"{characters['sayori']}: Ну кстати на самом деле у нас совсем мало членов в клубе и нам явно не помешала бы твоя помощь)))")
    slow_print(f"{player}: Да не хочу я. Я даже ничего не понимаю в вашей бессмысленной литературе")
    slow_print(f"{characters['sayori']}: Ну пожааааааууйста, {player}, нам очень сильно нужна помощь!!! У нас очень приятная атмосфера в клубе и много чая с кексами!!!^^ *жалостливо смотрит*")
    
    choice = input("1 - Ну ладно так уж и быть я приду \n2 - Нет, не хочу\n> ").strip()
    if choice == "2":
        print("/После уроков я пошел спокойно домой, ожидая поскорее наступающих летних каникул/")
        print("*Вами была открыта альтернативная концовка! 'Этим днем ничего не произошло'*")
        input()
        sys.exit(0)
    elif choice == "1":
        slow_print("/после уроков/")
        slow_print(f"{player}: *я удрученно поплелся за Саери в этот ее дурацкий клуб*")
        slow_print(f"{player}:*Я не мог понять зачем она тащит меня сюда*")
        slow_print(f"{player}:*Может поскорее сбежать пока еще не поздно...*")
        slow_print("/Двери открываются/")
        slow_print(f"{player}:*Походу поздно...*")
        slow_print(f"{characters['sayori']}:Всем привеееет! Я кажется привела вам нового участника нашего клуба!!!")
        slow_print(f"{characters['monika']}:Хахахаха, Сайори успокойся и познакомь лучше нас")
        slow_print("/Моника стояла у окна скрестив руки на груди. Она держалась твердо и статно. Ее зеленые глаза отдавали каким-то необычным блеском, будто бы показывая всю силу и твердость характера этой девушки./")
        slow_print(f"{characters['sayori']}:Ой точно...Моника, Юри, Нацуки знакомьтесь - {player} теперь член нашего литературного клуба")
        slow_print(f"{player}:Это пока не точно.")
        slow_print(f"{characters['monika']}:Приятно познакомиться {player}! Я-Моника, глава литературного клуба. Юри-самая старшая из нас")
        slow_print("/Передо мной стояла высокая девушка с темно-фиолетовыми волосами и такого же цвета глазами. Судя по ее робкому взгляду на меня она явно была очень скромной и не часто общается с людьми/")
        slow_print(f"{characters['yuri']}:*небольшое молчание* Я-Юр-рри ")
        slow_print(f"{characters['monika']}:Ну и конечно как же без нашего главного кондитера клуба-Нацуки *смеясь*")
        slow_print(f"{characters['natsuki']}:*начинается запыхаться от злости* Я ВАМ ЧТО ПОВАР НА ВСЕХ?! Я МЕЖДУ ПРОЧИМ НЕ ТОЛЬКО НА ВСЕХ ВАС ГОТОВЛЮ!!! У МЕНЯ И ДРУГИЕ ИНТЕРЕСЫ ЕСТЬ!!!!")
        slow_print(f"{characters['sayori']}: Как например прочтение манги в школьной кладовке?)")
        slow_print(f"{characters['natsuki']}:ДА ЧТО ВЫ ПОНИМАЕТЕ ВООБЩЕ!!! МАНГА МЕЖДУ ПРОЧИМ ТОЖЕ ЛИТЕРАТУРА!!! ")
        slow_print("/Нацуки по внешнему виду казалась хрупкой и беззащитной девушкой. Она была невысокого роста с короткой розовой прической и светлыми глазами. Однако столько дерзости и какой-то злости, от которой хочется только умиляться вместо страха, я еще ни у кого не видел/")
        slow_print(f"{characters['monika']}:А с Сайори я так понимаю вы уже давно знакомы *Хитро посмотрела на Саери*")
        slow_print(f"{characters['sayori']}:*смутилась и отвернула от меня голову* Ну я просто иногда рассказывала о тебе своим подругам")
        slow_print(f"{player}:Приятно познакомиться, я не знаю я пока еще не уверен хочу ли я вступить...Тем более я не особо лажу с данным предметом")
        slow_print(f"{characters['natsuki']}: Мальчики безнадежны... *тяжело вздыхает* Вы пытаетесь 'понять' литературу, а ее надо ЧУВСТВОВАТЬ, ничего вы как обычно не умеете")
        slow_print(f"{characters['sayori']}:Ну вот как раз научим его!")
        slow_print(f"{player}:Я еще ни на что не соглашался!")
        slow_print(f"{characters['natsuki']}:А тебя и никто и не спрашивает! Тем более нам сейчас нужна помощь для подготовки. Вот тут ты и понадобишься ")
        slow_print(f"{characters['sayori']}: Ну пожалуйста останься ")
        slow_print(f"{characters['monika']}:Просто попробуй. Мы не кусаемся *мило смеется*, но на самом деле лишняя помощь не помешает")
        slow_print(f"{characters['yuri']}: *стоя дальше всех, тихо произнесла* Останься с нами. Тебе понравится")
        slow_print(f"{player}:*Задумался* ну... хорошо.")
        slow_print(f"{characters['monika']}: Тогда добро пожаловать в наш славный литератрный клуб!")

    days = ["Понедельник", "Вторник", "Среда", "Четверг"]
    for day in days:
        clear_screen()
        slow_print(f"\n=== {day.upper()} ===")
        tasks = [task_sayori, task_natsuki, task_yuri, task_monika]
        random_task = random.choice(tasks)
        random_task()
        poem_minigame()
        show_affection()
        if day != days[-1]:
            input("\nНажми Enter для продолжения...")

    peaceful_ending()

if __name__ == "__main__":
    try:
        main_game()
    except KeyboardInterrupt:
        slow_print("\n\nИгра прервана. Возвращайся в литературный клуб скоро!")
