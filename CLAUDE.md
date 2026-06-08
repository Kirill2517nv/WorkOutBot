# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup & Running

```bash
python -m venv venv
source venv/bin/activate          # Linux/Mac
# venv\Scripts\activate           # Windows
pip install -r requirements.txt
cp .env.example .env              # затем вставь BOT_TOKEN
python bot.py
```

Требуется Python 3.11+. Зависимости: `aiogram==3.13.1`, `aiosqlite==0.20.0`, `python-dotenv==1.0.1`.

## Architecture

Бот построен на **aiogram 3.x** с FSM (Finite State Machine) для ведения тренировок пошагово.

### Поток данных тренировки

1. Пользователь → `/train` → `handlers/training.py`
2. `TrainingStates` FSM: `waiting_for_week` → `waiting_for_result` (цикл по упражнениям)
3. Результат каждого упражнения сохраняется в `exercise_logs` через `database.py`
4. После последнего упражнения сессия закрывается (`completed_at` проставляется)

### Данные тренировок (`workouts.py`)

Все 9 тренировок захардкожены как словари в `WORKOUTS`. Цикл: `WORKOUT_CYCLE = [phase1_A, phase1_B, phase1_C, phase2_A, ...]`. Текущая позиция в цикле хранится в `user_state.next_workout_index` (инкрементируется при каждом старте тренировки).

Каждое упражнение имеет поле `input_type`:
- `"time"` → просит секунды подходов через пробел: `10 11 9`
- `"reps"` → просит повторения: `8 7 6`
- `"reps_weight"` → просит повторения×вес: `6×+10 5×+10`
- `"free"` → произвольный текст (используется для бега)

### База данных

SQLite через aiosqlite. Три таблицы:
- `user_state` — текущая неделя и индекс следующей тренировки в цикле
- `sessions` — факт тренировки (workout_key, started_at, completed_at)
- `exercise_logs` — результаты упражнений (sets_json — JSON-массив строк)

### Определение недели и фазы

`week_to_phase(week)` → 1/2/3. `phase_start_index(phase)` → стартовый индекс в `WORKOUT_CYCLE`. При первом `/train` бот спрашивает неделю, потом ведёт цикл автоматически.
