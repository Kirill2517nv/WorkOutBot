# Все тренировки программы калистеники 12 недель
# Структура: phase1/2/3 × A/B/C = 9 тренировок в цикле

WORKOUTS = {
    "phase1_A": {
        "title": "Фаза 1 — Тренировка А (Тяга + горизонт + горизонт сзади)",
        "exercises": [
            {
                "name": "Бег",
                "sets": 1,
                "target": "30 мин",
                "input_type": "free",
                "prompt": "Сколько минут пробежал?",
                "description": "Разминочный бег перед тренировкой.",
            },
            {
                "name": "Scapular pull-ups",
                "sets": 3,
                "target": "10 повт",
                "input_type": "reps",
                "description": (
                    "Висишь на турнике на прямых руках, локти не сгибаешь. "
                    "Тянешь плечи вниз к бёдрам и чуть сводишь лопатки — тело немного приподнимается. "
                    "Потом отпускаешь. Только лопатки, тело неподвижно."
                ),
            },
            {
                "name": "Tuck front lever hold",
                "sets": 5,
                "target": "8–12 сек",
                "input_type": "time",
                "description": (
                    "Висишь на турнике, прижимаешь колени к груди, поднимаешь тело горизонтально. "
                    "Плечи вдавлены вниз и назад, таз чуть подкручен. "
                    "Ощущение — как будто давишь турником к земле. Отдых 2–3 мин."
                ),
            },
            {
                "name": "Skin the cat",
                "sets": 3,
                "target": "5–6 повт",
                "input_type": "reps",
                "description": (
                    "Висишь на турнике. Поднимаешь ноги и проносишь их назад сквозь руки, "
                    "вытягиваясь вниз головой. Потом возвращаешься. Медленно, без рывков."
                ),
            },
            {
                "name": "Tuck back lever hold",
                "sets": 4,
                "target": "8–12 сек",
                "input_type": "time",
                "description": (
                    "В нижней точке skin the cat прижимаешь колени к груди и поднимаешь "
                    "тело горизонтально лицом вниз. Руки прямые. Плечи тянутся — это нормально."
                ),
            },
            {
                "name": "Подтягивания (weighted / узкий хват)",
                "sets": 4,
                "target": "5–7 повт",
                "input_type": "reps_weight",
                "description": (
                    "С добавленным весом (пояс с блином, рюкзак) или узким хватом. "
                    "Из полного виса до подбородка выше турника, медленно вниз."
                ),
            },
            {
                "name": "Австралийские тяги",
                "sets": 3,
                "target": "10–12 повт",
                "input_type": "reps",
                "description": (
                    "Турник на высоте пояса–груди. Ложишься под него, держишься, тело прямое. "
                    "Тянешь грудь к перекладине, опускаешься. Чем горизонтальнее тело — тем тяжелее."
                ),
            },
            {
                "name": "Подъём прямых ног в висе",
                "sets": 3,
                "target": "8–10 повт",
                "input_type": "reps",
                "description": (
                    "Висишь на турнике. Поднимаешь прямые ноги до горизонтали или выше без раскачки."
                ),
            },
            {
                "name": "Seated leg raises",
                "sets": 3,
                "target": "15–20 повт",
                "input_type": "reps",
                "description": (
                    "Садишься на скамью или пол, руки рядом сзади. Поднимаешь прямые ноги "
                    "на 20–30 см и опускаешь. Медленно. Ключевое упражнение против судорог в L-sit."
                ),
            },
            {
                "name": "Hollow body hold",
                "sets": 3,
                "target": "20–25 сек",
                "input_type": "time",
                "description": (
                    "Ложишься на спину, поясница прижата к полу. Руки вытянуты за голову, "
                    "ноги под углом 30–45°. Форма «чаши». Не задерживай дыхание."
                ),
            },
        ],
    },

    "phase1_B": {
        "title": "Фаза 1 — Тренировка Б (Толчок + планш + L-sit)",
        "exercises": [
            {
                "name": "Бег",
                "sets": 1,
                "target": "30 мин",
                "input_type": "free",
                "prompt": "Сколько минут пробежал?",
                "description": "Разминочный бег перед тренировкой.",
            },
            {
                "name": "Planche lean",
                "sets": 4,
                "target": "12–15 сек",
                "input_type": "time",
                "description": (
                    "Стоишь в упоре, пальцы смотрят в стороны или назад. Медленно переносишь "
                    "вес вперёд — плечи уходят за линию рук. Лопатки не сводишь, а выталкиваешь "
                    "вперёд и вниз (округлённые плечи). Держишь."
                ),
            },
            {
                "name": "Frog stand (лягушка)",
                "sets": 5,
                "target": "10–15 сек",
                "input_type": "time",
                "description": (
                    "Приседаешь, ставишь ладони на пол. Колени кладёшь на трицепсы. "
                    "Переносишь вес на руки и отрываешь ноги. Балансируешь. Лучше на параллетках."
                ),
            },
            {
                "name": "Tuck L-sit на брусьях",
                "sets": 4,
                "target": "максимум сек",
                "input_type": "time",
                "description": (
                    "Берёшься за брусья, жмёшь вниз, приподнимаешь себя. Прижимаешь колени к груди. "
                    "Плечи давят вниз, не к ушам. Держишь сколько можешь."
                ),
            },
            {
                "name": "Отжимания на брусьях с весом",
                "sets": 4,
                "target": "6–8 повт",
                "input_type": "reps_weight",
                "description": (
                    "Пояс с блином или рюкзак. Полная амплитуда. Локти немного в стороны, не вперёд."
                ),
            },
            {
                "name": "Pike push-ups",
                "sets": 3,
                "target": "8–10 повт",
                "input_type": "reps",
                "description": (
                    "Позиция перевёрнутой V: таз высоко, ноги и руки прямые. "
                    "Медленно опускаешь голову между руками к полу и жмёшь обратно. 3 сек вниз."
                ),
            },
            {
                "name": "Archer push-ups (лучник)",
                "sets": 3,
                "target": "6–8 повт на каждую сторону",
                "input_type": "reps",
                "description": (
                    "Широкая постановка рук. Опускаешься в одну сторону — та рука сгибается, "
                    "вторая остаётся прямой. Поднимаешься и переходишь на другую сторону."
                ),
            },
            {
                "name": "L-sit попытки (tuck → одна нога → обе)",
                "sets": 4,
                "target": "максимум",
                "input_type": "time",
                "description": (
                    "Начинай с tuck. Если держишь 10+ сек — выпрями одну ногу, потом другую. "
                    "Много коротких подходов лучше одного долгого через судороги."
                ),
            },
            {
                "name": "Pike compression",
                "sets": 3,
                "target": "20–30 сек",
                "input_type": "time",
                "description": (
                    "Садишься на пол, ноги прямые. Наклоняешься и тянешь грудь к ногам, держишь."
                ),
            },
            {
                "name": "Dragon flag негативы",
                "sets": 3,
                "target": "3–4 повт",
                "input_type": "reps",
                "description": (
                    "Ложишься на скамью, держишься за края. Поднимаешь тело вертикально, "
                    "потом медленно (4–5 сек) опускаешь горизонтально не касаясь скамьи."
                ),
            },
        ],
    },

    "phase1_C": {
        "title": "Фаза 1 — Тренировка В (Повтор скиллов + полное тело)",
        "exercises": [
            {
                "name": "Бег",
                "sets": 1,
                "target": "30 мин",
                "input_type": "free",
                "prompt": "Сколько минут пробежал?",
                "description": "Разминочный бег перед тренировкой.",
            },
            {
                "name": "Front lever review (tuck)",
                "sets": 3,
                "target": "8–10 сек",
                "input_type": "time",
                "description": "Tuck front lever. Чисто, без максимального напряжения.",
            },
            {
                "name": "Back lever review (tuck)",
                "sets": 3,
                "target": "8–10 сек",
                "input_type": "time",
                "description": "Tuck back lever. Вход через skin the cat.",
            },
            {
                "name": "Planche lean (повтор)",
                "sets": 3,
                "target": "10–12 сек",
                "input_type": "time",
                "description": "Повтор. Контролируешь протракцию лопаток (округлены вперёд, не сведены).",
            },
            {
                "name": "Взрывные подтягивания",
                "sets": 3,
                "target": "5–6 повт",
                "input_type": "reps",
                "description": (
                    "Тянешь себя максимально резко — цель оторвать руки от перекладины в верхней точке. "
                    "Полная амплитуда. Достаточный отдых."
                ),
            },
            {
                "name": "Muscle-up негативы",
                "sets": 3,
                "target": "2–3 повт",
                "input_type": "reps",
                "description": (
                    "Заходишь в упор на турнике (с прыжка). Из упора медленно (4–5 сек) "
                    "перебрасываешь запястья и опускаешься в вис."
                ),
            },
            {
                "name": "Отжимания на брусьях без веса",
                "sets": 3,
                "target": "12–15 повт",
                "input_type": "reps",
                "description": "Большой объём, без утяжеления. Техника та же.",
            },
            {
                "name": "L-sit на брусьях",
                "sets": 3,
                "target": "максимум",
                "input_type": "time",
                "description": "Лучшая прогрессия которую можешь держать. Записывай время.",
            },
            {
                "name": "Подъём прямых ног в висе (объём)",
                "sets": 3,
                "target": "10–12 повт",
                "input_type": "reps",
                "description": "Как в тренировке А, чуть больше повторений.",
            },
        ],
    },

    "phase2_A": {
        "title": "Фаза 2 — Тренировка А (Тяга + горизонт + горизонт сзади)",
        "exercises": [
            {
                "name": "Бег",
                "sets": 1,
                "target": "30 мин",
                "input_type": "free",
                "prompt": "Сколько минут пробежал?",
                "description": "Разминочный бег.",
            },
            {
                "name": "Advanced tuck front lever hold",
                "sets": 5,
                "target": "8–12 сек",
                "input_type": "time",
                "description": (
                    "Как tuck FL, но бёдра не прижаты к груди — они перпендикулярны телу (~90°). "
                    "Колени по-прежнему согнуты, но рычаг длиннее."
                ),
            },
            {
                "name": "One-leg front lever (попытки)",
                "sets": 3,
                "target": "3–5 сек",
                "input_type": "time",
                "description": (
                    "Одна нога вытянута горизонтально, вторая согнута. "
                    "Первые попытки — пробуешь, не держишь до отказа."
                ),
            },
            {
                "name": "Adv. tuck back lever → Straddle BL",
                "sets": 5,
                "target": "8–12 сек",
                "input_type": "time",
                "description": (
                    "Начинаешь с advanced tuck BL (бёдра опущены). "
                    "Когда держишь уверенно — пробуешь развести ноги в стороны (straddle)."
                ),
            },
            {
                "name": "Straddle back lever (первые попытки)",
                "sets": 3,
                "target": "3–5 сек",
                "input_type": "time",
                "description": (
                    "Ноги прямые и разведены, тело горизонтально лицом вниз. "
                    "Если не держишь — возвращаешься к advanced tuck."
                ),
            },
            {
                "name": "Weighted pull-ups",
                "sets": 4,
                "target": "5–6 повт",
                "input_type": "reps_weight",
                "description": "Подтягивания с весом, чуть тяжелее чем в фазе 1.",
            },
            {
                "name": "Chest-to-bar pull-ups",
                "sets": 4,
                "target": "4–5 повт",
                "input_type": "reps",
                "description": "Подтягивания до груди — грудь касается перекладины. Без веса.",
            },
            {
                "name": "Toes-to-bar",
                "sets": 3,
                "target": "8–10 повт",
                "input_type": "reps",
                "description": "Висишь на турнике, носки касаются перекладины. Полная амплитуда.",
            },
            {
                "name": "Compression holds",
                "sets": 3,
                "target": "20–30 сек",
                "input_type": "time",
                "description": "Сидишь, поднимаешь прямые ноги и держишь. Можно на параллетках.",
            },
            {
                "name": "Hollow body + рокинг",
                "sets": 3,
                "target": "20–30 сек",
                "input_type": "time",
                "description": (
                    "Позиция hollow body, но раскачиваешься вперёд-назад как кресло-качалка, "
                    "не меняя форму."
                ),
            },
        ],
    },

    "phase2_B": {
        "title": "Фаза 2 — Тренировка Б (Толчок + планш + L-sit)",
        "exercises": [
            {
                "name": "Бег",
                "sets": 1,
                "target": "30 мин",
                "input_type": "free",
                "prompt": "Сколько минут пробежал?",
                "description": "Разминочный бег.",
            },
            {
                "name": "Tuck planche hold (параллетки)",
                "sets": 5,
                "target": "5–8 сек",
                "input_type": "time",
                "description": (
                    "Колени к груди, тело не опирается. Плечи максимально впереди кистей, "
                    "лопатки выдавлены вперёд. Параллетки дают нужную глубину."
                ),
            },
            {
                "name": "Planche lean (удлинённый)",
                "sets": 4,
                "target": "15–20 сек",
                "input_type": "time",
                "description": "Как в фазе 1, но дольше и с более сильным наклоном.",
            },
            {
                "name": "Full L-sit на брусьях",
                "sets": 5,
                "target": "максимум (цель 20+ сек)",
                "input_type": "time",
                "description": "Обе ноги вытянуты горизонтально. Носки тянешь, ноги прямые.",
            },
            {
                "name": "Weighted dips",
                "sets": 4,
                "target": "6–8 повт",
                "input_type": "reps_weight",
                "description": "Отжимания на брусьях с весом.",
            },
            {
                "name": "Pike HSPU",
                "sets": 3,
                "target": "6–8 повт",
                "input_type": "reps",
                "description": (
                    "Ноги на возвышении (скамья), позиция pike. Тело более вертикально. "
                    "Опускаешь голову к полу между руками и жмёшь."
                ),
            },
            {
                "name": "Tuck planche push-ups",
                "sets": 3,
                "target": "4–5 повт",
                "input_type": "reps",
                "description": "Отжимания из позиции tuck planche. Тело не касается пола.",
            },
            {
                "name": "L-sit цель 20+ сек",
                "sets": 4,
                "target": "максимум",
                "input_type": "time",
                "description": "Full L-sit. Фиксируй рекорд.",
            },
            {
                "name": "Front lever raises (tuck)",
                "sets": 3,
                "target": "5 повт",
                "input_type": "reps",
                "description": (
                    "Висишь в tuck front lever, опускаешься в вис и поднимаешься обратно. "
                    "Медленно и под контролем."
                ),
            },
            {
                "name": "Dragon flag",
                "sets": 3,
                "target": "3–5 повт",
                "input_type": "reps",
                "description": (
                    "Полная версия: поднимаешь тело вертикально и опускаешь горизонтально, "
                    "потом возвращаешься. Тело прямое как доска."
                ),
            },
        ],
    },

    "phase2_C": {
        "title": "Фаза 2 — Тренировка В (Повтор скиллов + muscle-up)",
        "exercises": [
            {
                "name": "Бег",
                "sets": 1,
                "target": "30 мин",
                "input_type": "free",
                "prompt": "Сколько минут пробежал?",
                "description": "Разминочный бег.",
            },
            {
                "name": "FL review (advanced tuck)",
                "sets": 3,
                "target": "8–10 сек",
                "input_type": "time",
                "description": "Advanced tuck front lever. Без максимального напряжения.",
            },
            {
                "name": "BL review (adv. tuck / straddle)",
                "sets": 3,
                "target": "8 сек",
                "input_type": "time",
                "description": "Лучшая прогрессия которую держишь уверенно.",
            },
            {
                "name": "Tuck planche review",
                "sets": 3,
                "target": "5–6 сек",
                "input_type": "time",
                "description": "Повтор tuck planche. Проверяешь позицию лопаток.",
            },
            {
                "name": "Muscle-up (kipping → чистый)",
                "sets": 3,
                "target": "1–3 повт",
                "input_type": "reps",
                "description": (
                    "В начале фазы с рывком бёдрами, к концу — стремишься к чистому без рывка."
                ),
            },
            {
                "name": "Подтягивания (разные хваты)",
                "sets": 3,
                "target": "8–10 повт",
                "input_type": "reps",
                "description": "Чередуй: нейтральный хват, обратный хват, широкий. Без веса.",
            },
            {
                "name": "Отжимания на брусьях (фаза 2)",
                "sets": 3,
                "target": "10–12 повт",
                "input_type": "reps",
                "description": "Без веса, средний объём.",
            },
            {
                "name": "L-sit рекорд",
                "sets": 4,
                "target": "максимум",
                "input_type": "time",
                "description": "Пробуешь побить личный рекорд в full L-sit.",
            },
            {
                "name": "Toes-to-bar (фаза 2, повтор)",
                "sets": 3,
                "target": "8–10 повт",
                "input_type": "reps",
                "description": "Как в тренировке А этой фазы.",
            },
        ],
    },

    "phase3_A": {
        "title": "Фаза 3 — Тренировка А (Тяга + горизонт + горизонт сзади)",
        "exercises": [
            {
                "name": "Бег",
                "sets": 1,
                "target": "30 мин",
                "input_type": "free",
                "prompt": "Сколько минут пробежал?",
                "description": "Разминочный бег.",
            },
            {
                "name": "One-leg FL → Straddle FL",
                "sets": 5,
                "target": "5–8 сек",
                "input_type": "time",
                "description": (
                    "One-leg: одна нога прямая горизонтально, вторая согнута. "
                    "Straddle: обе прямые и разведены. Работаешь с тем что держишь."
                ),
            },
            {
                "name": "FL негативы (full → tuck)",
                "sets": 3,
                "target": "3 повт",
                "input_type": "reps",
                "description": (
                    "Начинаешь в straddle FL, медленно (3–4 сек) опускаешься в tuck. "
                    "Специфичная нагрузка для финальной ступени."
                ),
            },
            {
                "name": "Straddle BL → Full BL попытки",
                "sets": 5,
                "target": "5–8 сек",
                "input_type": "time",
                "description": (
                    "Straddle back lever уверенно, потом попытки свести ноги вместе (full BL)."
                ),
            },
            {
                "name": "BL негативы",
                "sets": 3,
                "target": "3 повт",
                "input_type": "reps",
                "description": "Начинаешь в straddle или full BL, медленно опускаешься под контролем.",
            },
            {
                "name": "Weighted pull-ups (тяжёлые)",
                "sets": 4,
                "target": "3–5 повт",
                "input_type": "reps_weight",
                "description": "Максимальный вес с которым держишь технику. Долгий отдых.",
            },
            {
                "name": "Front lever pull-ups (tuck)",
                "sets": 3,
                "target": "4–5 повт",
                "input_type": "reps",
                "description": (
                    "Из позиции tuck front lever подтягиваешься вверх не меняя углы тела."
                ),
            },
            {
                "name": "Toes-to-bar (медленно)",
                "sets": 4,
                "target": "8–10 повт",
                "input_type": "reps",
                "description": "Без маха — медленный подъём и медленное опускание.",
            },
            {
                "name": "Compression sets",
                "sets": 3,
                "target": "30–40 сек",
                "input_type": "time",
                "description": "Сидишь, ноги в L-sit или чуть ниже. Долгое удержание.",
            },
            {
                "name": "Dragon flag (финал)",
                "sets": 3,
                "target": "4–6 повт",
                "input_type": "reps",
                "description": "Полная версия, с контролем в обеих фазах.",
            },
        ],
    },

    "phase3_B": {
        "title": "Фаза 3 — Тренировка Б (Толчок + advanced tuck planche + L-sit)",
        "exercises": [
            {
                "name": "Бег",
                "sets": 1,
                "target": "30 мин",
                "input_type": "free",
                "prompt": "Сколько минут пробежал?",
                "description": "Разминочный бег.",
            },
            {
                "name": "Advanced tuck planche hold",
                "sets": 5,
                "target": "5–8 сек",
                "input_type": "time",
                "description": (
                    "Как tuck planche, но бёдра опущены ниже — не прижаты к груди, "
                    "тело горизонтально длиннее."
                ),
            },
            {
                "name": "Tuck → Adv. tuck negatives",
                "sets": 3,
                "target": "3–5 повт",
                "input_type": "reps",
                "description": (
                    "Начинаешь в advanced tuck planche, медленно сгибаешься в tuck и опускаешься."
                ),
            },
            {
                "name": "Pseudo planche push-ups",
                "sets": 4,
                "target": "6–8 повт",
                "input_type": "reps",
                "description": (
                    "Отжимания с планшовым наклоном: руки пальцами назад или в стороны, "
                    "вес перенесён вперёд, плечи за линией рук."
                ),
            },
            {
                "name": "L-sit 25+ сек",
                "sets": 4,
                "target": "максимум (цель 25+ сек)",
                "input_type": "time",
                "description": "Full L-sit. Цель к концу фазы — 25 секунд и больше.",
            },
            {
                "name": "Korean dips",
                "sets": 4,
                "target": "5–6 повт",
                "input_type": "reps",
                "description": (
                    "Берёшься за брусья сзади — руки за спиной, кисти смотрят вперёд. "
                    "Медленно опускаешься: плечи уходят вперёд, локти назад. Без веса."
                ),
            },
            {
                "name": "HSPU / Handstand practice",
                "sets": 3,
                "target": "4–6 повт",
                "input_type": "reps",
                "description": (
                    "Отжимания в стойке на руках у стены или тренировка стойки. "
                    "Если стойки нет — pike HSPU с ногами на высоком возвышении."
                ),
            },
            {
                "name": "Adv. tuck planche push-ups",
                "sets": 3,
                "target": "3–4 повт",
                "input_type": "reps",
                "description": "Отжимания из advanced tuck planche. Делаешь сколько получается.",
            },
            {
                "name": "L-sit личный рекорд",
                "sets": 5,
                "target": "максимум",
                "input_type": "time",
                "description": "Пробуешь обновить рекорд каждую неделю.",
            },
            {
                "name": "Pike compression (интенсивно)",
                "sets": 3,
                "target": "40 сек",
                "input_type": "time",
                "description": "Долгое удержание с максимальным наклоном. К концу грудь к ногам.",
            },
            {
                "name": "Hollow body circles",
                "sets": 3,
                "target": "30 сек",
                "input_type": "time",
                "description": (
                    "В позиции hollow body делаешь медленные круговые движения сведёнными ногами."
                ),
            },
        ],
    },

    "phase3_C": {
        "title": "Фаза 3 — Тренировка В (Максимальные скиллы + сила)",
        "exercises": [
            {
                "name": "Бег",
                "sets": 1,
                "target": "30 мин",
                "input_type": "free",
                "prompt": "Сколько минут пробежал?",
                "description": "Разминочный бег.",
            },
            {
                "name": "FL — лучшая прогрессия",
                "sets": 4,
                "target": "максимум сек",
                "input_type": "time",
                "description": "Та ступень что держишь сейчас. Без компромисса с техникой.",
            },
            {
                "name": "BL — лучшая прогрессия",
                "sets": 4,
                "target": "максимум сек",
                "input_type": "time",
                "description": "То же для горизонта сзади.",
            },
            {
                "name": "PL — лучшая прогрессия",
                "sets": 3,
                "target": "максимум сек",
                "input_type": "time",
                "description": "То же для планша.",
            },
            {
                "name": "Muscle-up (чистые)",
                "sets": 3,
                "target": "2–4 повт",
                "input_type": "reps",
                "description": (
                    "Без рывка бёдрами. Если не получается — с минимальным рывком, работай над техникой."
                ),
            },
            {
                "name": "Weighted pull-ups (финал)",
                "sets": 4,
                "target": "4–5 повт",
                "input_type": "reps_weight",
                "description": "Тяжёлые. Хорошая амплитуда.",
            },
            {
                "name": "Weighted dips (финал)",
                "sets": 3,
                "target": "5–6 повт",
                "input_type": "reps_weight",
                "description": "Тяжёлые. Полная амплитуда.",
            },
            {
                "name": "L-sit личный рекорд (финал)",
                "sets": 4,
                "target": "максимум",
                "input_type": "time",
                "description": "Финальный замер прогресса.",
            },
            {
                "name": "Toes-to-bar (финал)",
                "sets": 3,
                "target": "10–12 повт",
                "input_type": "reps",
                "description": "Медленно и под контролем.",
            },
        ],
    },
}

# Порядок тренировок в цикле
WORKOUT_CYCLE = [
    "phase1_A", "phase1_B", "phase1_C",
    "phase2_A", "phase2_B", "phase2_C",
    "phase3_A", "phase3_B", "phase3_C",
]

# Карта неделя → фаза
def week_to_phase(week: int) -> int:
    if week <= 4:
        return 1
    elif week <= 8:
        return 2
    return 3

def phase_start_index(phase: int) -> int:
    return (phase - 1) * 3

def get_workout_by_key(key: str) -> dict:
    return WORKOUTS[key]
