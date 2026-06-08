import json
import aiosqlite
from config import DB_PATH


async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS user_state (
                user_id INTEGER PRIMARY KEY,
                current_week INTEGER DEFAULT 1,
                next_workout_index INTEGER DEFAULT 0,
                started_at TEXT DEFAULT (datetime('now'))
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                workout_key TEXT NOT NULL,
                started_at TEXT DEFAULT (datetime('now')),
                completed_at TEXT
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS exercise_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id INTEGER NOT NULL,
                exercise_index INTEGER NOT NULL,
                exercise_name TEXT NOT NULL,
                sets_json TEXT,
                FOREIGN KEY (session_id) REFERENCES sessions(id)
            )
        """)
        await db.commit()


# --- user_state ---

async def get_user_state(user_id: int) -> dict | None:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT * FROM user_state WHERE user_id = ?", (user_id,)
        ) as cur:
            row = await cur.fetchone()
            return dict(row) if row else None


async def create_user_state(user_id: int, week: int, next_workout_index: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR REPLACE INTO user_state (user_id, current_week, next_workout_index) VALUES (?, ?, ?)",
            (user_id, week, next_workout_index),
        )
        await db.commit()


async def update_user_state(user_id: int, **kwargs):
    if not kwargs:
        return
    sets = ", ".join(f"{k} = ?" for k in kwargs)
    values = list(kwargs.values()) + [user_id]
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(f"UPDATE user_state SET {sets} WHERE user_id = ?", values)
        await db.commit()


# --- sessions ---

async def create_session(user_id: int, workout_key: str) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute(
            "INSERT INTO sessions (user_id, workout_key) VALUES (?, ?)",
            (user_id, workout_key),
        )
        await db.commit()
        return cur.lastrowid


async def complete_session(session_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE sessions SET completed_at = datetime('now') WHERE id = ?",
            (session_id,),
        )
        await db.commit()


async def get_last_sessions(user_id: int, limit: int = 10) -> list[dict]:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            """SELECT id, workout_key, started_at, completed_at
               FROM sessions WHERE user_id = ?
               ORDER BY started_at DESC LIMIT ?""",
            (user_id, limit),
        ) as cur:
            rows = await cur.fetchall()
            return [dict(r) for r in rows]


# --- exercise_logs ---

async def save_exercise_log(session_id: int, exercise_index: int, exercise_name: str, sets_data: list):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """INSERT OR REPLACE INTO exercise_logs
               (session_id, exercise_index, exercise_name, sets_json)
               VALUES (?, ?, ?, ?)""",
            (session_id, exercise_index, exercise_name, json.dumps(sets_data, ensure_ascii=False)),
        )
        await db.commit()


async def get_last_exercise_result(user_id: int, exercise_name: str) -> list | None:
    """Возвращает sets_json последней тренировки где было это упражнение."""
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            """SELECT el.sets_json
               FROM exercise_logs el
               JOIN sessions s ON el.session_id = s.id
               WHERE s.user_id = ? AND el.exercise_name = ? AND s.completed_at IS NOT NULL
               ORDER BY s.started_at DESC LIMIT 1""",
            (user_id, exercise_name),
        ) as cur:
            row = await cur.fetchone()
            if row and row[0]:
                return json.loads(row[0])
            return None


async def get_exercise_history(user_id: int, exercise_name: str) -> list[dict]:
    """Возвращает все логи по упражнению с датой тренировки."""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            """SELECT el.sets_json, s.started_at, s.workout_key
               FROM exercise_logs el
               JOIN sessions s ON el.session_id = s.id
               WHERE s.user_id = ? AND el.exercise_name = ?
               ORDER BY s.started_at ASC""",
            (user_id, exercise_name),
        ) as cur:
            rows = await cur.fetchall()
            return [dict(r) for r in rows]


async def get_all_exercise_names(user_id: int) -> list[str]:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            """SELECT DISTINCT el.exercise_name
               FROM exercise_logs el
               JOIN sessions s ON el.session_id = s.id
               WHERE s.user_id = ?
               ORDER BY el.exercise_name""",
            (user_id,),
        ) as cur:
            rows = await cur.fetchall()
            return [r[0] for r in rows]


async def get_exercises_for_session(session_id: int) -> list[dict]:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            """SELECT exercise_index, exercise_name, sets_json
               FROM exercise_logs WHERE session_id = ?
               ORDER BY exercise_index""",
            (session_id,),
        ) as cur:
            rows = await cur.fetchall()
            return [dict(r) for r in rows]
