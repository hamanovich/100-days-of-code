project_title = "Биология"

menu_buttons = [
    ("Ботаника", "images/botanika_logo.png"),
    ("Анатомия", "images/anatomy_logo.png"),
    ("Цитология", "images/cytology_logo.png")
]

data = {
    "Ботаника": {
        "tasks": [
            {
                "question": "При лечении заболевания сердца использовали бицилин в виде внутримышечных инъекций в ягодичную мышцу.Проследите путь перемещения лекарства в организме человека до органа мишени, выбрав все подходящие элементы из предложенных:",
                "options": [
                    (1, "Аорта"),
                    (2, "Капилляры ягодичных мышц"),
                    (3, "Нижняя полая вена"),
                    (4, "Венечная артерия сердца"),
                    (5, "Печень"),
                    (6, "Сердце (камеры)"),
                    (7, "Капилляры легких")
                ],
                "answer": "2367614"
            },
            {
                "question": "Сопоставьте слова слева с определениями справа, перетягивая их друг на друга",
                "options": [
                    ("Кислород", "Входит в состав большинства органических и многих неорганических веществ. Обеспечивает клеточное дыхание и другие окислительные процессы, в ходе которых выделяется необходимая организму энергия"),
                    ("Калий", "Участвует в генерации нервных импульсов, регули-рует ритм сердечной деятельности. Также участвует в процессе фотосинтеза"),
                    ("Магний", "Входит в состав хлорофилла, многих ферментов, а также в состав костной ткани и эмали зубов"),
                    ("Цинк", "Входит в состав инсулина и многих ферментов. Принимает участие в процессах синтеза гормонов растений"),
                    ("Кобальт", "Входит в состав витамина В12, участвует в процессах кроветворения. Необходим для синтеза хлорофилла"),
                ],
                "answer": None
            }
        ]},

    "Анатомия": {
        "tasks": [
            {
                "question": "Подпишите части глаза, перетягивая слова на нужные позиции",
                "options": [
                    ("стекловидное тело", {"x": 260, "y": 130}),
                    ("зрительный нерв", {"x": 270, "y": 315}),
                    ("передняя камера", {"x": 60, "y": 320}),
                    ("хрусталик", {"x": 85, "y": 120}),
                    ("роговица", {"x": 55, "y": 265}),
                    ("зрачок", {"x": 100, "y": 290}),
                    ("склера", {"x": 295, "y": 80}),
                    ("сетчатка", {"x": 290, "y": 105}),
                ]

            }
        ]},

    "Цитология": {
        "intro": "Цитоло́гия — раздел биологии, изучающий живые клетки, их органеллы, их строение, функционирование, процессы деления, старения и смерти.",
        "tasks": []
    },
}
